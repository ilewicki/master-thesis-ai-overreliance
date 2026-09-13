# Experimental Prototype

Technical proof of concept for the master's thesis experiment on AI overreliance and human decision-making.

## Purpose

This prototype is intentionally small and disposable. Its purpose is to test whether the planned experimental flow can be implemented in a web application and whether the resulting observations can be reliably stored for later analysis.

It is **not** the final research application.

## Current scope

- Python
- Streamlit
- SQLite
- 2 simple mock scenarios
- Static AI recommendations
- Objective scoring
- Basic response-time measurement
- Persistence of complete observations

## Experimental flow

```text
scenario
  ↓
initial decision
  ↓
initial confidence
  ↓
AI recommendation + AI confidence
  ↓
final decision
  ↓
final confidence
  ↓
score
  ↓
SQLite
```

## Project structure

```text
prototype/
├── README.md
├── data/
└── src/
    └── app.py
```

The `data/` directory is for local experimental/prototype data and should not be committed to the repository.

## Status

Early technical POC.

The prototype deliberately prioritizes feasibility and learning over code quality, visual design, and production readiness.
