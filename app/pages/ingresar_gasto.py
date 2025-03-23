import streamlit as st
from supabase import create_client, Client
from datetime import datetime
from json import dumps

# Initialize connection.
#@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

# ver gastos
#gastos = supabase.table("gastos").select("*").execute()
#st.write(gastos)


# Ingresar nuevo gasto
#gasto_in = supabase.table("gastos").insert({"id": 1, "producto": "preuba1", "categoria_id": 1, "precio": 5500, "duracion_dias": 15, "personas": 3, "fecha_compra": str(datetime.today())}).execute()
            





    