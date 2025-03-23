import streamlit as st

st.title("Presupuesto Personal")

st.write("Utiliza el menú de la izquierda para navegar a las diferentes secciones de la aplicación.")
if st.button('Ir al Formulario'):
    st.experimental_set_query_params(page='formulario')