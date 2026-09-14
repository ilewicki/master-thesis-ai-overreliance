import streamlit as st


def render_header():
    st.title("AI Overreliance — POC")


def render_initial_decision(scenario):
    st.header("Decyzja początkowa")
    st.write(scenario.description)

    with st.form("initial_decision_form"):
        decision = st.radio(
            "Twój wybór:",
            list(scenario.options.keys()),
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
        f"AI rekomenduje: **{ai.decision}**"
    )

    st.write(
        f"Pewność AI: **{ai.confidence}%**"
    )


def render_final_decision(scenario):
    with st.form("final_decision_form"):
        decision = st.radio(
            "Jaka jest Twoja ostateczna decyzja?",
            list(scenario.options.keys()),
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


def render_experiment_summary(experiment):
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