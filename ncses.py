import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


DATA_URL = (
    "SEDed.csv"
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

st.sidebar.markdown("### Number of Earned Doctorates")
sex = st.sidebar.selectbox('Visualization type', ['Sunburst'])
if not st.sidebar.checkbox("Close", True):
    fig1 = px.sunburst(data, path=['S&E_Fields','Broad_Fields', 'Detailed_Fields', 'Year', 'Sex'], values='Number', height = 800, width = 800)
    #fig1.update_layout(
        # title={
        #     'text': "Field of Study of Doctrate Recipients by Sex and Selected Years",
        #     'y':0.94,
        #     'x':0.5,
        #     'xanchor': 'center',
        #     'yanchor': 'top'})
    st.plotly_chart(fig1)

st.sidebar.markdown("### Number of Earned Doctorates by Race and Ethnicity")
select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='2')
race_count = data.groupby(["Race_and_Ethnicity"])['Number'].agg('sum')
race_count = pd.DataFrame({'Race_and_Ethnicity':race_count.index, 'Number':race_count.values})
if not st.sidebar.checkbox("Hide", True, key='2'):
    st.markdown("### Numbers by Race/Ethnicity")
    if select == 'Bar plot':
        fig2 = px.bar(race_count, x='Race_and_Ethnicity', y='Number', color='Number', height=500)
        st.plotly_chart(fig2)
    else:
        fig2 = px.pie(race_count, values='Number', names='Race_and_Ethnicity')
        st.plotly_chart(fig2)

st.sidebar.markdown("### Number of Earned Doctorates by Sex")
sex = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='3')
sex_count = data.groupby(["Sex"])['Number'].agg('sum')
sex_count = pd.DataFrame({'Sex':sex_count.index, 'Number':sex_count.values})
if not st.sidebar.checkbox("Hide", True, key='3'):
    st.markdown("### Numbers by Sex")
    if select == 'Bar plot':
        fig3 = px.bar(sex_count, x='Sex', y='Number', color='Number', height=500)
        st.plotly_chart(fig3)
    elif:
        fig3 = px.pie(sex_count, values='Number', names='Sex')
        st.plotly_chart(fig3)
