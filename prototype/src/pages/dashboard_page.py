import pandas as pd
import streamlit as st

from database import get_observations


def render_dashboard():
    st.title("📊 Dashboard")

    if st.button("Odśwież dane"):
        st.rerun()

    observations = get_observations()

    if not observations:
        st.info("Brak danych eksperymentu.")
        return

    dataframe = pd.DataFrame(observations)

    selected_scenario = render_filters(dataframe)

    filtered_dataframe = filter_observations(
        dataframe,
        selected_scenario,
    )

    if filtered_dataframe.empty:
        st.info("Brak obserwacji dla wybranego filtra.")
        return

    render_summary(filtered_dataframe)
    render_charts(filtered_dataframe)
    render_observations(filtered_dataframe)


def render_filters(dataframe):
    scenarios = ["Wszystkie"] + sorted(
        dataframe["scenario_id"].unique().tolist()
    )

    return st.selectbox(
        "Scenariusz",
        scenarios,
    )


def filter_observations(dataframe, selected_scenario):
    if selected_scenario == "Wszystkie":
        return dataframe

    return dataframe[
        dataframe["scenario_id"] == selected_scenario
    ]


def render_summary(dataframe):
    total = len(dataframe)

    overreliance_count = dataframe["overreliance"].sum()

    overreliance_rate = (
        overreliance_count / total * 100
    )

    ai_helped_count = (
        (dataframe["ai_correct"] == 1)
        & (dataframe["score_change"] > 0)
    ).sum()

    average_score_change = dataframe["score_change"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Obserwacje",
        total,
    )

    col2.metric(
        "Overreliance",
        f"{overreliance_rate:.1f}%",
    )

    col3.metric(
        "AI pomogło",
        ai_helped_count,
    )

    col4.metric(
        "Śr. zmiana wyniku",
        f"{average_score_change:+.1f}",
    )


def render_charts(dataframe):
    st.subheader("Wyniki")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Overreliance")

        overreliance_data = (
            dataframe["overreliance"]
            .value_counts()
            .rename(
                {
                    0: "Brak overreliance",
                    1: "Overreliance",
                }
            )
        )

        st.bar_chart(overreliance_data)

    with col2:
        st.write("Zmiana wyniku")

        st.bar_chart(
            dataframe["score_change"]
        )


def render_observations(dataframe):
    st.subheader("Obserwacje")

    display_dataframe = dataframe.rename(
        columns={
            "id": "ID",
            "scenario_id": "Scenariusz",
            "initial_decision": "Decyzja początkowa",
            "initial_confidence": "Pewność początkowa",
            "initial_score": "Wynik początkowy",
            "ai_recommendation": "Rekomendacja AI",
            "ai_confidence": "Pewność AI",
            "ai_correct": "AI poprawne",
            "final_decision": "Decyzja końcowa",
            "final_confidence": "Pewność końcowa",
            "final_score": "Wynik końcowy",
            "score_change": "Zmiana wyniku",
            "decision_changed": "Zmiana decyzji",
            "followed_ai": "Podążanie za AI",
            "overreliance": "Overreliance",
            "created_at": "Utworzono",
        }
    )

    st.dataframe(
        display_dataframe,
        width=True,
        hide_index=True,
    )