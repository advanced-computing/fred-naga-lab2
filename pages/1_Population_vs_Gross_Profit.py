import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
import numpy as np
from pkg.mapping import population_map, gross_profit_map
from pkg.load_data import connect_to_population_data, connect_to_spring, connect_to_summer, connect_to_fall, connect_to_winter

# population data
table='solid-dominion-452916-p4.aml_fl_tn.iowa_population'
df_pop = connect_to_population_data(table)

# gross profit data
table2='solid-dominion-452916-p4.aml_fl_tn.iowa_season'
df_spring = connect_to_spring(table2)
df_summer = connect_to_summer(table2)
df_fall = connect_to_fall(table2)
df_winter = connect_to_winter(table2)

tab1, tab2 = st.tabs(["Map", "Plot"])

#############################################################

with tab1:

    st.title("Iowa Population by County")
    url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
    population_map(df_pop, url)

    st.title("Item-Level Gross Profit by Store")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Spring")
        gross_profit_map(df_spring)
        st.write("Fall")
        gross_profit_map(df_fall)

    with col2:
        st.write("Summer")
        gross_profit_map(df_summer)
        st.write("Winter")
        gross_profit_map(df_winter)

with tab2:
    st.title("Gross Profit by Store vs City Population")
    fig = px.scatter(
        df_spring,
        x="pop_city",
        y="gross_profit",
        color='county',        
        hover_data={"city": True, "county": True, "pop_city": False, "gross_profit": False},
        labels={"pop_city": "city population", 
                "gross_profit": "item-level gross profit by store"},
    )
    fig.update_layout(showlegend=False, height=500)
    st.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(
    df_spring,
    x="pop_city",
    y="gross_profit",
    trendline="ols",  
    hover_data={"city": True, "county": True, "pop_city": False, "gross_profit": False},
    labels={"pop_city": "city population", 
            "gross_profit": "item-level gross profit by store"},
    )
    fig.update_layout(showlegend=False, height=500)
    st.plotly_chart(fig, use_container_width=True)