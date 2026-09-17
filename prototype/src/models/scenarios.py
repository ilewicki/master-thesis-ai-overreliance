from models.models import (
    AIRecommendation,
    Decision,
    Option,
    Scenario,
)


SCENARIO_01 = Scenario(
    scenario_id="S01",
    description=(
        "Masz do wyboru dwie opcje. "
        "Wybierz tę, którą uważasz za lepszą."
    ),
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


AI_RECOMMENDATION_01 = AIRecommendation(
    decision=Decision.A,
    confidence=95,
)


SCENARIO_02 = Scenario(
    scenario_id="S02",
    description=(
        "Masz do wyboru dwie opcje. "
        "Wybierz tę, którą uważasz za lepszą."
    ),
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


AI_RECOMMENDATION_02 = AIRecommendation(
    decision=Decision.B,
    confidence=95,
)