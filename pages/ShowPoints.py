import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
from folium import IFrame
import json

# Load Data
departments_df = pd.read_csv('data/Capitals.csv')
industrial_heritage_df = pd.read_csv('data/Industrial_Heritage.csv')
# st.write(industrial_heritage_df)

data_filenames = ['Airports.csv', 'Ports.csv', 'Volcanoes.csv', 'Train_Stations.csv', 'Industrial_Heritage.csv']
locations_df = pd.concat([pd.read_csv(f'data/{filename}') for filename in data_filenames])
# st.write(locations_df)

available_departments = set(industrial_heritage_df['Department'])
# st.write(available_departments)

debug = st.expander("See Data in use")

left_pane, right_pane =  st.columns([2, 3])

# Protection Type to Show
selected_protection_group = left_pane.selectbox(
    "Selección de Grado de Protección:",
    options=sorted(['Sin Proteccion','Bien de Interés Cultural', 'BIC-Municipal', 'UNESCO', 'BIC-NAL']),
    index=0  # Default to the first group in the list
)

# Location Types to Show
location_group_types_to_show = left_pane.multiselect(
    "Selección de Localizaciones:",
    options=["Aeropuertos Internacionales", "Aeropuertos Nacionales", "Aeropuertos Regionales",
             "Puertos Marítimos", "Puertos Fluviales",
             "Capitales", "Volcanes", "Estaciones de Tren",
             "Patrimonio Industrial"],
    default=["Capitales", "Puertos Marítimos", "Puertos Fluviales",]
)

# Departments to Show
departments_to_show = left_pane.multiselect(
    "Selección de Departamentos:",
    options=sorted(set(departments_df['Department'])),
    # default=sorted(set(industrial_heritage_df['Department']))
    default=sorted(set(departments_df['Department']))
)

with (right_pane):

    # Create a Map of Colombia
    m = folium.Map(location=[6.3709, -75.2973], zoom_start=6, min_zoom=5, max_zoom=13)

    # Icon Definition
    with open('data/location_types.json') as json_file:
        location_types = json.load(json_file)

    debug.write(location_types)

    location_types={
        'Capitales': {'location_group': 'Capitales',
                            'icon_name': 'location-dot', 'icon_color': 'red', 'icon_prefix': 'fa'},
        'Aeropuerto,Internacional': {'location_group': 'Aeropuertos Internacionales',
                                     'icon_name': 'plane', 'icon_color': 'cadetblue', 'icon_prefix': 'fa'},
        'Aeropuerto,Nacional': {'location_group': 'Aeropuertos Nacionales',
                                'icon_name': 'plane', 'icon_color': 'blue', 'icon_prefix': 'fa'},
        'Aeropuerto,Regional': {'location_group': 'Aeropuertos Regionales',
                                'icon_name': 'plane', 'icon_color': 'lightblue', 'icon_prefix': 'fa'},
        'Puerto,Marítimo': {'location_group': 'Puertos Marítimos',
                            'icon_name': 'ship', 'icon_color': 'cadetblue', 'icon_prefix': 'fa'},
        'Puerto,Fluvial': {'location_group': 'Puertos Fluviales',
                           'icon_name': 'ship', 'icon_color': 'green', 'icon_prefix': 'fa'},
        'Volcán': {'location_group': 'Volcanes',
                   'icon_name': 'fire', 'icon_color': 'red', 'icon_prefix': 'fa'},
        'Estación de Tren': {'location_group': 'Estaciones de Tren',
                             'icon_name': 'train', 'icon_color': 'cadetblue', 'icon_prefix': 'fa'},

        'Patrimonio Industrial,Ferrocarril': {'location_group': 'Patrimonio Industrial',
                                              'icon_name': 'hands-holding-circle', 'icon_color': 'red', 'icon_prefix': 'fa'},
        'Patrimonio Industrial,Aeropuerto': {'location_group': 'Patrimonio Industrial',
                                              'icon_name': 'hands-holding-circle', 'icon_color': 'red', 'icon_prefix': 'fa'},
        'Patrimonio Industrial,Puerto': {'location_group': 'Patrimonio Industrial',
                                             'icon_name': 'hands-holding-circle', 'icon_color': 'red', 'icon_prefix': 'fa'},
        'Patrimonio Industrial,Puente': {'location_group': 'Patrimonio Industrial',
                                         'icon_name': 'hands-holding-circle', 'icon_color': 'red', 'icon_prefix': 'fa'},
        'Patrimonio Industrial,Cable': {'location_group': 'Patrimonio Industrial',
                                         'icon_name': 'hands-holding-circle', 'icon_color': 'red', 'icon_prefix': 'fa'}
    }

    # List to hold all visible locations' coordinates
    visible_locations = []
    visible_locations_info = []

    debug.write('location_group_types_to_show')
    debug.write(f'{location_group_types_to_show}')

    debug.write('departments_to_show')
    debug.write(f'{departments_to_show}')

    for idx, row in locations_df.iterrows():

        location_type = f"{row['Type']},{row['Subtype']}"
        if location_type.endswith('nan'):
            location_type = location_type.replace(',nan','')

        location_group = location_types[location_type]['location_group']
        location_department = row['Department']
        
        # st.sidebar.write(f'{location_type} > {location_group} > {location_department}')

        if location_group in location_group_types_to_show and location_department in departments_to_show:

            visible_locations.append([row['Latitude'], row['Longitude']])

            image_src = "https://agroingenio.streamlit.app/~/+/media/494e0dfd8d06c829162b2b15878906b2770a25553f0b791656c4f096.jpg"

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
                    color=location_types[location_type]['icon_color'],
                    icon=location_types[location_type]['icon_name'],
                    prefix=location_types[location_type]['icon_prefix']
                    )
            ).add_to(m)

            visible_locations_info.append(
                f"{location_type} {location_group} "
                f"{row['Name']} {row['Department']} {row['City']} "
                f"{location_types[location_type]['icon_color']} "
                f"{location_types[location_type]['icon_name']} "
                f"{location_types[location_type]['icon_prefix']} "
            )


    debug.write('visible_locations_info')
    debug.write(visible_locations_info)

    # Adjust zoom based on the number of visible locations
    if len(visible_locations) == 1:
        # m.location = visible_locations[0]
        # m.zoom_start = 20
        folium.Map(location=visible_locations[0], zoom_start=20)
    elif len(visible_locations) > 1:
        m.fit_bounds(visible_locations)

    # Add LatLngPopup to capture click events
    m.add_child(folium.LatLngPopup())

    # Mostrar el mapa en Streamlit
    folium_static(m, width=600, height=620)