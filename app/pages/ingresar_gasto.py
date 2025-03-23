import streamlit as st
from datetime import datetime
from supabase import create_client

# Establecer la conexión con Supabase
supabase = st.connection("supabase").connect()

st.set_page_config(page_title="Ingresar Gasto", page_icon="📝")

st.title("Ingresar Nuevo Gasto")

# Obtener categorías desde la base de datos
categorias_response = supabase.table("categorias").select("*").execute()
categorias = [categoria['nombre'] for categoria in categorias_response.data]

# Crear el formulario
with st.form(key='ingresar_gasto'):
    producto = st.text_input('Producto')
    categoria = st.selectbox('Categoría', categorias)
    precio = st.number_input('Precio', min_value=0.0, format="%.2f")
    duracion_dias = st.number_input('Duración (días)', min_value=0, format="%d")
    personas = st.number_input('Número de personas', min_value=1, format="%d")
    fecha_compra = st.date_input('Fecha de compra', value=datetime.today())
    submit_button = st.form_submit_button(label='Registrar Gasto')

# Procesar el formulario
if submit_button:
    # Obtener el ID de la categoría seleccionada
    categoria_id = next((cat['id'] for cat in categorias_response.data if cat['nombre'] == categoria), None)
    
    # Datos a insertar
    gasto_data = {
        "producto": producto,
        "categoria_id": categoria_id,
        "precio": precio,
        "duracion_dias": duracion_dias,
        "personas": personas,
        "fecha_compra": fecha_compra.isoformat()
    }
    
    # Insertar datos en la tabla 'gastos' de Supabase
    response = supabase.table("gastos").insert(gasto_data).execute()
    
    if response.status_code == 201:
        st.success("Gasto registrado correctamente.")
    else:
        st.error(f"Error al registrar el gasto: {response.json()}")
