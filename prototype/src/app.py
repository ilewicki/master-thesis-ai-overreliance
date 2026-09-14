import streamlit as st

from database import initialize_database
from experiment import render_experiment


st.set_page_config(
    page_title="AI Overreliance",
    page_icon="🧠",
)

initialize_database()

render_experiment()