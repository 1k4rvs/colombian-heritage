import streamlit as st

# python -m streamlit run .\streamlit_app.py

# st.logo(
#     'https://upload.wikimedia.org/wikipedia/commons/c/ce/World_Heritage_Logo_global.svg',
#     link="https://streamlit.io/gallery",
#     icon_image='https://upload.wikimedia.org/wikipedia/commons/c/ce/World_Heritage_Logo_global.svg',
# )

st.set_page_config(layout="wide")

st.sidebar.header(":compass: AgroIngenio")
st.sidebar.markdown("Soporte Colaborativo para la Protección del Patrimonio Industrial y Agroindustrial Colombiano :material/search_check:")

main = st.Page(
    "pages/Main.py", title="Principal", icon=":material/home:", default=True
)

sites = st.Page(
    "pages/ShowPoints.py", title="Lugares", icon=":material/grade:"
)


routes = st.Page(
    "pages/ShowRoutes.py", title="Rutas", icon=":material/route:"
)

maps = st.Page(
    "pages/PilotMapPoC.py", title="Maps", icon=":material/map:"
)

pg = st.navigation(
    {
        "Main": [main],
        "Items": [sites, routes],
        "Maps": [maps],
    }
)

pg.run()