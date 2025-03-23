import streamlit as st

st.set_page_config(page_title="Presupuesto personal",
                   page_icon="💰")


st.title("Creando ingreso de datos")

nuevo_gasto = st.Page("tools/ingresar_gasto.py",
                      title="Registrar gasto",
                      icon=":material/add_circle:")