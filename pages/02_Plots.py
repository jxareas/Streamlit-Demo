import streamlit as st
import pandas as pd
import plotly_express as px

st.set_page_config(layout='wide')

df: pd.DataFrame = st.session_state['df']

col1, col2 = st.columns(2)

x_axis_value = col1.selectbox('Select the x-axis variable:', options=df.columns)
y_axis_value = col2.selectbox('Select the y-axis variable', options=df.columns)

plot = px.scatter(df, x=x_axis_value, y=y_axis_value)
st.plotly_chart(plot, use_container_width=True)
