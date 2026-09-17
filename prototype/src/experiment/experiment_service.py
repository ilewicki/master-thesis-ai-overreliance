from models.models import (
    AIRecommendation,
    Decision,
    ExperimentSession,
    ExperimentStage,
    Observation,
    Scenario,
    ScenarioState,
)
from models.scoring import (
    calculate_decision_change,
    calculate_followed_ai,
    calculate_overreliance,
    calculate_score,
)


def submit_initial_decision(
    session: ExperimentSession,
    scenario: Scenario,
    decision: Decision,
    confidence: int,
) -> None:
    scenario_state = session.current_scenario

    scenario_state.initial_decision = decision
    scenario_state.initial_confidence = confidence
    scenario_state.initial_score = calculate_score(
        scenario,
        decision,
    )

    session.stage = ExperimentStage.AI


def complete_scenario(
    session: ExperimentSession,
    scenario: Scenario,
    ai: AIRecommendation,
    final_decision: Decision,
    final_confidence: int,
) -> Observation:
    scenario_state = session.current_scenario

    scenario_state.final_decision = final_decision
    scenario_state.final_confidence = final_confidence

    if scenario_state.initial_decision is None:
        raise RuntimeError("Initial decision has not been submitted.")

    if scenario_state.initial_confidence is None:
        raise RuntimeError("Initial confidence has not been submitted.")

    if scenario_state.initial_score is None:
        raise RuntimeError("Initial score has not been calculated.")

    scenario_state.final_score = calculate_score(
        scenario,
        final_decision,
    )

    scenario_state.score_change = (
        scenario_state.final_score
        - scenario_state.initial_score
    )

    scenario_state.decision_changed = calculate_decision_change(
        scenario_state.initial_decision,
        final_decision,
    )

    scenario_state.followed_ai = calculate_followed_ai(
        final_decision,
        ai.decision,
    )

    scenario_state.ai_correct = (
        ai.decision == scenario.optimal_decision
    )

    scenario_state.overreliance = calculate_overreliance(
        scenario_state.initial_decision,
        final_decision,
        ai.decision,
        scenario.optimal_decision,
    )

    observation = Observation(
        participant_id=session.participant_id,
        scenario_id=scenario.scenario_id,
        initial_decision=scenario_state.initial_decision,
        initial_confidence=scenario_state.initial_confidence,
        initial_score=scenario_state.initial_score,
        ai_recommendation=ai.decision,
        ai_confidence=ai.confidence,
        ai_correct=scenario_state.ai_correct,
        final_decision=scenario_state.final_decision,
        final_confidence=scenario_state.final_confidence,
        final_score=scenario_state.final_score,
        score_change=scenario_state.score_change,
        decision_changed=scenario_state.decision_changed,
        followed_ai=scenario_state.followed_ai,
        overreliance=scenario_state.overreliance,
    )

    session.observations.append(observation)

    return observation


def move_to_next_scenario(
    session: ExperimentSession,
    total_scenarios: int,
) -> None:
    session.current_scenario_index += 1
    session.current_scenario = ScenarioState()

    if session.current_scenario_index >= total_scenarios:
        session.stage = ExperimentStage.COMPLETE
    else:
        session.stage = ExperimentStage.INITIAL