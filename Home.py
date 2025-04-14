import pandas as pd
import pydeck as pdk
import streamlit as st

# store data
df = pd.read_csv('data/iowa.csv')

df_store = (
    df
    .groupby(['store'])
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
df_pop_geo_county

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
            # 2D circles for population
            pdk.Layer(
                "ScatterplotLayer",
                data=df_pop_geo_county,
                get_position='[longitude, latitude]',
                get_radius="radius",
                get_fill_color="[0, 100, 255, 160]",
                pickable=True,
                auto_highlight=True,
            ),
        ],
        tooltip={
            "html": "<b>Store:</b> {store}<br/>"
                    "<b>Gross Profit:</b> ${gross_profit}<br/>"
                    "<b>Bottles Sold:</b> {bottles}",
            "style": {
                "backgroundColor": "rgba(0, 0, 0, 0.8)",
                "color": "white"
            }
        }
    )
)



# # 2. 全米のCounty GeoJSONを取得
# url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
# response = requests.get(url)
# all_counties_geojson = response.json()

# # 3. FIPSが "19" で始まる（Iowa）のみ抽出
# iowa_features = [f for f in all_counties_geojson["features"] if str(f["id"]).startswith("19")]

# iowa_geojson = {
#     "type": "FeatureCollection",
#     "features": iowa_features
# }

# # 4. 地図描画
# fig = px.choropleth_mapbox(
#     df_pop_county,
#     geojson=iowa_geojson,
#     locations="fips",
#     featureidkey="id",  # ← 修正ポイント
#     color="pop_county",
#     color_continuous_scale="Viridis",
#     mapbox_style="carto-positron",
#     zoom=6,
#     center={"lat": 42.0, "lon": -93.5},
#     opacity=0.6,
#     labels={"pop_county": "Population"},
#     title="Population by County in Iowa"
# )

# fig.update_layout(margin={"r":0, "t":40, "l":0, "b":0})
# st.plotly_chart(fig)