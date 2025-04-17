import pandas as pd
import streamlit as st
from pkg.mapping import population_map, gross_profit_map
from pkg.load_data import connect_to_population_data, connect_to_profit_data

# load data
table='solid-dominion-452916-p4.aml_fl_tn.iowa_population'
df_pop = connect_to_population_data(table)
table1='solid-dominion-452916-p4.aml_fl_tn.iowa_spring'
df_spring = connect_to_profit_data(table1)
table2='solid-dominion-452916-p4.aml_fl_tn.iowa_summer'
df_summer = connect_to_profit_data(table2)
table3='solid-dominion-452916-p4.aml_fl_tn.iowa_fall'
df_fall = connect_to_profit_data(table3)
table4='solid-dominion-452916-p4.aml_fl_tn.iowa_winter'
df_winter = connect_to_profit_data(table4)

#############################################################

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