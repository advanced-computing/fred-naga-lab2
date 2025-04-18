import streamlit as st
import plotly.express as px

def county_population_plot(df, x, y, 
                           color=None, trendline=None,
                           title="", x_title="", y_title=""):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color if color else None,     
        hover_data={"county": True, x: False, y: False},
        trendline=trendline if trendline else None, 
        labels={title: title, x: x_title, y: y_title},
    )
    fig.update_layout(showlegend=False, height=500)
    st.plotly_chart(fig, use_container_width=True)

def city_population_plot(df, x, y, color=None, trendline=None,
                         title="", x_title="", y_title=""):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color if color else None,     
        hover_data={"city": True, x: False, y: False},
        trendline=trendline if trendline else None,
        labels={title: title, x: x_title, y: y_title},
    )
    fig.update_layout(showlegend=False, height=500)
    st.plotly_chart(fig, use_container_width=True)
