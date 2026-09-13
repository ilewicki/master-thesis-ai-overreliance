# POC Contract

## Purpose
Validate the technical feasibility of one complete experimental cycle.

## Scope
- Streamlit UI
- SQLite persistence
- 2 simple scenarios
- Static/mock AI recommendation
- Objective scoring
- Basic time measurement

## Experimental flow
`start → scenario → initial decision → initial confidence → AI recommendation + AI confidence → final decision → final confidence → score → persistence`

## Scenarios

### S01 — AI incorrect
Decision objective:
- A: value 80, cost 20 → score 60
- B: value 110, cost 40 → score 70
- Optimal decision: B
- Mock AI recommendation: A
- AI confidence: 95%

Expected overreliance case:
`initial B → AI A → final A → score change = -10 → overreliance = true`

### S02 — AI correct
Decision objective:
- A: value 80, cost 20 → score 60
- B: value 110, cost 40 → score 70
- Optimal decision: B
- Mock AI recommendation: B
- AI confidence: 95%

Expected beneficial case:
`initial A → AI B → final B → score change = +10`

## Scoring
`score = value - cost`

`score_change = final_score - initial_score`

## Observation record
- `id`
- `participant_id`
- `scenario_id`
- `initial_decision`
- `initial_confidence`
- `initial_time`
- `ai_recommendation`
- `ai_confidence`
- `ai_correct`
- `final_decision`
- `final_confidence`
- `final_time`
- `initial_score`
- `final_score`
- `score_change`
- `decision_changed`
- `followed_ai`
- `overreliance`
- `created_at`

## Architecture
For the POC keep the architecture intentionally small:

`Streamlit → experiment state / scoring → SQLite`

Start with a single `src/app.py`. Split modules only when real complexity appears.

## Success criteria
The POC is successful if:
1. A participant can complete the full flow.
2. The application preserves the experiment state between stages.
3. Decision times are recorded.
4. Scores are calculated automatically.
5. A complete observation is persisted in SQLite.
6. The stored observation allows the decision process to be reconstructed.

## Out of scope
- Real LLM/API integration
- Authentication
- REST API
- PostgreSQL
- Production deployment
- Final UI design
- Final research scenarios
