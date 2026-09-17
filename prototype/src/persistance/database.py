from datetime import datetime, timezone
import sqlite3
from pathlib import Path

from models.models import Observation


DATABASE_PATH = Path(__file__).parent.parent / "data" / "experiment.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    connection = get_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scenario_id TEXT NOT NULL,
            participant_id TEXT NOT NULL,

            initial_decision TEXT NOT NULL,
            initial_confidence INTEGER NOT NULL,
            initial_score INTEGER NOT NULL,

            ai_recommendation TEXT NOT NULL,
            ai_confidence INTEGER NOT NULL,
            ai_correct INTEGER NOT NULL,

            final_decision TEXT NOT NULL,
            final_confidence INTEGER NOT NULL,
            final_score INTEGER NOT NULL,

            score_change INTEGER NOT NULL,
            decision_changed INTEGER NOT NULL,
            followed_ai INTEGER NOT NULL,
            overreliance INTEGER NOT NULL,

            created_at TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()


def save_observation(
    observation: Observation,
):
    connection = get_connection()

    connection.execute(
        """
        INSERT INTO observations (
            scenario_id,
            participant_id,
            initial_decision,
            initial_confidence,
            initial_score,
            ai_recommendation,
            ai_confidence,
            ai_correct,
            final_decision,
            final_confidence,
            final_score,
            score_change,
            decision_changed,
            followed_ai,
            overreliance,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            observation.scenario_id,
            observation.participant_id,
            observation.initial_decision.value,
            observation.initial_confidence,
            observation.initial_score,
            observation.ai_recommendation.value,
            observation.ai_confidence,
            observation.ai_correct,
            observation.final_decision.value,
            observation.final_confidence,
            observation.final_score,
            observation.score_change,
            observation.decision_changed,
            observation.followed_ai,
            observation.overreliance,
            datetime.now(timezone.utc).isoformat(),
        ),
    )

    connection.commit()
    connection.close()


def get_observations():
    connection = get_connection()

    cursor = connection.execute(
        """
        SELECT
            id,
            participant_id,
            scenario_id,
            initial_decision,
            initial_confidence,
            initial_score,
            ai_recommendation,
            ai_confidence,
            ai_correct,
            final_decision,
            final_confidence,
            final_score,
            score_change,
            decision_changed,
            followed_ai,
            overreliance,
            created_at
        FROM observations
        ORDER BY id DESC
        """
    )

    observations = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return observations


if __name__ == "__main__":
    print("Initializing database...")
    initialize_database()