import streamlit as st
from multiapp import MultiApp
from apps import home, train
from PIL import  Image

#configuration of the page
st.set_page_config(layout="wide")

app = MultiApp()


display = Image.open('echodot.jpg')
display = np.array(display)
col1, col2 = st.beta_columns(2)
col1.image(display, width = 400)
col2.title("Echo Dot - 4 Geração - Amazon")

app.add_app("Home", home.app)
app.add_app("Base de Teste", train.app)

# The main app
app.run()







