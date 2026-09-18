from dataclasses import dataclass, field
from enum import Enum


class Decision(Enum):
    A = "A"
    B = "B"


class ExperimentStage(Enum):
    INITIAL = "initial"
    AI = "ai"
    COMPLETE = "complete"


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
class ScenarioState:
    initial_time: float | None = None
    final_time: float | None = None 

    initial_decision: Decision | None = None
    initial_confidence: int | None = None
    initial_score: int | None = None

    final_decision: Decision | None = None
    final_confidence: int | None = None
    final_score: int | None = None

    score_change: int | None = None
    decision_changed: bool = False
    followed_ai: bool = False
    ai_correct: bool | None = None
    overreliance: bool = False


@dataclass(frozen=True)
class Observation:
    participant_id: str
    scenario_id: str

    initial_decision: Decision
    initial_confidence: int
    initial_score: int
    
    initial_time: float

    ai_recommendation: Decision
    ai_confidence: int
    ai_correct: bool

    final_decision: Decision
    final_confidence: int
    final_score: int

    score_change: int
    decision_changed: bool
    followed_ai: bool
    overreliance: bool

    final_time: float


@dataclass
class ExperimentSession:
    participant_id: str
    current_scenario_index: int = 0
    stage: ExperimentStage = ExperimentStage.INITIAL
    current_scenario: ScenarioState = field(
        default_factory=ScenarioState
    )
    observations: list[Observation] = field(default_factory=list)