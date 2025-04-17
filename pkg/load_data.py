import streamlit as st # added
from google.oauth2 import service_account #added
import pandas_gbq # added

@st.cache_resource
def connect_to_population_data(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT fips, 
            county,
            pop_county,
    FROM `{table}`
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)

@st.cache_resource
def connect_to_profit_data(table):

    # create API client
    creds = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(creds)

    sql = f"""
    SELECT latitude, 
            longitude,
            gross_profit,
    FROM `{table}`
    """

    return pandas_gbq.read_gbq(sql, credentials=credentials)