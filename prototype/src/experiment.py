import streamlit as st

from database import save_observation
from models import ExperimentState
from scenarios import AI_RECOMMENDATION_01, SCENARIO_01
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


def render_experiment():
    scenario = SCENARIO_01
    ai = AI_RECOMMENDATION_01
    experiment = get_experiment_state()

    render_header()

    if experiment.stage == "initial":
        initial_stage(experiment, scenario)

    elif experiment.stage == "ai":
        ai_stage(experiment, scenario, ai)

    elif experiment.stage == "complete":
        render_experiment_summary(experiment)


def get_experiment_state() -> ExperimentState:
    if "experiment" not in st.session_state:
        st.session_state.experiment = ExperimentState()

    return st.session_state.experiment


def initial_stage(experiment, scenario):
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


def ai_stage(experiment, scenario, ai):
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
    )

    experiment.observation_saved = True
    experiment.stage = "complete"

    st.rerun()