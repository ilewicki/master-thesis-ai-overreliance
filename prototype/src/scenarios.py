from models import AIRecommendation, Option, Scenario


SCENARIO_01 = Scenario(
    scenario_id="S01",
    description=(
        "Masz do wyboru dwie opcje. "
        "Wybierz tę, którą uważasz za lepszą."
    ),
    options={
        "A": Option(
            name="A",
            value=80,
            cost=20,
        ),
        "B": Option(
            name="B",
            value=110,
            cost=40,
        ),
    },
    optimal_decision="B",
)


AI_RECOMMENDATION_01 = AIRecommendation(
    decision="A",
    confidence=95,
)

SCENARIO_02 = Scenario(
    scenario_id="S02",
    description=(
        "Masz do wyboru dwie opcje. "
        "Wybierz tę, którą uważasz za lepszą."
    ),
    options={
        "A": Option(name="A", value=80, cost=20),
        "B": Option(name="B", value=110, cost=40),
    },
    optimal_decision="B",
)


AI_RECOMMENDATION_02 = AIRecommendation(
    decision="B",
    confidence=95,
)