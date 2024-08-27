import streamlit as st

st.set_page_config(layout="wide")
st.header("""
    Agroingenio
    Soporte Colaborativo para la Protección del Patrimonio Industrial y Agroindustrial Colombiano
""", divider="orange")

st.sidebar.markdown("Investigadora:")
st.sidebar.markdown("Angela María Santa Quintero")
st.sidebar.markdown("Desarrollador:")
st.sidebar.markdown("Pedro Ángel Vaquero Díaz")
st.image("resources/images/colombia-heritage-logo.jpg", caption="Soporte Colaborativo para la Protección del Patrimonio Industrial y Agroindustrial Colombiano")
# st.image("resources/images/Navegacion_Del_Rio_Magdalena_Por_Vapor.jpg", caption="Navegacion Del Rio Magdalena por Vapor")

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

st.markdown("Investigación y Desarrollo a cargo de Ángela María Santa Quintero y Pedro Ángel Vaquero Diaz &mdash :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


left_pane, right_pane =  st.columns([3, 2])

# Protection Type to Show
selected_route = left_pane.selectbox(
    "Selección de Ruta:",
    options=sorted(routes.keys()),
    index=0  # Default to the first group in the list
)
