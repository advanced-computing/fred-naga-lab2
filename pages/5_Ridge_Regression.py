# https://advanced-computing-fred-naga-lab2-home-jczcrq.streamlit.app/
import streamlit as st
import json

st.title('Ridge Regression')

st.header('🍻 Training - 70% of Data',divider=True)
st.markdown('**Beta Hat of 4,529 features**')

with open('json/beta_hat_1_labeled.json', 'r') as f:
    beta_hat = json.load(f)

st.json(beta_hat)

st.header('🧉 Validation - 15% of Data',divider=True)


st.header('🍾 Testing - 15% of Data',divider=True)
