import streamlit as st
from utils.db import save_user_data, save_pitch_data, load_user_data
from utils.generator import generate_pitch

st.set_page_config(page_title="Presentación BNI", page_icon="📢")

st.title("📢 Generador de Presentaciones BNI")

# Cargar datos del usuario si existen
user_email = st.text_input("Introduce tu email para identificarte:")
user_data = load_user_data(user_email) if user_email else {}

# Datos del perfil
st.subheader("👤 Datos fijos del usuario")
name = st.text_input("Nombre", user_data.get("name", ""))
empresa = st.text_input("Empresa", user_data.get("empresa", ""))
membresia = st.text_input("Membresía", user_data.get("membresia", ""))

if st.button("Guardar datos de usuario"):
    save_user_data(user_email, name, empresa, membresia)
    st.success("✅ Datos guardados correctamente")

# Datos semanales
st.subheader("📆 Datos de la semana")
numero_lista = st.text_input("Número en la lista")
formacion = st.number_input("Unidades de formación", min_value=0)
reuniones = st.number_input("Reuniones 1 a 1", min_value=0)
nombre_negocio = st.text_input("Gracias por negocio cerrado - Nombre del miembro")
importe_negocio = st.text_input("Importe del negocio cerrado")
referencias = st.number_input("Número de referencias dadas", min_value=0)
tipo_referencia = st.selectbox("Tipo de referencias", ["Interna", "Externa"])

# Presentación del servicio
st.subheader("🧠 Presentación del servicio")
servicio = st.text_input("Servicio que quieres destacar esta semana")
ventaja = st.text_area("Ventaja competitiva")
historia = st.text_area("Historia o ejemplo real")
cliente_ideal = st.text_area("¿Qué cliente estás buscando esta semana? (sé lo más específico posible)")

# Ajustes
st.subheader("🎛️ Ajustes de presentación")
duracion = st.selectbox("Duración estimada", ["30 segundos", "45 segundos", "60 segundos", "90 segundos"])
tono = st.selectbox("Tono", ["Profesional", "Cercano", "Inspirador", "Humorístico"])

if st.button("🎤 Generar presentación"):
    pitch = generate_pitch(name, empresa, membresia, numero_lista, formacion, reuniones,
                           nombre_negocio, importe_negocio, referencias, tipo_referencia,
                           servicio, ventaja, historia, cliente_ideal, duracion, tono)
    st.success("✅ Presentación generada:")
    st.text_area("Tu presentación", pitch, height=300)
    save_pitch_data(user_email, pitch)