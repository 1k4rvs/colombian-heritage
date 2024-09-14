# C:\Program Files\Python312\python -m streamlit run .\ColombianIndustrialHeritageRoutesWebApp.py

# https://www.openstreetmap.org/way/1172223300#map=12/9.0540/-74.1237

import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
from folium import IFrame
import json

routes = {
    'Ruta Cafetera: Manizales - Buenaventura (PAC-Caldas 1900-1930)':
        {'main_points': 'Ruta_Cafetera_Manizales_Buenaventura.csv',
         'ways': ['1172223300.csv']},
    'Ruta Cafetera: Manizales - Puerto Colombia (PAC-Caldas 1900-1930)':
        {'main_points': 'Ruta_Cafetera_Manizales_Puerto_Colombia.csv',
            'ways': ['222909864.csv','1186114535.csv','1186114534.csv',
                     '1186114533.csv', '1186114532.csv', '1172223300.csv']
         # 'ways': ['1172223300.csv','89114136.csv','100647095.csv','248954095.csv','91364457.csv','91365705.csv','100615639.csv']
    },
}

left_pane, right_pane =  st.columns([4, 1])

# Protection Type to Show
selected_route = left_pane.selectbox(
    "Selección de Ruta:",
    options=sorted(routes.keys()),
    index=0  # Default to the first group in the list
)

locations_df = pd.read_csv(f"data/{routes[selected_route]['main_points']}")
list_of_ways = routes[selected_route]['ways']


with left_pane:

    # Create a Map of Colombia
    m = folium.Map(location=[6.3709, -75.2973],
                   zoom_start=6, min_zoom=5, max_zoom=16,
                   min_lat=16, max_lat= -1,
                   min_lon=-82, max_lon= -67,
                   control_scale = True, tiles="cartodb positron"
                   )

    # Icon Definition
    with open('data/location_types.json') as json_file:
        location_types = json.load(json_file)

    # Icon Definition
    location_types = {
        'Patrimonio Industrial,WayPoint':
         {'location_group': 'WayPoint',
             'icon_name': 'circle-dot', 'icon_color': 'cadetblue', 'icon_prefix': 'fa'},
        'Patrimonio Industrial,Ferrocarril':
            {'location_group': 'Patrimonio Industrial',
             'icon_name': 'train', 'icon_color': 'cadetblue', 'icon_prefix': 'fa'},
        'Patrimonio Industrial,Aeropuerto':
            {'location_group': 'Patrimonio Industrial',
             'icon_name': 'hands-holding-circle', 'icon_color': 'cadetblue', 'icon_prefix': 'fas'},
        'Patrimonio Industrial,Puerto':
            {'location_group': 'Patrimonio Industrial',
             'icon_name': 'ship', 'icon_color': 'cadetblue', 'icon_prefix': 'fa'},
        'Patrimonio Industrial,Puente':
            {'location_group': 'Patrimonio Industrial',
             'icon_name': 'bridge-water', 'icon_color': 'cadetblue', 'icon_prefix': 'fa'},
        'Patrimonio Industrial,Cable':
            {'location_group': 'Patrimonio Industrial',
             'icon_name': 'cable-car', 'icon_color': 'cadetblue', 'icon_prefix': 'fa'}
    }

    # List to hold all visible locations' coordinates
    visible_locations = []
    visible_locations_info = []

    previous_point = None

    for idx, row in locations_df.iterrows():

        location_type = f"{row['Type']},{row['Subtype']}".replace(',nan','')
        location_group = location_types[location_type]['location_group']
        location_department = row['Department']

        new_point = [row['Latitude'], row['Longitude']]

        visible_locations.append(new_point)

        image_src = "resources/images/colombia-heritage-logo.jpg"

        if location_type != 'Patrimonio Industrial,WayPoint':

            # Create the HTML content for the popup
            html = f"""
                <h4>{row['Name']}</h4>
                <img src="{image_src}" width="150"><br>
                <p>{row['Department']}, {row['City']}</p>
                <p>Location: {m.location}</p>               
            """

            iframe = IFrame(html, width=300, height=300)
            popup = folium.Popup(iframe, max_width=2650)

            # Add marker with popup
            folium.Marker(
                [row['Latitude'], row['Longitude']],
                popup=popup,
                icon=folium.Icon(
                    icon=location_types[location_type]['icon_name'],
                    prefix=location_types[location_type]['icon_prefix'],
                    color=location_types[location_type]['icon_color']
                    )
            ).add_to(m)

        if not previous_point is None:
            points = [previous_point, new_point]
            folium.PolyLine(points, color="red", weight=3.5, dash_array='15', opacity=1).add_to(m)

        visible_locations_info.append(
            f"{location_type} {location_group} "
            f"{row['Name']} {row['Department']} {row['City']} "
            f"{location_types[location_type]['icon_color']} "
            f"{location_types[location_type]['icon_name']} "
            f"{location_types[location_type]['icon_prefix']} "
        )

        previous_point = new_point

    # debug.write('visible_locations_info')
    # debug.write(visible_locations_info)


    # Add Way Points
    # for way in list_of_ways:
    #
    #     debug.write(way)
    #
    #     way_df = pd.read_csv(f'resources/OSM/{way}')
    #     right_pane.write(f'Way:{way}')
    #     right_pane.write(way_df)
    #
    #     previous_way_point = None
    #
    #     for idx, row in way_df.iterrows():
    #         new_way_point = [row['Latitude'], row['Longitude']]
    #         if not previous_way_point is None:
    #             way_points = [previous_way_point, new_way_point]
    #             folium.PolyLine(way_points, color="green", weight=3.5, dash_array='1', opacity=1).add_to(m)
    #
    #         previous_way_point = new_way_point

    # Adjust zoom based on the number of visible locations
    if len(visible_locations) == 1:
        # m.location = visible_locations[0]
        # m.zoom_start = 20
        folium.Map(location=visible_locations[0], zoom_start=20)
    elif len(visible_locations) > 1:
        m.fit_bounds(visible_locations)

    # Add LatLngPopup to capture click events
    m.add_child(folium.LatLngPopup())

    # Show map
    folium_static(m, width=800, height=620)

debug = st.expander("See Data in use")
debug.write(list_of_ways)
debug.write(locations_df)
debug.write(location_types)
debug.write(visible_locations_info)


