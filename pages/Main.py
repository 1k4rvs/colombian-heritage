import streamlit as st

left_pane, central_pane, right_pane =  st.columns([1,3,1])

central_pane.header("""
    :compass: AgroIngenio:
    Soporte Colaborativo para la Protección del Patrimonio Industrial y Agroindustrial Colombiano :material/search_check:
""", divider="orange")

# st.sidebar.header(":compass: AgroIngenio")
# st.sidebar.markdown("Soporte Colaborativo para la Protección del Patrimonio Industrial y Agroindustrial Colombiano :material/search_check:")

central_pane.image("resources/images/colombia-heritage-logo.jpg")

central_pane.markdown("Investigación y Desarrollo a cargo de Ángela María Santa Quintero y Pedro Ángel Vaquero Diaz :woman_standing::man_standing: ")

