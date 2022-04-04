import streamlit as st
from multiapp import MultiApp
from apps import home, home2

#configuration of the page
st.set_page_config(layout="wide")

app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Base de Teste", home2.app)

# The main app
app.run()







