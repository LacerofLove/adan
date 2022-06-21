"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np

#@st.cache
def load_data():
    df = pd.read_pickle('Adanimals_df').T
    monthly_care_arr = np.load('NFT_staking_CARE_arr.npy')
    NFT_monthly_arr= np.load('NFT_monthly_arr.npy')
    return df, monthly_care_arr, NFT_monthly_arr


import datetime

st.title('Adjust $CARE per Month')
if 'count' not in st.session_state:
    st.session_state.count = 0
    #st.session_state.last_updated = datetime.time(0,0)

def update_counter():
    st.session_state.CARE_increment = st.session_state.CARE_increment
    #st.session_state.month_increment = st.session_state.month_increment

    #st.session_state.last_updated = st.session_state.update_time

df, monthly_CARE_arr_24_8000, NFT_monthly_arr = load_data()
df_T = df.T


default_val_CARE = int(NFT_monthly_arr[0])

with st.form(key='my_form'):
    #st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
    #st.number_input('Month of staking (1-24)', value=0, step=1, key='month_increment')
    st.number_input('CARE per month for NFT staking', value=default_val_CARE, step=1, key='CARE_increment')
    submit = st.form_submit_button(label='Update', on_click=update_counter)

#st.write('Current Month = ', st.session_state.month_increment)
st.write('Total $CARE tokens emitted per month = ', st.session_state.CARE_increment)
#st.write('Last Updated = ', st.session_state.last_updated)


st.title('Adanimals NFT Simulator')




df_T['monthly $CARE'] = (df_T['Weight (%)']*st.session_state.CARE_increment/100).astype(int)


df_T

