import streamlit as st


def render_header():
    st.title("Badanie zjawiska AI Overreliance — POC")


def render_initial_decision(scenario):
    st.header("Decyzja początkowa")
    st.write(scenario.description)

    with st.form("initial_decision_form"):
        decisions = list(scenario.options.keys())

        decision = st.radio(
            "Twój wybór:",
            decisions,
            format_func=lambda decision: decision.value,
        )

        confidence = st.slider(
            "Jak pewny jesteś swojej decyzji?",
            min_value=0,
            max_value=100,
            value=50,
        )

        submitted = st.form_submit_button(
            "Potwierdź decyzję"
        )

    return decision, confidence, submitted


def render_ai_recommendation(ai):
    st.header("Rekomendacja AI")

    st.write(
        f"AI rekomenduje: **{ai.decision.value}**"
    )

    st.write(
        f"Pewność AI: **{ai.confidence}%**"
    )


def render_final_decision(scenario):
    with st.form("final_decision_form"):
        decisions = list(scenario.options.keys())

        decision = st.radio(
            "Twój wybór:",
            decisions,
            format_func=lambda decision: decision.value,
        )

        confidence = st.slider(
            "Jak pewny jesteś swojej ostatecznej decyzji?",
            min_value=0,
            max_value=100,
            value=50,
        )

        submitted = st.form_submit_button(
            "Potwierdź ostateczną decyzję"
        )

    return decision, confidence, submitted


def render_experiment_summary(experiments):
    st.header("Eksperyment zakończony")

    rows = []

    for index, experiment in enumerate(experiments, start=1):
        rows.append(
            {
                "Scenariusz": index,
                "Decyzja początkowa": experiment.initial_decision.value,
                "Decyzja końcowa": experiment.final_decision.value,
                "Wynik początkowy": experiment.initial_score,
                "Wynik końcowy": experiment.final_score,
                "Zmiana wyniku": experiment.score_change,
                "Zmiana decyzji": experiment.decision_changed,
                "Podążanie za AI": experiment.followed_ai,
                "Overreliance": experiment.overreliance,
            }
        )

    st.dataframe(
        rows,
        hide_index=True,
        width="stretch",
    )