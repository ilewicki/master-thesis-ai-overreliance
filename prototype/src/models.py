from dataclasses import dataclass
from typing import Literal


Decision = Literal["A", "B"]


@dataclass(frozen=True)
class Option:
    name: Decision
    value: int
    cost: int


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    description: str
    options: dict[Decision, Option]
    optimal_decision: Decision


@dataclass(frozen=True)
class AIRecommendation:
    decision: Decision
    confidence: int


@dataclass
class ExperimentState:
    stage: str = "initial"

    initial_decision: Decision | None = None
    initial_confidence: int | None = None
    initial_score: int | None = None

    ai_recommendation: Decision | None = None
    ai_confidence: int | None = None

    final_decision: Decision | None = None
    final_confidence: int | None = None

    final_score: int | None = None
    score_change: int | None = None

    decision_changed: bool = False
    followed_ai: bool = False
    ai_correct: bool | None = None
    overreliance: bool = False