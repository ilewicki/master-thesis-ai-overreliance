import streamlit as st


def render_header():
    st.title("Badanie zjawiska AI Overreliance — POC")


def render_welcome():
    st.title("Badanie podejmowania decyzji")

    st.write(
        """
        W tym badaniu sprawdzamy, w jaki sposób informacje
        przekazywane przez sztuczną inteligencję wpływają
        na podejmowanie decyzji.
        """
    )

    st.write(
        """
        Udział w badaniu polega na wykonaniu kilku krótkich
        zadań decyzyjnych. W każdym zadaniu najpierw podejmiesz
        własną decyzję, a następnie zobaczysz rekomendację AI
        i będziesz mieć możliwość zmiany swojej decyzji.
        """
    )

    return st.button("Rozpocznij badanie")


def render_participant_data():
    st.title("Informacje o uczestniku")

    st.write(
        """
        Przed rozpoczęciem właściwej części badania
        prosimy o podanie kilku podstawowych informacji.
        """
    )

    with st.form("participant_data_form"):
        age_group = st.radio(
            "Wiek:",
            [
                "18–24",
                "25–34",
                "35–44",
                "45–54",
                "55+",
            ],
        )

        education = st.radio(
            "Poziom wykształcenia:",
            [
                "Podstawowe",
                "Średnie",
                "Wyższe",
            ],
        )

        submitted = st.form_submit_button(
            "Przejdź do badania"
        )

    return age_group, education, submitted


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


def render_experiment_summary(observations):
    st.header("Eksperyment zakończony")
    rows = []

    for index, observation in enumerate(observations, start=1):
        rows.append(
            {
                "Scenariusz": index,
                "Decyzja początkowa": observation.initial_decision.value,
                "Czas decyzji początkowej": f"{observation.initial_time:.2f} s",
                "Decyzja końcowa": observation.final_decision.value,
                "Czas decyzji końcowej": f"{observation.final_time:.2f} s",
                "Wynik początkowy": observation.initial_score,
                "Wynik końcowy": observation.final_score,
                "Zmiana wyniku": observation.score_change,
                "Zmiana decyzji": observation.decision_changed,
                "Podążanie za AI": observation.followed_ai,
                "Overreliance": observation.overreliance,
            }
        )

    st.dataframe(
        rows,
        hide_index=True,
        width="stretch",
    )


def render_scenario_progress(
    current_index: int,
    total_scenarios: int,
):
    st.caption(
        f"Scenariusz {current_index + 1} "
        f"z {total_scenarios}"
    )