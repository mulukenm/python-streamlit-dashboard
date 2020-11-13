import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


DATA_URL = (
    "SED_new_11122020ed.csv"
)

st.title("NCSES Survey of Earned Doctorates (SED)")
st.sidebar.title("Survey of Earned Doctorates (SED)")
st.markdown("This application is a Python Streamlit dashboard to analyze "
            "SED data by Race and ethnicity, Sex, S&E Fields, "
            "Broad Fields, detailed Fields, and Years of Earned Doctorates.")
st.sidebar.markdown("Survey of Earned Doctorates Recipientsby different attributes.")

@st.cache(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
data = load_data()

st.sidebar.markdown("### Earned Doctorate Recipients")
select1 = st.sidebar.selectbox('Visualization type', ['Sunburst'])
if not st.sidebar.checkbox("Close", True):
    fig_1 = px.sunburst(data, path=['S&E_Fields','Broad_Fields', 'Detailed_Fields', 'Year', 'Sex'], values='Number', height = 800, width = 800)
    #fig1.update_layout(
        # title={
        #     'text': "Field of Study of Doctorate Recipients by Sex and Selected Years",
        #     'y':0.94,
        #     'x':0.5,
        #     'xanchor': 'center',
        #     'yanchor': 'top'})
    st.plotly_chart(fig_1)

st.sidebar.markdown("### Earned Doctorate Recipients by Sex and Race/Ethnicity")
select2 = st.sidebar.selectbox('Visualization type', ['Barplot'], key='2')
if not st.sidebar.checkbox("Hide", True, key='2'):
    fig_1 = px.bar(data, x="Race_and_Ethnicity", y="Number", color="Sex", barmode="group")
    st.plotly_chart(fig_2)


st.sidebar.markdown("### Earned Doctorate Recipients by Race and Ethnicity")
select3 = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='3')
race_count = data.groupby(["Race_and_Ethnicity"])['Number'].agg('sum')
race_count = pd.DataFrame({'Race_and_Ethnicity':race_count.index, 'Number':race_count.values})
if not st.sidebar.checkbox("Hide", True, key='3'):
    st.markdown("### Earned Doctorate Recipients by Race/Ethnicity")
    if select == 'Bar plot':
        fig_3 = px.bar(race_count, x='Race_and_Ethnicity', y='Number', color='Number', height=500)
        st.plotly_chart(fig_3)
    else:
        fig_3 = px.pie(race_count, values='Number', names='Race_and_Ethnicity')
        st.plotly_chart(fig_3)

st.sidebar.markdown("### Earned Doctorate Recipients by Sex")
select4 = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='4')
sex_count = data.groupby(["Sex"])['Number'].agg('sum')
sex_count = pd.DataFrame({'Sex':sex_count.index, 'Number':sex_count.values})
if not st.sidebar.checkbox("Hide", True, key='4'):
    st.markdown("### Earned Doctorate Recipients by Sex")
    if select == 'Bar plot':
        fig_4 = px.bar(sex_count, x='Sex', y='Number', color='Number', height=500)
        st.plotly_chart(fig_4)
    else:
        fig_4 = px.pie(sex_count, values='Number', names='Sex')
        st.plotly_chart(fig_4)
