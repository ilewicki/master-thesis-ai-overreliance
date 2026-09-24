import streamlit as st

from persistence.database import (
    get_observations,
    get_participants,
)


def render_dashboard():
    st.title("Dashboard badania")

    participants = get_participants()
    observations = get_observations()

    if not participants:
        st.info("Brak uczestników badania.")
        return

    render_summary_metrics(participants, observations)

    st.divider()

    render_scenario_summary(observations)

    st.divider()

    render_score_summary(observations)

    st.divider()

    render_participants(participants)


def render_summary_metrics(participants, observations):
    total_participants = len(participants)
    total_observations = len(observations)

    changed_decisions = sum(
        observation["decision_changed"]
        for observation in observations
    )

    followed_ai = sum(
        observation["followed_ai"]
        for observation in observations
    )

    overreliance = sum(
        observation["overreliance"]
        for observation in observations
    )

    columns = st.columns(5)

    columns[0].metric(
        "Uczestnicy",
        total_participants,
    )

    columns[1].metric(
        "Obserwacje",
        total_observations,
    )

    columns[2].metric(
        "Zmiana decyzji",
        changed_decisions,
    )

    columns[3].metric(
        "Podążanie za AI",
        followed_ai,
    )

    columns[4].metric(
        "Overreliance",
        overreliance,
    )


def render_scenario_summary(observations):
    st.subheader("Wyniki według scenariusza")

    scenario_ids = sorted(
        {observation["scenario_id"] for observation in observations}
    )

    rows = []

    for scenario_id in scenario_ids:
        scenario_observations = [
            observation
            for observation in observations
            if observation["scenario_id"] == scenario_id
        ]

        count = len(scenario_observations)

        changed = sum(
            observation["decision_changed"]
            for observation in scenario_observations
        )

        followed_ai = sum(
            observation["followed_ai"]
            for observation in scenario_observations
        )

        overreliance = sum(
            observation["overreliance"]
            for observation in scenario_observations
        )

        average_score_change = (
            sum(
                observation["score_change"]
                for observation in scenario_observations
            )
            / count
        )

        rows.append(
            {
                "Scenariusz": scenario_id,
                "Obserwacje": count,
                "Zmiana decyzji": changed,
                "Podążanie za AI": followed_ai,
                "Overreliance": overreliance,
                "Śr. zmiana wyniku": round(
                    average_score_change,
                    2,
                ),
            }
        )

    st.dataframe(
        rows,
        hide_index=True,
        width="stretch",
    )


def render_participants(participants):
    st.subheader("Uczestnicy")

    rows = [
        {
            "Participant ID": participant["participant_id"],
            "Wiek": participant["age_group"],
            "Wykształcenie": participant["education"],
            "Rozpoczęcie": participant["created_at"],
        }
        for participant in participants
    ]

    st.dataframe(
        rows,
        hide_index=True,
        width="stretch",
    )


def render_score_summary(observations):
    st.subheader("Wpływ zmiany decyzji na wynik")

    score_changes = [
        observation["score_change"]
        for observation in observations
    ]

    if not score_changes:
        return

    average_change = sum(score_changes) / len(score_changes)

    positive = sum(
        score_change > 0
        for score_change in score_changes
    )

    negative = sum(
        score_change < 0
        for score_change in score_changes
    )

    unchanged = sum(
        score_change == 0
        for score_change in score_changes
    )

    columns = st.columns(4)

    columns[0].metric(
        "Średnia zmiana wyniku",
        f"{average_change:.2f}",
    )

    columns[1].metric(
        "Wynik poprawiony",
        positive,
    )

    columns[2].metric(
        "Wynik pogorszony",
        negative,
    )

    columns[3].metric(
        "Bez zmiany",
        unchanged,
    )