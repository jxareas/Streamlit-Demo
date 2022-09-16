import streamlit as st
import pandas as pd

st.title("Streamlit Demo")

st.markdown("This current app is meant to demonstrate how to create a "
            "**simple navigation using Streamlit.**")

csv_file = st.file_uploader("Upload your .csv file here!")

if 'df' not in st.session_state:
    st.session_state.df = None

if csv_file is not None:
    df = pd.read_csv(csv_file)
    st.session_state['df'] = df

if st.session_state['df'] is not None:
    st.success("Data Uploaded Successfully")
    st.title("Preview: ")
    df = st.session_state['df']
    st.write(df.head())
else:
    st.error("No Data Uploaded")
