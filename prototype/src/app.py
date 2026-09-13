import streamlit as st

# ----------------------------------------------------------------------
SCENARIO = {
    "A": {
        "value": 80,
        "cost": 20,
    },
    "B": {
        "value": 110,
        "cost": 40,
    },
}

AI_RECOMMENDATION = "A"
AI_CONFIDENCE = 95

# Declared Loss Function
def calculate_score(option):
    return SCENARIO[option]["value"] - SCENARIO[option]["cost"]

def calculate_decision_change(initial_decision, final_decision):
    return initial_decision != final_decision

# ----------------------------------------------------------------------
st.title("AI Overreliance — POC")

st.header("Scenariusz 01")

st.write(
    "Masz do wyboru dwie opcje. "
    "Wybierz tę, którą uważasz za lepszą."
)

option = st.radio(
    "Twój wybór:",
    ["A", "B"],
)

confidence = st.slider(
    "Jak pewny jesteś swojej decyzji?",
    min_value=0,
    max_value=100,
    value=50,
)

if st.button("Potwierdź decyzję"):
    st.session_state["initial_decision"] = option
    st.session_state["initial_confidence"] = confidence
    st.session_state["initial_score"] = calculate_score(option)
    st.session_state["initial_decision_submitted"] = True

if st.session_state.get("initial_decision_submitted", False):

    st.header("Rekomendacja AI")

    st.write(
        f"AI rekomenduje: **{AI_RECOMMENDATION}**"
    )

    st.write(
        f"Pewność AI: **{AI_CONFIDENCE}%**"
    )

    final_decision = st.radio(
        "Jaka jest Twoja ostateczna decyzja?",
        ["A", "B"],
        key="final_decision_input",
    )

    final_confidence = st.slider(
        "Jak pewny jesteś swojej ostatecznej decyzji?",
        min_value=0,
        max_value=100,
        value=50,
        key="final_confidence_input",
    )

    if st.button("Potwierdź ostateczną decyzję"):
        st.session_state["final_decision"] = final_decision
        st.session_state["final_confidence"] = final_confidence

