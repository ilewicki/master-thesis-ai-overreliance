import streamlit as st
import time

from .experiment_ui import (
    render_ai_recommendation,
    render_experiment_summary,
    render_final_decision,
    render_header,
    render_initial_decision,
)
from models.models import (
    AIRecommendation,
    ExperimentSession,
    ExperimentStage,
    Scenario,
)
from models.scenarios import (
    AI_RECOMMENDATION_01,
    AI_RECOMMENDATION_02,
    SCENARIO_01,
    SCENARIO_02,
)

from .experiment_service import (
    complete_scenario,
    move_to_next_scenario,
    submit_initial_decision,
)

from persistance.database import save_observation


SCENARIOS = [
    (SCENARIO_01, AI_RECOMMENDATION_01),
    (SCENARIO_02, AI_RECOMMENDATION_02),
]


def render_experiment():
    session = get_experiment_session()

    if session.stage == ExperimentStage.COMPLETE:
        render_experiment_summary(session.observations)
        return

    scenario, ai = get_current_scenario(session)

    render_header()

    render_scenario_progress(
        session.current_scenario_index,
        len(SCENARIOS),
    )

    render_scenario(
        session=session,
        scenario=scenario,
        ai=ai,
    )


def get_experiment_session() -> ExperimentSession:
    if "experiment_session" not in st.session_state:
        raise RuntimeError(
            "Experiment session has not been initialized."
        )

    return st.session_state.experiment_session


def get_current_scenario(
    session: ExperimentSession,
) -> tuple[Scenario, AIRecommendation]:
    return SCENARIOS[session.current_scenario_index]


def render_scenario(
    session: ExperimentSession,
    scenario: Scenario,
    ai: AIRecommendation,
):
    if session.stage == ExperimentStage.INITIAL:
        initial_stage(
            session,
            scenario,
        )

    elif session.stage == ExperimentStage.AI:
        ai_stage(
            session,
            scenario,
            ai,
        )


def initial_stage(
    session: ExperimentSession,
    scenario: Scenario,
):  
    start_timer()
    
    decision, confidence, submitted = render_initial_decision(
        scenario
    )

    if not submitted:
        return

    initial_time = stop_timer()

    submit_initial_decision(
        session=session,
        scenario=scenario,
        decision=decision,
        confidence=confidence,
        initial_time=initial_time,
    )
    st.session_state.pop("scenario_start_time", None)

    st.rerun()


def ai_stage(
    session: ExperimentSession,
    scenario: Scenario,
    ai: AIRecommendation,
):
    start_timer()

    render_ai_recommendation(ai)

    decision, confidence, submitted = render_final_decision(
        scenario
    )

    if not submitted:
        return

    final_time = stop_timer()

    observation = complete_scenario(
        session=session,
        scenario=scenario,
        ai=ai,
        final_decision=decision,
        final_confidence=confidence,
        final_time=final_time,
    )
    
    # DB connection
    save_observation(observation)

    move_to_next_scenario(
        session=session,
        total_scenarios=len(SCENARIOS),
    )
    st.session_state.pop("scenario_start_time", None)
    st.rerun()


def render_scenario_progress(
    current_index: int,
    total_scenarios: int,
):
    st.caption(
        f"Scenariusz {current_index + 1} "
        f"z {total_scenarios}"
    )


def start_timer():
    if "scenario_start_time" not in st.session_state:
        st.session_state.scenario_start_time = time.monotonic()


def stop_timer() -> float:
    start_time = st.session_state.scenario_start_time
    return time.monotonic() - start_time