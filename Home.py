# https://advanced-computing-fred-naga-lab2-home-pcbqhv.streamlit.app/
import streamlit as st

st.set_page_config(page_title="Predictive Analytics for Item-Level Gross Profits in Iowa Liquor Stores",
                   page_icon="🏠")
st.sidebar.header("Fred & Naga")

st.title('🍺   🍷   🥂   🥃   🍶   🍸   🍹   🍾   🧉   🍻')
st.title('Predictive Analytics for Item-Level Gross Profits in Iowa Liquor Stores')

st.header('🍺 Problem',divider=True)
st.markdown('''
            **Research Question**
            - What kind of algorithm should we develop to help liquor owners decide on
            the location of a liquor store and assortment of liquors?

            **How to Use**
            - The model shows which products sell best in different types of cities (e.g., high-income areas prefer Item B). Thus, managers can tailor the product lineup for each store based on local demographics to maximize sales.
            - The model identifies peak months for each product (e.g., Item A peaks in December, Item C in June), so managers can schedule promotions and adjust inventory levels accordingly to capture seasonal demand. 
            ''')

st.header('🍷 Data',divider=True)
st.markdown('''
            **Outcome**
            - [Item-Level Gross Profit in 2024](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data)
            
            **Features**
            - [Age Population]()
            - [Annual Income by County in 2022](https://data.iowa.gov/Economic-Statistics/Annual-Personal-Income-for-State-of-Iowa-by-County/st2k-2ti2/about_data)
            - [Fuel Sales by County in 2024](https://data.iowa.gov/Sales-Distribution/Iowa-Motor-Fuel-Sales-by-County-and-Year/hbwp-wys3/about_data)
            - [Excessive Drinking Percentage by County in 2022](https://www.countyhealthrankings.org/health-data/community-conditions/health-infrastructure/health-promotion-and-harm-reduction/excessive-drinking?state=19&tab=1&year=2025) (Used as an interaction term with store type)
            - [Store Types](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data)
            - [Liquor Types](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data)
            ''')

st.header('🍶 Strategy',divider=True)
st.markdown('''
            - Project item-level gross profits based on the features that each store has.
            - Train the data with Ridge Regression, test it and ...
            ''')

st.header('🍹 Next Steps',divider=True)
st.markdown('''
            **???**
            - ...
            - ...
            - ...
            ''')