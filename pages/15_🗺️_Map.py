import folium
import streamlit as st
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
st.logo('images/banner-app-Photoroom.png', icon_image='images/image.png')
st.set_page_config(
    page_title="Maps",
    page_icon="📌",
)

def get_coordinates(place_name):
    geolocator = Nominatim(user_agent="streamlit_app")
    location = geolocator.geocode(place_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

st.header("Maps")
place_name = st.text_input("Enter a place name or address:")

map_center = [19.873383111857923, 75.3285979664069]
m = folium.Map(location=map_center, zoom_start=16)
folium.Marker(
    map_center, popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

# If a place name is entered, get the coordinates and add a marker
if place_name:
    lat, lon = get_coordinates(place_name)
    if lat is not None and lon is not None:
        # st.write(f"Coordinates for {place_name}: Latitude {lat}, Longitude {lon}")
        folium.Marker(
            [lat, lon], popup=place_name, tooltip=place_name
        ).add_to(m)
        m.location = [lat, lon]
        m.zoom_start = 12
    else:
        st.error("Could not find the place. Please try another place name or address.")

st_data = st_folium(m, width=625, height=400)
