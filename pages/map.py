import pandas as pd
import plotly.express as px
import streamlit as st
import requests
import json
import pydeck as pdk

st.title("Iowa Population by County")

df_pop = pd.read_csv("data/pop_geo_county.csv") 

url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
response = requests.get(url)
shapes = response.json()

# mapping
fig = px.choropleth(
    df_pop,
    geojson=shapes,
    locations="fips",
    color="pop_county",
    color_continuous_scale="Viridis",
    range_color=(df_pop["pop_county"].min(), df_pop["pop_county"].max()),
    scope="usa",
    labels={"pop_county": "Population"},
    hover_name="county", 
)

# Iowa中心にズーム（PlotlyのChoroplethはzoom設定不可 → Iowaに限定したデータが必要）
fig.update_geos(fitbounds="locations", visible=False)

# レイアウト調整
fig.update_layout(
    # title_text="Iowa Population by County",
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    height=400,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)

fig.update_traces(
    colorbar=dict(
        len=1,
        y=0.5, 
        thickness=10
    )
)

st.plotly_chart(fig, use_container_width=True)

st.title("Item-Level Gross Profit by Store")

# store data
df = pd.read_csv('data/iowa.csv')

df_store = (
    df
    .groupby(['store', 'city','county'])
    .agg({
        'bottles': 'sum',
        'gross_profit': 'sum',
        'latitude': 'first',
        'longitude': 'first',
    })
    .reset_index()
)
df_store = df_store.dropna(subset=["gross_profit", "latitude", "longitude"])

# population data
df_pop_geo_county = pd.read_csv('data/pop_geo_county.csv')
df_pop_geo_county["radius"] = df_pop_geo_county["pop_county"] / 20

# map
st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=df_store['latitude'].mean(),
            longitude=df_store['longitude'].mean(),
            zoom=6,
            pitch=45,
        ),
        layers=[
            # 3D columns for store gross profit
            pdk.Layer(
                "ColumnLayer",
                data=df_store,
                get_position='[longitude, latitude]',
                get_elevation="gross_profit",
                elevation_scale=0.3,
                radius=1000,
                get_fill_color="[255, 140, 0, 200]",
                pickable=True,
                auto_highlight=True,
            ),
        ],
        tooltip={
            "html": "<b>Store:</b> {store}<br/>"
                    "<b>County:</b> {county}<br/>"
                    "<b>City:</b> {city}<br/>"
                    "<b>Gross Profit:</b> ${gross_profit}<br/>",
            "style": {
                "backgroundColor": "rgba(0, 0, 0, 0.8)",
                "color": "white"
            }
        }
    )
)
