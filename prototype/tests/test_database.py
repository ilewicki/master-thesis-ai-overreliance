from models.models import Decision, Observation

from persistance.database import (
    get_observations,
    initialize_database,
    save_observation,
)


def test_save_and_get_observation(tmp_path):
    database_path = tmp_path / "test.db"

    initialize_database(database_path)

    observation = Observation(
        participant_id="TEST",
        scenario_id="S01",

        initial_decision=Decision.B,
        initial_confidence=90,
        initial_score=70,

        ai_recommendation=Decision.A,
        ai_confidence=95,
        ai_correct=False,

        final_decision=Decision.A,
        final_confidence=80,
        final_score=60,

        score_change=-10,
        decision_changed=True,
        followed_ai=True,
        overreliance=True,

        initial_time=12.5,
        final_time=8.3,
    )

    save_observation(
        observation,
        database_path,
    )

    observations = get_observations(database_path)

    assert len(observations) == 1

    saved = observations[0]

    assert saved["participant_id"] == "TEST"
    assert saved["scenario_id"] == "S01"

    assert saved["initial_decision"] == "B"
    assert saved["initial_confidence"] == 90
    assert saved["initial_score"] == 70

    assert saved["ai_recommendation"] == "A"
    assert saved["ai_confidence"] == 95
    assert saved["ai_correct"] == 0

    assert saved["final_decision"] == "A"
    assert saved["final_confidence"] == 80
    assert saved["final_score"] == 60

    assert saved["score_change"] == -10
    assert saved["decision_changed"] == 1
    assert saved["followed_ai"] == 1
    assert saved["overreliance"] == 1

    assert saved["initial_time"] == 12.5
    assert saved["final_time"] == 8.3

    assert saved["created_at"] is not None