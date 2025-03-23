import streamlit as st

st.set_page_config(page_title="Presupuesto personal",
                   page_icon="💰")


st.title("Creando ingreso de datos")
st.markdown(
    """
    Puedo usar latex
    $$
    \sum_{k_0}^{n-1} a^2
    $$
    """
)

nuevo_gasto = st.Page("tools/ingresar_gasto.py",
                      title="Registrar gasto",
                      icon=":material/add_circle:")