from models.models import Decision, Scenario, Option
from models.scoring import (
    calculate_decision_change,
    calculate_followed_ai,
    calculate_overreliance,
    calculate_score,
)


def test_calculate_score():
    scenario = Scenario(
        scenario_id="TEST",
        description="Test",
        options={
            Decision.A: Option(
                name=Decision.A,
                value=80,
                cost=20,
            ),
            Decision.B: Option(
                name=Decision.B,
                value=110,
                cost=40,
            ),
        },
        optimal_decision=Decision.B,
    )

    assert calculate_score(scenario, Decision.A) == 60
    assert calculate_score(scenario, Decision.B) == 70


def test_overreliance_when_participant_switches_from_correct_to_wrong_ai():
    assert calculate_overreliance(
        initial_decision=Decision.B,
        final_decision=Decision.A,
        ai_decision=Decision.A,
        optimal_decision=Decision.B,
    ) is True


def test_no_overreliance_when_ai_is_correct():
    assert calculate_overreliance(
        initial_decision=Decision.A,
        final_decision=Decision.B,
        ai_decision=Decision.B,
        optimal_decision=Decision.B,
    ) is False