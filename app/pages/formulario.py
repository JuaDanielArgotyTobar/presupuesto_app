import streamlit as st

st.title("Formulario de Ingreso de Datos")

with st.form(key='formulario_ingreso'):
    nombre = st.text_input('Nombre')
    presupuesto = st.number_input('Presupuesto', min_value=0.0, format="%.2f")
    submit_button = st.form_submit_button(label='Enviar')

if submit_button:
    st.success(f"Datos enviados: Nombre - {nombre}, Presupuesto - {presupuesto}")
    # Aquí puedes agregar la lógica para almacenar los datos en la base de datos
