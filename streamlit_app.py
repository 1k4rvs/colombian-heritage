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
