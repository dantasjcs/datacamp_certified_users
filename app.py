import streamlit as st
from streamlit_plotly_mapbox_events import plotly_mapbox_events
import plotly.express as px
import pandas as pd

st.set_page_config(layout='wide', page_title='Datacamp certified users')

@st.cache_resource
def load_data(path_to):
    data = pd.read_csv(path_to)
    return data

data = load_data('datacamp_users.csv')


col1, col2 = st.columns((2, 1))
with col1:
    mapbox = px.scatter_mapbox(data, lat="lat", lon="lon", zoom=1, height=600, width=1200, mapbox_style="carto-positron", hover_name='Full Location', hover_data={'lat': False, 'lon': False})
    mapbox.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    plot_name_holder_clicked = st.empty()
    mapbox_events = plotly_mapbox_events(mapbox, click_event=True)

if len(mapbox_events[0])>0:
    lat = mapbox_events[0][0]['lat']
    location = data[data['lat']==lat]['Full Location'].iloc[0]
    first_name = data[data['lat']==lat]['First Name']
    last_name = data[data['lat']==lat]['Last Name']
    with col2:
        st.subheader('Users from the DataCamp Certification Community in:')   
        st.markdown(f"##### {location}")

        for i in range(len(first_name)):
            name = f"{first_name.iloc[i]} {last_name.iloc[i]}"
            st.write(name)
