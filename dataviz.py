import streamlit as st
from figures import fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10

tabs = ["Multivariate Analysis", "Parental Level of Education in comparison with ethnicity and gender", "Bar Charts", "Test Score Comparison with stats", "Scatter Plot of math and writing scores", "Box Plot of scores", "Heatmap of gender and parental level of education", "Pairplot", "Ethnicity Analysis", "Distplot"]
selected_tab = st.sidebar.selectbox("Select Visualization", tabs)

if selected_tab == "Multivariate Analysis":
    st.write("### Multivariate Analysis")
    st.write("Explanation: This figure shows a multivariate analysis with pie charts representing different categories.")
    fig1()
elif selected_tab == "Parental Level of Education in comparison with ethnicity and gender":
    st.write("### Parental Level of Education in comparison with ethnicity and gender")
    st.write("Explanation: This figure presents a sunburst chart comparing parental level of education with ethnicity and gender.")
    fig2()
elif selected_tab == "Bar Charts":
    st.write("### Bar Charts")
    st.write("Explanation: This figure displays bar charts for different categories, comparing the percentage of male and female students.")
    fig3()
elif selected_tab == "Test Score Comparison with stats":
    st.write("### Test Score Comparison with Stats")
    st.write("Explanation: This figure presents violin plots comparing the distribution of math, reading, and writing scores.")
    fig4()
elif selected_tab == "Scatter Plot of math and writing scores":
    st.write("### Scatter Plot of Math and Writing Scores")
    st.write("Explanation: This figure shows a scatter plot comparing math and writing scores for male and female students.")
    fig5()
elif selected_tab == "Box Plot of scores":
    st.write("### Box Plot of Scores")
    st.write("Explanation: This figure displays box plots representing the distribution of math, reading, and writing scores.")
    fig6()
elif selected_tab == "Heatmap of gender and parental level of education":
    st.write("### Heatmap of Gender and Parental Level of Education")
    st.write("Explanation: This figure presents a heatmap showing the relationship between gender, parental level of education, and math scores.")
    fig7()
elif selected_tab == "Pairplot":
    st.write("### Pairplot")
    st.write("Explanation: This figure shows a pairplot with scatter plots and histograms for different features, colored by gender.")
    fig8()
elif selected_tab == "Ethnicity Analysis":
    st.write("### Ethnicity Analysis")
    st.write("Explanation: This figure displays a bar chart analyzing the mean scores for different ethnicities.")
    fig9()
elif selected_tab == "Distplot":
    st.write("### Distribution Plot of Math Scores by Gender")
    st.write("Explanation: This figure presents a distribution plot comparing math scores between male and female students.")
    fig10()
