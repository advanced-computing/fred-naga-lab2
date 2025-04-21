import streamlit as st
from pkg.mapping import population_map, income_map
from pkg.plotting import income_histogram_plot, county_population_plot
from pkg.load_data import connect_to_iowa, connect_to_county


# county data
table='solid-dominion-452916-p4.aml_fl_tn.county'
df_county = connect_to_county(table)
df_county = df_county.groupby('county').first().reset_index()

st.title("Iowa Population by County")
url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
population_map(df_county, url)

# Average income map and table
st.title("Average Income by County")
income_map(df_county, url)

st.title("Income Distribution")
income_histogram_plot(df_county,30)

# This function is generic
st.subheader("Income vs. Gross Profit by County")
county_population_plot(
    df_county,
    x="annual_income",
    y="gross_profit",
    color="county",
    title="Income vs. Gross Profit by County",
    x_title="Annual Income",
    y_title="Gross Profit",
    trendline="ols"        # optional: adds a regression line
)

st.subheader("Income vs. Gross Profit with Trendline")
county_population_plot(
    df_county,
    x="annual_income",
    y="gross_profit",
    title="Income vs. Gross Profit (w/ Trendline)",
    x_title="Annual Income",
    y_title="Gross Profit",
    trendline="ols"        # optional: adds a regression line
)