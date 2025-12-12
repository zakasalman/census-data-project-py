import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('example.csv')
st.set_page_config(layout = 'wide')

list_of_states  = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India ka Census')

state_select = st.sidebar.selectbox('Select State',list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter' , sorted(df.columns[5:]))
secondry = st.sidebar.selectbox('Select Secondry Parameter' , sorted(df.columns))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size Represents Primary Parameter')
    st.text(' Colour represents Secondry Parameter')
    if state_select == 'Overall India':
        #         plot for india
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size = primary ,
                                color = secondry,size_max= 35 ,width = 1200 , height= 700 ,
                                zoom=3, mapbox_style='carto-positron',hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
#         plot for state wise data
        state_df = df[df['State'] == state_select]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary,
                        color=secondry, size_max=35, width=1200, height=700,
                        zoom=3, mapbox_style='carto-positron',hover_name='District')
        st.plotly_chart(fig, use_container_width=True)

