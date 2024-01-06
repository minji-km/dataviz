import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import iplot
import streamlit as st

data = pd.read_csv("StudentsPerformance.csv")

def create_pie_chart(fig, labels, title, row, col, colors):
    fig.add_trace(
        go.Pie(
            labels=labels,
            values=None,
            title=title,
            titlefont={'color': 'black', 'size': 24},
        ),
        row=row, col=col
    )
    fig.update_traces(
        hoverinfo='label+value',
        textinfo='label+percent',
        textfont_size=10,
        marker=dict(
            colors=colors,
            line=dict(color='#000000', width=2)
        )
    )

def fig1():
    fig = make_subplots(rows=2, cols=3,
                        specs=[[{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}],
                            [{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}]])

    colors = px.colors.sequential.Viridis
    create_pie_chart(fig, data['gender'], 'Gender', 1, 1, colors)
    create_pie_chart(fig, data['race/ethnicity'], 'Race', 1, 2, colors)
    create_pie_chart(fig, data['parental level of education'], 'ParentEduc.', 1, 3, colors)
    create_pie_chart(fig, data['lunch'], 'Lunch', 2, 1, colors)
    create_pie_chart(fig, data['test preparation course'], 'TestPrep.', 2, 2, colors)

    fig.layout.update(title="<b>Multivariate analysis<b>", showlegend=False, height=700, width=1100,
                    template=None, titlefont={'color': 'black', 'size': 24})
    fig.show()
    st.plotly_chart(fig, use_container_width=True)

def fig2():
    fig = px.sunburst(data, path=['race/ethnicity', 'gender', 'parental level of education'])
    fig.update_layout(title_text="<b>Parental level of education in comparison with race and genre<b>", 
                    titlefont={'size': 28},
                    width=800, 
                    height=700,
                    )
    fig.show()
    st.plotly_chart(fig, use_container_width=True)

def fig3():
    colors = px.colors.sequential.Viridis
    plots = []
    categories = {
        'parental level of education': ["some high school", "high school", "associate's degree", "some college", "bachelor's degree", "master's degree"],
        'race/ethnicity': ["group A", "group B", "group C", "group D", "group E"],
        'lunch': ["standard", "free/reduced"],
        'test preparation course': ["none", "completed"]
    }

    for feature, cats in categories.items():
        source = data.groupby([feature, 'gender']).size().unstack().reset_index()
        source = source.rename(columns={'male': 'Male', 'female': 'Female'})
        source = source.fillna(0)

        fig = px.bar(source, x=feature, y=['Male', 'Female'], barmode='group', color_discrete_sequence=colors,
                    labels={'value': '% of Students', 'variable': 'Gender'},
                    title=f"{feature.capitalize()}",
                    height=400)

        fig.update_layout(legend=dict(orientation="v", y=1, yanchor="top", x=1.0, xanchor="right"))

        plots.append(fig)

    for plot in plots:
        plot.show()
        st.plotly_chart(fig, use_container_width=True)

def fig4():
    fig = go.Figure()
    fig.add_trace(go.Violin(x=data['math score'], line_color='salmon', name='Math'))
    fig.add_trace(go.Violin(x=data['reading score'], line_color='gold', name= 'Reading'))
    fig.add_trace(go.Violin(x=data['writing score'], line_color='lightseagreen', name='Writing'))

    fig.update_traces(orientation='h', side='positive', width=3, points=False, meanline_visible=True)
    fig.update_layout(xaxis_showgrid=False, xaxis_zeroline=False)

    fig.update_layout(title='<b> Test Score Comparison with stats (median quartile min max) <b>',
                    titlefont={'size': 24,
                                'family':'San Serif',
                                'color': 'black'
                                },
                    xaxis_title='Test scores',
                    width=750,
                    showlegend=False,
                    paper_bgcolor="lightgray",
                    plot_bgcolor='lightgray',             
    )
    fig.show()
    st.plotly_chart(fig, use_container_width=True)

def create_scatter_plot(data, gender_colors=None):
    if gender_colors is None:
        gender_colors = {'male': 'cornflowerblue', 'female': 'darkorange'}

    traces = []
    for gender, color in gender_colors.items():
        trace = go.Scatter(
            x=data[data['gender'] == gender]['math score'],
            showlegend=True,
            text=gender.capitalize(),
            y=data[data['gender'] == gender]['writing score'],
            name=gender.capitalize(),
            mode='markers',
            marker=dict(color=color, size=9, opacity=0.55)
        )
        traces.append(trace)

    layout = go.Layout(
        title='Math Score & Writing Score',
        xaxis=dict(title='Math Score'),
        yaxis=dict(title='Writing Score'),
        width=700,
        height=450,
        template='simple_white'
    )

    fig = make_subplots(rows=1, cols=1, subplot_titles=['Math and writing Score'], specs=[[{'type': 'scatter'}]])
    for trace in traces:
        fig.add_trace(trace)

    fig.update_layout(layout)
    return fig

def fig5():
    gender_colors = {'male': 'purple', 'female': 'green'}
    scatter_plot = create_scatter_plot(data, gender_colors)
    iplot(scatter_plot)
    st.plotly_chart(scatter_plot, use_container_width=True)

def fig6():
    data_bp = [go.Box(x =data['reading score'],
                showlegend=False,
                name = 'Reading Score'),
            go.Box(x=data['writing score'],
                showlegend=False,
                name = 'Writing Score'),
            go.Box(x=data['math score'],
                showlegend=False,
                name = 'Math Score')]

    layout_bp = go.Layout(title={'text': "Bopxplot of math, writing and reading scores",
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'},
                    width = 700,
                    height=450)

    fig = go.Figure(data = data_bp, layout = layout_bp)
    iplot(fig)
    st.plotly_chart(fig, use_container_width=True)

def fig7():
    data_heatmap = [go.Heatmap(x=data['gender'],
                    y= data['parental level of education'],
                    z = data['math score'].values.tolist(),
                    colorscale = 'Magma')]

    layout_heatmap = go.Layout(title={'text': "Gender & Level of Education",
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'},
                    xaxis = dict(title='Gender'),
                    yaxis =dict(title='Level of Education'),
                    width=600,
                    height=450,
                    template='plotly_white')

    fig = go.Figure(data = data_heatmap, layout = layout_heatmap)
    iplot(fig)
    st.plotly_chart(fig, use_container_width=True)

def fig8():
    pairplot = sns.pairplot(data,hue = 'gender')
    plt.show()
    st.pyplot(pairplot.fig)

def fig9():
    barplot = px.bar(data_frame=data.groupby('race/ethnicity').agg({'math score' : 'mean','reading score' : 'mean','writing score' : 'mean'}), barmode='group',
       title = "<b>Ethnicity Analysis of scores</b>")
    st.plotly_chart(barplot, use_container_width=True)