from models.domain import (
    AIRecommendation,
    Decision,
    ExperimentSession,
    ExperimentStage,
    Observation,
    Scenario,
    ScenarioState,
)
from experiment.scoring import (
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
    initial_time: float,
) -> None:
    scenario_state = session.current_scenario

    scenario_state.initial_decision = decision
    scenario_state.initial_confidence = confidence
    scenario_state.initial_score = calculate_score(
        scenario,
        decision,
    )
    scenario_state.initial_time = initial_time

    session.stage = ExperimentStage.AI


def complete_scenario(
    session: ExperimentSession,
    scenario: Scenario,
    ai: AIRecommendation,
    final_decision: Decision,
    final_confidence: int,
    final_time: float,
) -> Observation:
    scenario_state = session.current_scenario

    _validate_initial_state(scenario_state)

    initial_decision = scenario_state.initial_decision
    initial_confidence = scenario_state.initial_confidence
    initial_score = scenario_state.initial_score
    initial_time = scenario_state.initial_time

    final_score = calculate_score(
        scenario,
        final_decision,
    )

    score_change = final_score - initial_score

    decision_changed = calculate_decision_change(
        initial_decision,
        final_decision,
    )

    followed_ai = calculate_followed_ai(
        final_decision,
        ai.decision,
    )

    ai_correct = ai.decision == scenario.optimal_decision

    overreliance = calculate_overreliance(
        initial_decision,
        final_decision,
        ai.decision,
        scenario.optimal_decision,
    )

    observation = Observation(
        participant_id=session.participant_id,
        scenario_id=scenario.scenario_id,
        initial_decision=initial_decision,
        initial_confidence=initial_confidence,
        initial_score=initial_score,
        initial_time=initial_time,
        ai_recommendation=ai.decision,
        ai_confidence=ai.confidence,
        ai_correct=ai_correct,
        final_decision=final_decision,
        final_confidence=final_confidence,
        final_score=final_score,
        final_time=final_time,
        score_change=score_change,
        decision_changed=decision_changed,
        followed_ai=followed_ai,
        overreliance=overreliance,
    )

    session.observations.append(observation)

    return observation


def _validate_initial_state(
    scenario_state: ScenarioState,
) -> None:
    if scenario_state.initial_decision is None:
        raise RuntimeError(
            "Initial decision has not been submitted."
        )

    if scenario_state.initial_confidence is None:
        raise RuntimeError(
            "Initial confidence has not been submitted."
        )

    if scenario_state.initial_score is None:
        raise RuntimeError(
            "Initial score has not been calculated."
        )

    if scenario_state.initial_time is None:
        raise RuntimeError(
            "Initial time has not been recorded."
        )
    

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