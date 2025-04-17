import streamlit as st

st.set_page_config(page_title="Predictive Analytics for Item-Level Gross Profits in Iowa Liquor Stores",
                   page_icon="🏠")
st.sidebar.header("Fred & Naga")

st.title('Predictive Analytics for Item-Level Gross Profits in Iowa Liquor Stores')

st.header('Problem',divider=True)
st.markdown('''
            This project takes maps of construction applications and prices of sold properties 
            in NYC and combines them to understand the relationsship between the amount of 
            housing construction and the property prices.
            ''')

st.header('Data',divider=True)
st.markdown('''
            **Research Questions**
            - What areas of the city (borough, community district, etc.) are seeing the most construction of housing? How many units can be expected?
            - What kinds of housing are being prioritized by the city? New developments? Renovations? Low density? High density? Luxury? Affordable?
            - Do people apply for construction permits in areas with high property prices?
            **Datasets**
            - [Construction Applications](https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Build-Job-Application-Filings/w9ak-ipjd/about_data)
            - [Prices of Sold Properties](https://data.cityofnewyork.us/City-Government/NYC-Citywide-Annualized-Calendar-Sales-Update/w2pb-icbu/about_data)
            ''')

st.header('Next Steps',divider=True)
st.markdown('''
            **Research Questions**
            - What areas of the city (borough, community district, etc.) are seeing the most construction of housing? How many units can be expected?
            - What kinds of housing are being prioritized by the city? New developments? Renovations? Low density? High density? Luxury? Affordable?
            - Do people apply for construction permits in areas with high property prices?

            **Datasets**
            - [Construction Applications](https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Build-Job-Application-Filings/w9ak-ipjd/about_data)
            - [Prices of Sold Properties](https://data.cityofnewyork.us/City-Government/NYC-Citywide-Annualized-Calendar-Sales-Update/w2pb-icbu/about_data)
            ''')