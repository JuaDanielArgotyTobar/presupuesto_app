import streamlit as st

st.set_page_config(page_title="Presupuesto personal",
                   page_icon="💰")


st.title("Creando ingreso de datos")

# Everything is accessible via the st.secrets dict:
st.write("DB url:", st.secrets.SUPABASE_URL)
