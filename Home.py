# https://advanced-computing-fred-naga-lab2-home-jczcrq.streamlit.app/
import streamlit as st

st.set_page_config(page_title="Predictive Analytics for Item-Level Gross Profits in Iowa Liquor Stores",
                   page_icon="🏠")
st.sidebar.header("Fred & Naga")

st.title('🍺   🍷   🥂   🥃   🍶   🍸   🍹   🍾   🧉   🍻')
st.title('Predictive Analytics for Item-Level Gross Profits in Iowa Liquor Stores')

st.header('🍺 Problem',divider=True)
st.markdown('''
            Choosing where to start a business is always a difficult decision. Rather than relying on 
            evidence-based strategies, entrepreneurs often make decisions based on intuition or 
            outdated heuristics, which can lead to significant resource misallocation. A predictive 
            algorithm that estimates item-level gross profit can support data-driven decision making 
            and help entrepreneurs develop successful business strategies. As a first step, we 
            develop an algorithm to project item-level gross profits in liquor stores, using Iowa 
            liquor sales data.          

            **Research Question**
            - How can we leverage demographic, economic, and liquor sales data to develop a 
            predictive algorithm that helps liquor store owners identify optimal store locations and 
            product assortments?
            - Which geographic or socioeconomic groups are most associated with higher alcohol 
            consumption or preferences for specific types of liquor?

            **How to Use**
            - **Business Perspective.** The algorithm identifies which products sell best in 
            different types of areas (e.g., high-income cities may prefer Item B). This enables liquor 
            owners to tailor product assortments based on local demographics to maximize sales and 
            reduce inventory risk.
            - **Policy Perspective.** The model can help policymakers identify areas with high 
            predicted alcohol consumption, allowing for targeted interventions to mitigate public 
            health risks. It may also help local governments optimize alcohol-related tax revenues.
            ''')

st.header('🍷 Data',divider=True)
st.markdown('''
            **Outcome**
            - [Item-Level Gross Profit in 2024](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data)
            
            **Features**
            - [Age Population in ●]()
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