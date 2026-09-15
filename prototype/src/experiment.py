import streamlit as st

from database import save_observation
from models import ExperimentState
from scenarios import (
    AI_RECOMMENDATION_01,
    AI_RECOMMENDATION_02,
    SCENARIO_01,
    SCENARIO_02,
)
from scoring import (
    calculate_decision_change,
    calculate_followed_ai,
    calculate_overreliance,
    calculate_score,
)
from experiment_ui import (
    render_ai_recommendation,
    render_experiment_summary,
    render_final_decision,
    render_header,
    render_initial_decision,
)


SCENARIOS = [
    (SCENARIO_01, AI_RECOMMENDATION_01),
    (SCENARIO_02, AI_RECOMMENDATION_02),
]


def render_experiment():
    participant_id = st.session_state.participant_id
    experiment = get_experiment_state()

    current_scenario_index = get_current_scenario_index()

    if current_scenario_index >= len(SCENARIOS):
        render_experiment_summary(
            get_completed_experiments()
        )
        return

    scenario, ai = SCENARIOS[current_scenario_index]

    # Header UI
    render_header()
    st.caption(
        f"Scenariusz badawczy nr {current_scenario_index + 1} z {len(SCENARIOS)}"
    )

    if experiment.stage == "initial":
        initial_stage(experiment, scenario)

    elif experiment.stage == "ai":
        ai_stage(
            experiment,
            scenario,
            ai,
            participant_id,
        )

    elif experiment.stage == "complete":
        render_experiment_summary(
            get_completed_experiments()
        )


def get_experiment_state() -> ExperimentState:
    if "experiment" not in st.session_state:
        st.session_state.experiment = ExperimentState()

    return st.session_state.experiment


def get_completed_experiments() -> list[ExperimentState]:
    if "completed_experiments" not in st.session_state:
        st.session_state.completed_experiments = []

    return st.session_state.completed_experiments


def get_current_scenario_index() -> int:
    if "current_scenario_index" not in st.session_state:
        st.session_state.current_scenario_index = 0

    return st.session_state.current_scenario_index


def initial_stage(experiment: ExperimentState, scenario):
    decision, confidence, submitted = render_initial_decision(scenario)

    if not submitted:
        return

    experiment.initial_decision = decision
    experiment.initial_confidence = confidence
    experiment.initial_score = calculate_score(
        scenario,
        decision,
    )
    experiment.stage = "ai"

    st.rerun()


def ai_stage(
    experiment: ExperimentState,
    scenario,
    ai,
    participant_id: str,
):
    render_ai_recommendation(ai)

    decision, confidence, submitted = render_final_decision(scenario)

    if not submitted:
        return

    experiment.final_decision = decision
    experiment.final_confidence = confidence

    experiment.final_score = calculate_score(
        scenario,
        decision,
    )

    experiment.score_change = (
        experiment.final_score - experiment.initial_score
    )

    experiment.decision_changed = calculate_decision_change(
        experiment.initial_decision,
        experiment.final_decision,
    )

    experiment.followed_ai = calculate_followed_ai(
        experiment.final_decision,
        ai.decision,
    )

    experiment.ai_correct = (
        ai.decision == scenario.optimal_decision
    )

    experiment.overreliance = calculate_overreliance(
        experiment.initial_decision,
        experiment.final_decision,
        ai.decision,
        scenario.optimal_decision,
    )

    save_observation(
        scenario_id=scenario.scenario_id,
        ai_recommendation=ai.decision,
        ai_confidence=ai.confidence,
        experiment=experiment,
        participant_id=participant_id,
    )

    experiment.observation_saved = True

    completed_experiments = get_completed_experiments()
    completed_experiments.append(experiment)

    move_to_next_scenario()


def move_to_next_scenario():
    current_scenario_index = get_current_scenario_index()

    if current_scenario_index + 1 < len(SCENARIOS):
        st.session_state.current_scenario_index += 1

        #  new scenario -> new state
        st.session_state.experiment = ExperimentState()

    else:
        st.session_state.experiment.stage = "complete"

    st.rerun()