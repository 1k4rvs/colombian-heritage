import streamlit as st

# python -m streamlit run .\streamlit_app.py

st.set_page_config(layout="wide")
st.header("""
    :compass: AgroIngenio:
    Soporte Colaborativo para la Protección del Patrimonio Industrial y Agroindustrial Colombiano :material/search_check:
""", divider="orange")

st.sidebar.header(":compass: AgroIngenio")
st.sidebar.markdown("Soporte Colaborativo para la Protección del Patrimonio Industrial y Agroindustrial Colombiano :material/search_check:")

st.image("resources/images/colombia-heritage-logo.jpg")

st.markdown("Investigación y Desarrollo a cargo de Ángela María Santa Quintero y Pedro Ángel Vaquero Diaz :woman_standing::man_standing: ")

import pydeck as pdk
import pandas as pd

data = pd.read_csv('data/demo_path.csv')

# Arc Layer
arc_layer = pdk.Layer(
        "ArcLayer",
        data,
        get_source_position=["start_lon", "start_lat"],
        get_target_position=["end_lon", "end_lat"],
        # get_source_color=[200, 30, 0, 160],
        # get_target_color=[200, 30, 0, 160],
        # auto_highlight=True,
        # width_scale=0.0001,
        # get_width="outbound",
        # width_min_pixels=3,
        # width_max_pixels=30,
        get_source_color=[0, 128, 200],  # Origin: Blue
        get_target_color=[255, 0, 0],    # Target: Red
        auto_highlight=True,
        width_scale=0.5,
        get_width=3,
        width_min_pixels=1,
        width_max_pixels=5,
        great_circle=False,  # Menos curvatura en el arco
        get_height=0.6,  # Altura menor para reducir la curvatura
)

# Initial View State
view_state = pdk.ViewState(
    latitude=5.0661,
    longitude=-75.4847,
    zoom=10,
    pitch=45,
)

map = pdk.Deck(
    layers=[arc_layer],
    initial_view_state=view_state,
    map_style="mapbox://styles/mapbox/light-v9"
)

st.pydeck_chart(map)