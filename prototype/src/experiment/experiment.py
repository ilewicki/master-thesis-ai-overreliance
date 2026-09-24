import time

import streamlit as st

from .experiment_service import (
    complete_scenario,
    move_to_next_scenario,
    submit_initial_decision,
)
from .experiment_ui import (
    render_ai_recommendation,
    render_experiment_summary,
    render_final_decision,
    render_header,
    render_initial_decision,
    render_participant_data,
    render_welcome,
    render_scenario_progress,
)
from models.domain import (
    ExperimentScenario,
    ExperimentSession,
    ExperimentStage,
)
from models.scenarios import EXPERIMENT_SCENARIOS
from persistence.database import (
    save_observation,
    save_participant,
)


def render_experiment():
    session = get_experiment_session()

    if session.stage == ExperimentStage.WELCOME:
        render_welcome_stage(session)
        return

    if session.stage == ExperimentStage.PARTICIPANT_DATA:
        render_participant_data_stage(session)
        return

    if session.stage == ExperimentStage.COMPLETE:
        render_experiment_summary(session.observations)
        return

    experiment_scenario = get_current_scenario(session)

    render_header()
    render_scenario_progress(
        current_index=session.current_scenario_index,
        total_scenarios=len(EXPERIMENT_SCENARIOS),
    )
    render_scenario(
        session=session,
        experiment_scenario=experiment_scenario,
    )


def get_experiment_session() -> ExperimentSession:
    if "experiment_session" not in st.session_state:
        raise RuntimeError(
            "Experiment session has not been initialized."
        )

    return st.session_state.experiment_session


def get_current_scenario(
    session: ExperimentSession,
) -> ExperimentScenario:
    return EXPERIMENT_SCENARIOS[
        session.current_scenario_index
    ]


def render_welcome_stage(
    session: ExperimentSession,
):
    start_experiment = render_welcome()

    if start_experiment:
        session.stage = ExperimentStage.PARTICIPANT_DATA
        st.rerun()


def render_participant_data_stage(
    session: ExperimentSession,
):
    age_group, education, submitted = render_participant_data()

    if not submitted:
        return

    session.age_group = age_group
    session.education = education

    save_participant(
        participant_id=session.participant_id,
        age_group=session.age_group,
        education=session.education,
    )

    session.stage = ExperimentStage.INITIAL
    st.rerun()


def render_scenario(
    session: ExperimentSession,
    experiment_scenario: ExperimentScenario,
):
    if session.stage == ExperimentStage.INITIAL:
        handle_initial_stage(
            session=session,
            experiment_scenario=experiment_scenario,
        )

    elif session.stage == ExperimentStage.AI:
        handle_ai_stage(
            session=session,
            experiment_scenario=experiment_scenario,
        )


def handle_initial_stage(
    session: ExperimentSession,
    experiment_scenario: ExperimentScenario,
):
    start_timer()

    decision, confidence, submitted = render_initial_decision(
        experiment_scenario.scenario
    )

    if not submitted:
        return

    initial_time = stop_timer()

    submit_initial_decision(
        session=session,
        scenario=experiment_scenario.scenario,
        decision=decision,
        confidence=confidence,
        initial_time=initial_time,
    )

    st.rerun()


def handle_ai_stage(
    session: ExperimentSession,
    experiment_scenario: ExperimentScenario,
):
    start_timer()

    render_ai_recommendation(
        experiment_scenario.ai_recommendation
    )

    decision, confidence, submitted = render_final_decision(
        experiment_scenario.scenario
    )

    if not submitted:
        return

    final_time = stop_timer()

    observation = complete_scenario(
        session=session,
        scenario=experiment_scenario.scenario,
        ai=experiment_scenario.ai_recommendation,
        final_decision=decision,
        final_confidence=confidence,
        final_time=final_time,
    )

    save_observation(observation)

    move_to_next_scenario(
        session=session,
        total_scenarios=len(EXPERIMENT_SCENARIOS),
    )

    st.rerun()


def start_timer():
    if "scenario_start_time" not in st.session_state:
        st.session_state.scenario_start_time = time.monotonic()


def stop_timer() -> float:
    start_time = st.session_state.pop("scenario_start_time")
    return time.monotonic() - start_time