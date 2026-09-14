import streamlit as st

from database import initialize_database
from pages.dashboard_page import render_dashboard
from pages.experiment_page import render_experiment_page


st.set_page_config(
    page_title="AI Overreliance",
    page_icon="🧠",
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