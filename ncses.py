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

data = load_data()

st.sidebar.markdown("### Number of Earned Doctorates by Race and Ethnicity")
select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
sentiment_count = data['Number].groupby("Race_and_Ethnicity")
sentiment_count = pd.DataFrame({'Race_and_Ethnicity':Race_and_Ethnicity.index, 'Values':Race_and_Ethnicity.values})
if not st.sidebar.checkbox("Hide", True):
    st.markdown("### Number of tweets by sentiment")
    if select == 'Bar plot':
        fig = px.bar(sentiment_count, x='Sentiment', y='Tweets', color='Tweets', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment_count, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)
