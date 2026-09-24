from models.domain import Decision, Scenario


def calculate_score(
    scenario: Scenario,
    decision: Decision,
) -> int:
    option = scenario.options[decision]

    return option.value - option.cost


def calculate_decision_change(
    initial_decision: Decision,
    final_decision: Decision,
) -> bool:
    return initial_decision != final_decision


def calculate_followed_ai(
    final_decision: Decision,
    ai_decision: Decision,
) -> bool:
    return final_decision == ai_decision


def calculate_overreliance(
    initial_decision: Decision,
    final_decision: Decision,
    ai_decision: Decision,
    optimal_decision: Decision,
) -> bool:
    initial_correct = initial_decision == optimal_decision
    ai_wrong = ai_decision != optimal_decision
    followed_ai = final_decision == ai_decision

    return initial_correct and ai_wrong and followed_ai