import streamlit as st
import pandas as pd
from utils import lottie
from streamlit_lottie import st_lottie

lottie_robot_animation = lottie.load_url("https://assets9.lottiefiles.com/packages/lf20_xaxycw1s.json")


df: pd.DataFrame = st.session_state['df']

if df is None:
    column1, column2, _ = st.columns([1, 1, 1])
    with column2:
        st.header("No data loaded")
        st_lottie(lottie_robot_animation, height=200, quality="high")
        st.write("Go back to home and add a file")
else:
    st.header('Summary Statistics')
    st.write("Here we can take a look at the most important summary statistics for all variables")
    st.write(df.describe())

    st.header('Unique values')
    st.write("Number of distinct values for each variable")
    st.write(df.nunique().rename('n'))
