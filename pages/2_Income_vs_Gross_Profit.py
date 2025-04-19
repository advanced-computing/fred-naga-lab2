import streamlit as st
from pkg.mapping import population_map, gross_profit_map, income_map
from pkg.plotting import income_histogram_plot, county_population_plot
from pkg.load_data import connect_to_iowa, connect_to_county, connect_to_city, connect_to_spring, connect_to_summer, connect_to_fall, connect_to_winter


# county data
table='solid-dominion-452916-p4.aml_fl_tn.county'
df_county = connect_to_county(table)

# iowa data
table='solid-dominion-452916-p4.aml_fl_tn.iowa'
df_iowa = connect_to_iowa(table)

df_grouped = (
    df_iowa
    .groupby("county", as_index=False)
    .agg({
        "annual_income": "first",   # keeps your existing county‐level income
        "gross_profit":   "sum"     # or "mean" if you’d rather average it
    })
)


st.title("Iowa Population by County")
url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
population_map(df_county, url)

# Average income map and table
st.title("Average Income by County")
income_map(df_county, url)

st.title("Income Distribution")
income_histogram_plot(df_county,30)

# This function is generic
st.subheader("Income vs. Gross Profit by County Stores")
county_population_plot(
    df_iowa,
    x="annual_income",
    y="gross_profit",
    title="Income vs. Gross Profit by Store",
    x_title="Annual Income",
    y_title="Gross Profit",
    trendline="ols"        # optional: adds a regression line
)

st.subheader("Income vs. Gross Profit by County")
county_population_plot(
    df_grouped,
    x="annual_income",
    y="gross_profit",
    title="Income vs. Gross Profit by County",
    x_title="Annual Income",
    y_title="Gross Profit",
    trendline="ols"        # optional: adds a regression line
)