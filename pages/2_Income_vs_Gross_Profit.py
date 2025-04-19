import streamlit as st
from pkg.mapping import population_map, gross_profit_map, income_map, median_income_map
from pkg.plotting import income_histogram_plot
from pkg.load_data import connect_to_iowa, connect_to_county, connect_to_city, connect_to_spring, connect_to_summer, connect_to_fall, connect_to_winter


# county data
table='solid-dominion-452916-p4.aml_fl_tn.county'
df_county = connect_to_county(table)


st.title("Iowa Population by County")
url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
population_map(df_county, url)

# Average income map and table
st.title("Average Income by County")
income_map(df_county, url)

st.title("Income Distribution")
income_histogram_plot(df_county,30)
