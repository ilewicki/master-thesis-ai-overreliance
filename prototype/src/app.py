import streamlit as st

from models import ExperimentState
from scenarios import AI_RECOMMENDATION_01, SCENARIO_01
from scoring import (
    calculate_decision_change,
    calculate_followed_ai,
    calculate_overreliance,
    calculate_score,
)


scenario = SCENARIO_01
ai = AI_RECOMMENDATION_01


st.title("AI Overreliance — POC")


# ----------------------------------------------------------------------
# Experiment state

if "experiment" not in st.session_state:
    st.session_state.experiment = ExperimentState()

experiment = st.session_state.experiment


# ----------------------------------------------------------------------
# Initial decision

if experiment.stage == "initial":
    st.header("Scenariusz 01")
    st.write(scenario.description)

    with st.form("initial_decision_form"):
        initial_decision = st.radio(
            "Twój wybór:",
            list(scenario.options.keys()),
        )

        initial_confidence = st.slider(
            "Jak pewny jesteś swojej decyzji?",
            min_value=0,
            max_value=100,
            value=50,
        )

        submitted = st.form_submit_button(
            "Potwierdź decyzję"
        )

    if submitted:
        experiment.initial_decision = initial_decision
        experiment.initial_confidence = initial_confidence
        experiment.initial_score = calculate_score(
            scenario,
            initial_decision,
        )
        experiment.stage = "ai"

        st.rerun()


# ----------------------------------------------------------------------
# AI recommendation and final decision

if experiment.stage == "ai":
    st.header("Rekomendacja AI")

    st.write(
        f"AI rekomenduje: **{ai.decision}**"
    )

    st.write(
        f"Pewność AI: **{ai.confidence}%**"
    )

    with st.form("final_decision_form"):
        final_decision = st.radio(
            "Jaka jest Twoja ostateczna decyzja?",
            list(scenario.options.keys()),
        )

        final_confidence = st.slider(
            "Jak pewny jesteś swojej ostatecznej decyzji?",
            min_value=0,
            max_value=100,
            value=50,
        )

        submitted = st.form_submit_button(
            "Potwierdź ostateczną decyzję"
        )

    if submitted:
        experiment.final_decision = final_decision
        experiment.final_confidence = final_confidence

        experiment.final_score = calculate_score(
            scenario,
            final_decision,
        )

        experiment.score_change = (
            experiment.final_score
            - experiment.initial_score
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

        experiment.stage = "complete"

        st.rerun()


# ----------------------------------------------------------------------
# Experiment summary

if experiment.stage == "complete":
    st.header("Eksperyment zakończony")

    st.write(
        f"Decyzja początkowa: "
        f"**{experiment.initial_decision}**"
    )

    st.write(
        f"Decyzja końcowa: "
        f"**{experiment.final_decision}**"
    )

    st.write(
        f"Wynik początkowy: "
        f"**{experiment.initial_score} pkt**"
    )

    st.write(
        f"Wynik końcowy: "
        f"**{experiment.final_score} pkt**"
    )

    st.write(
        f"Zmiana wyniku: "
        f"**{experiment.score_change:+d} pkt**"
    )

    st.write(
        f"Zmiana decyzji: "
        f"**{experiment.decision_changed}**"
    )

    st.write(
        f"Podążanie za AI: "
        f"**{experiment.followed_ai}**"
    )

    st.write(
        f"Overreliance: "
        f"**{experiment.overreliance}**"
    )