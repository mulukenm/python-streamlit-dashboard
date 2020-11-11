import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


DATA_URL = (
    "SED.csv"
)

st.title("NCSES Survey of Earned Doctorates (SED)")
st.sidebar.title("Survey of Earned Doctorates (SED)")
st.markdown("This application is a Streamlit dashboard used"
            "to analyze SED data by Race and ethnicity, Sex, S&E Fields,"
            "Broad Fields, detailed Fields, and Years.")
st.sidebar.markdown("This application is a Streamlit dashboard used "
            "to SED data.")

@st.cache(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
data = load_data()

st.sidebar.markdown("### Number of Earned Doctorates by Race and Ethnicity")
select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
race_count = data.groupby(["Race_and_Ethnicity"])['Number'].agg('sum')
race_count = pd.DataFrame({'Race_and_Ethnicity':race_count.index, 'Number':race_count.values})
if not st.sidebar.checkbox("Hide", True):
    st.markdown("### Numbers by Race/Ethnicity")
    if select == 'Bar plot':
        fig = px.bar(race_count, x='Race_and_Ethnicity', y='Number', color='Race_and_Ethnicity', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(race_count, values='Number', names='Race_and_Ethnicity')
        st.plotly_chart(fig)
st.sidebar.markdown("### Number of Earned Doctorates by Sex")
select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
race_count = data.groupby(["Sex"])['Number'].agg('sum')
race_count = pd.DataFrame({'Sex':race_count.index, 'Number':race_count.values})
if not st.sidebar.checkbox("Hide", True):
    st.markdown("### Numbers by Sex")
    if select == 'Bar plot':
        fig = px.bar(race_count, x='Sex', y='Number', color='Sex', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(race_count, values='Number', names='Sex')
        st.plotly_chart(fig)
