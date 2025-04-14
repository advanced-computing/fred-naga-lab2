import pandas as pd
import plotly.express as px
import streamlit as st
import requests
import json
import pydeck as pdk

# FIPS付きのIowaのcounty populationデータ（仮）
# 例: df_pop = pd.read_csv("iowa_county_population.csv")
df_pop = pd.read_csv("data/pop_geo_county.csv")  # fips列はゼロパディングされた文字列で！

# GeoJSONロード
geojson_url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
response = requests.get(geojson_url)
counties_geojson = response.json()

# タイトル表示
st.title("🗺️ Iowa Population by County")

# Choroplethマップ作成
fig = px.choropleth(
    df_pop,
    geojson=counties_geojson,
    locations="fips",            # 各countyのFIPSコード
    color="pop_county",          # 色付けの基準
    color_continuous_scale="Viridis",
    range_color=(df_pop["pop_county"].min(), df_pop["pop_county"].max()),
    scope="usa",
    labels={"population": "Population"},
    hover_name="county",         # hoverで表示するCounty名（オプション）
)

# Iowa中心にズーム（PlotlyのChoroplethはzoom設定不可 → Iowaに限定したデータが必要）
fig.update_geos(fitbounds="locations", visible=False)

# レイアウト調整
fig.update_layout(
    title_text="Iowa County Population Map",
    margin={"r": 0, "t": 50, "l": 0, "b": 0},
    height=600
)

# 表示
st.plotly_chart(fig, use_container_width=True)

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
