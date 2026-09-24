from datetime import datetime, timezone
import sqlite3
from pathlib import Path

from models.domain import Observation


PROJECT_ROOT = Path(__file__).parent.parent.parent
DATABASE_PATH = PROJECT_ROOT / "data" / "experiment.db"


def get_connection(database_path: Path = DATABASE_PATH) -> sqlite3.Connection:
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database(
    database_path: Path = DATABASE_PATH,
) -> None:
    database_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with get_connection(database_path) as connection:
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

                initial_time REAL NOT NULL,
                final_time REAL NOT NULL,

                created_at TEXT NOT NULL
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS participants (
                participant_id TEXT PRIMARY KEY,
                age_group TEXT NOT NULL,
                education TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )


def save_participant(
    participant_id: str,
    age_group: str,
    education: str,
    database_path: Path = DATABASE_PATH,
) -> None:
    with get_connection(database_path) as connection:
        connection.execute(
            """
            INSERT INTO participants (
                participant_id,
                age_group,
                education,
                created_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                participant_id,
                age_group,
                education,
                datetime.now(timezone.utc).isoformat(),
            ),
        )


def save_observation(
    observation: Observation,
    database_path: Path = DATABASE_PATH,
) -> None:
    with get_connection(database_path) as connection:
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
                initial_time,
                final_time,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                observation.initial_time,
                observation.final_time,
                datetime.now(timezone.utc).isoformat(),
            ),
        )


def get_participants(
    database_path: Path = DATABASE_PATH,
) -> list[dict]:
    with get_connection(database_path) as connection:
        rows = connection.execute(
            """
            SELECT
                participant_id,
                age_group,
                education,
                created_at
            FROM participants
            ORDER BY created_at
            """
        ).fetchall()

    return [dict(row) for row in rows]


def get_observations(
    database_path: Path = DATABASE_PATH,
) -> list[dict]:
    with get_connection(database_path) as connection:
        rows = connection.execute(
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
                initial_time,
                final_time,
                created_at
            FROM observations
            ORDER BY created_at
            """
        ).fetchall()

    return [dict(row) for row in rows]


if __name__ == "__main__":
    print("Initializing database...")
    initialize_database()