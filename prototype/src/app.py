import uuid

import streamlit as st

from persistence.database import initialize_database
from models.domain import ExperimentSession
from pages.dashboard_page import render_dashboard
from pages.experiment_page import render_experiment_page


st.set_page_config(
    page_title="AI Overreliance",
    page_icon="🧠",
)

if "participant_id" not in st.session_state:
    st.session_state.participant_id = str(uuid.uuid4())


if "experiment_session" not in st.session_state:
    st.session_state.experiment_session = ExperimentSession(
        participant_id=st.session_state.participant_id
    )

initialize_database()

pages = [
    st.Page(
        render_experiment_page,
        title="Eksperyment",
        icon="🧪",
    ),
    st.Page(
        render_dashboard,
        title="Dashboard",
        icon="📊",
    ),
]

page = st.navigation(pages)

page.run()