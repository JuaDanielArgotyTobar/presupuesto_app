import streamlit as st
from supabase import create_client, Client
from datetime import datetime
from json import dumps


st.set_page_config(page_title="Registrar Gasto",
                   page_icon="💸")


# Initialize connection.
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()
# ===========================================================================
# Obtener categorías desde la base de datos
def obtener_categorias():
    response = supabase.table("categorias").select("*").execute()
    if response.data:
        return {categoria["nombre"]: categoria["id"] for categoria in response.data}
    return {}

# Insertar un gasto en la base de datos
def insertar_gasto(producto, categoria_ids, precio, duracion, personas, fecha):
    fecha_str = fecha.strftime("%Y-%m-%d")  # Convertir fecha a string
    for categoria_id in categoria_ids:
        data = {
            "producto": producto,
            "categoria_id": categoria_id,
            "precio": precio,
            "duracion_dias": duracion,
            "personas": personas,
            "fecha_compra": fecha_str,
        }
        supabase.table("gastos").insert(data).execute()
# ================================================================================
# UI del formulario en Streamlit
st.title("Registro de Gastos")

# Entrada de datos
producto = st.text_input("Gasto")
categorias_dict = obtener_categorias()
categorias_seleccionadas = st.multiselect("Categorías", list(categorias_dict.keys()))
precio = st.number_input("Precio", min_value=0.0, format="%.2f")
duracion = st.number_input("Duración en días", min_value=1, step=1)
personas = st.number_input("Personas", min_value=1, step=1)
fecha = st.date_input("Fecha de compra", datetime.now())

if st.button("Guardar Gasto"):
    if producto and categorias_seleccionadas and precio > 0:
        categoria_ids = [categorias_dict[nombre] for nombre in categorias_seleccionadas]
        insertar_gasto(producto, categoria_ids, precio, duracion, personas, fecha)
        st.success("Gasto registrado correctamente")
    else:
        st.error("Por favor completa todos los campos correctamente")