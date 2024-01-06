import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import iplot
import streamlit as st
from figures import fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9

data = pd.read_csv("StudentsPerformance.csv")

tabs = ["Multivariate Analysis", "Parental Level of Education in comparison with ethnicity and gender", "Bar Charts", "Test Score Comparison with stats", "Scatter Plot of math and writing scores", "Box Plot of scores", "Heatmap of gender and parental level of education", "Pairplot", "Ethnicity Analysis"]
selected_tab = st.sidebar.selectbox("Select Visualization", tabs)

if selected_tab == "Multivariate Analysis":
    fig1()
elif selected_tab == "Parental Level of Education in comparison with ethnicity and gender":
    fig2()
elif selected_tab == "Bar Charts":
    fig3()
elif selected_tab == "Test Score Comparison with stats":
    fig4()
elif selected_tab == "Scatter Plot of math and writing scores":
    fig5()
elif selected_tab == "Box Plot of scores":
    fig6()
elif selected_tab == "Heatmap of gender and parental level of education":
    fig7()
elif selected_tab == "Pairplot":
    fig8()
elif selected_tab == "Ethnicity Analysis":
    fig9()
