import streamlit as st
from multiapp import MultiApp
from apps import home, train

#configuration of the page
st.set_page_config(layout="wide")

app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Base de Teste", train.app)

# The main app
app.run()







