from models.domain import (
    AIRecommendation,
    Decision,
    ExperimentSession,
    ExperimentStage,
)
from models.scenarios import (
    SCENARIO_01,
    SCENARIO_02,
)
from experiment.experiment_service import (
    complete_scenario,
    move_to_next_scenario,
    submit_initial_decision,
)


def test_submit_initial_decision():
    session = ExperimentSession(
        participant_id="TEST"
    )

    submit_initial_decision(
        session=session,
        scenario=SCENARIO_01,
        decision=Decision.B,
        confidence=80,
        initial_time=10.0,
    )

    state = session.current_scenario

    assert state.initial_decision == Decision.B
    assert state.initial_confidence == 80
    assert state.initial_score == 70
    assert state.initial_time == 10.0


def test_complete_scenario_creates_overreliance_observation():
    session = ExperimentSession(
        participant_id="TEST"
    )

    submit_initial_decision(
        session=session,
        scenario=SCENARIO_01,
        decision=Decision.B,
        confidence=90,
        initial_time=10.0,
    )

    ai = AIRecommendation(
        decision=Decision.A,
        confidence=95,
    )

    observation = complete_scenario(
        session=session,
        scenario=SCENARIO_01,
        ai=ai,
        final_decision=Decision.A,
        final_confidence=80,
        final_time=5.0
    )

    assert observation.participant_id == "TEST"
    assert observation.scenario_id == "S01"

    assert observation.initial_decision == Decision.B
    assert observation.ai_recommendation == Decision.A
    assert observation.final_decision == Decision.A

    assert observation.initial_score == 70
    assert observation.final_score == 60
    assert observation.score_change == -10

    assert observation.decision_changed is True
    assert observation.followed_ai is True
    assert observation.ai_correct is False
    assert observation.overreliance is True

    assert observation.initial_time == 10.0
    assert observation.final_time == 5.0


def test_complete_scenario_when_ai_is_correct():
    session = ExperimentSession(
        participant_id="TEST"
    )

    submit_initial_decision(
        session=session,
        scenario=SCENARIO_02,
        decision=Decision.A,
        confidence=60,
        initial_time=10.0,
    )

    ai = AIRecommendation(
        decision=Decision.B,
        confidence=95,
    )

    observation = complete_scenario(
        session=session,
        scenario=SCENARIO_02,
        ai=ai,
        final_decision=Decision.B,
        final_confidence=90,
        final_time=5.0
    )

    assert observation.initial_score == 60
    assert observation.final_score == 70
    assert observation.score_change == 10

    assert observation.decision_changed is True
    assert observation.followed_ai is True
    assert observation.ai_correct is True
    assert observation.overreliance is False

    assert observation.initial_time == 10.0
    assert observation.final_time == 5.0


def test_move_to_next_scenario():
    session = ExperimentSession(
        participant_id="TEST",
        current_scenario_index=0,
        stage=ExperimentStage.AI,
    )

    move_to_next_scenario(
        session=session,
        total_scenarios=2,
    )

    assert session.current_scenario_index == 1
    assert session.stage == ExperimentStage.INITIAL


def test_move_to_next_scenario_completes_session():
    session = ExperimentSession(
        participant_id="TEST",
        current_scenario_index=1,
        stage=ExperimentStage.AI,
    )

    move_to_next_scenario(
        session=session,
        total_scenarios=2,
    )

    assert session.current_scenario_index == 2
    assert session.stage == ExperimentStage.COMPLETE