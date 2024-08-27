import streamlit as st

# python -m streamlit run .\streamlit_app.py

st.set_page_config(layout="wide")
st.header("""
    :compass: Agroingenio:
    Soporte Colaborativo para la Protección del Patrimonio Industrial y Agroindustrial Colombiano :material/search_check:
""", divider="orange")

st.sidebar.header(":compass: Agroingenio")
st.sidebar.markdown("Soporte Colaborativo para la Protección del Patrimonio Industrial y Agroindustrial Colombiano :material/search_check:")

st.image("resources/images/colombia-heritage-logo.jpg")

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

st.markdown("Investigación y Desarrollo a cargo de Ángela María Santa Quintero y Pedro Ángel Vaquero Diaz :woman_standing::man_standing: ")
