import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.set_page_config(
     page_title="Adanimals NFTs",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
 )

@st.cache
def load_data():
    df = pd.read_pickle('Adanimals_df').T
    monthly_care_arr = np.load('NFT_staking_CARE_arr.npy')
    NFT_monthly_arr= np.load('NFT_monthly_arr.npy')
    return df, monthly_care_arr, NFT_monthly_arr


import datetime

st.title('Adjust $CARE Emissions per Month')
if 'count' not in st.session_state:
    st.session_state.count = 0
    #st.session_state.last_updated = datetime.time(0,0)

def update_counter():
    st.session_state.CARE_increment = st.session_state.CARE_increment

df, monthly_CARE_arr_24_8000, NFT_monthly_arr = load_data()
df_T = df.T



with st.form(key='my_form'):
    default_val_CARE = int(NFT_monthly_arr[0])

    st.number_input('CARE per month for NFT staking', value=default_val_CARE, step=1, key='CARE_increment')
    submit = st.form_submit_button(label='Update', on_click=update_counter)

st.write('Total $CARE tokens emitted per month for NFT staking = ', st.session_state.CARE_increment)



st.title('Adanimals NFTs Simulation Table')

st.write('The table displays simulation results of 8000 randomly generated Adanimals. The $CARE tokens earned per NFT depend on its Total Score. The higher its score, the higher its weight and thus its eligibility for token rewards. Ice, Earth and Air Elements are proposed names for stats instead of strength, agility, intelligence. The total score is the sum of these stats. Luck, bravery and Wits' )



df_T['monthly $CARE'] = (df_T['Weight (%)']*st.session_state.CARE_increment/100).astype(int)


st.dataframe(df_T)


st.subheader('Rarity per NFT')

hist, bin_edges = np.histogram(df_T['rarity'].to_numpy().astype(int), bins=60)

hist_df = pd.DataFrame({
    'Rarity Score of NFT': bin_edges[:-1],
    'Number of NFTs': hist
})

c = alt.Chart(hist_df).mark_circle(size=80).encode(
    x='Rarity Score of NFT',
    y='Number of NFTs',
    color='Rarity Score of NFT',
    tooltip=['Rarity Score of NFT', 'Number of NFTs']
).interactive()

st.altair_chart(c, use_container_width=True)


if False:
    st.subheader('Total Scores per NFT')


    hist, bin_edges = np.histogram(df_T['total score'].to_numpy().astype(int), bins=100)

    hist_df = pd.DataFrame({
        'Total Score of NFT': bin_edges[:-1],
        'Number of NFTs': hist
    })


    '''
    c = alt.Chart(hist_df).mark_bar().encode(
        x='Total Score of NFT',
        y='Number of NFTs'
    )
    #st.bar_chart(hist_values[0])
    st.altair_chart(c, use_container_width=True)
    '''

    c = alt.Chart(hist_df).mark_circle(size=80).encode(
        x='Total Score of NFT',
        y='Number of NFTs',
        color='Total Score of NFT',
        tooltip=['Total Score of NFT', 'Number of NFTs']
    ).interactive()

    st.altair_chart(c, use_container_width=True)


st.subheader('Earnings per NFT')



hist_, bin_edges_ = np.histogram(df_T['monthly $CARE'].to_numpy().astype(int), bins=200)

hist_df2 = pd.DataFrame({
    'Earned $CARE per month': bin_edges_[:-1],
    'Number of NFTs': hist_
})

'''
c2 = alt.Chart(hist_df2).mark_bar().encode(
    x='Earned $CARE per month',
    y='Number of NFTs'
)
#st.bar_chart(hist_values[0])
st.altair_chart(c2, use_container_width=True)
'''


c3 = alt.Chart(hist_df2).mark_circle(size=80).encode(
    x='Earned $CARE per month',
    y='Number of NFTs',
    color='Earned $CARE per month',
    tooltip=['Earned $CARE per month', 'Number of NFTs']
).interactive()

st.altair_chart(c3, use_container_width=True)
