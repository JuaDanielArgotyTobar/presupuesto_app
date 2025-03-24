import streamlit as st
from supabase import create_client, Client

st.set_page_config(page_title="Gastos",
                   page_icon="📖")

# Initialize connection.
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

# Obtener los datos de la tabla "gastos"
def obtener_gastos():
    response = supabase.table("gastos").select("*").execute()
    return response.data if response.data else []

# ===========================================================================================
# Mostrar tabla de gastos 
st.title("📊 Historial de Gastos")

gastos = obtener_gastos()
if gastos:
    st.dataframe(gastos)  # Mostrar la tabla en Streamlit
else:
    st.warning("No hay datos en la tabla de gastos.")