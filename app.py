import streamlit as st
import os
from utils.db import save_user_data, save_pitch_data, load_user_data
from utils.generator import generate_pitch
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

st.set_page_config(page_title="Presentación Semanal BNI", page_icon="📢")

st.title("📢 Presentación Semanal BNI")

user_id = st.text_input("Introduce tu email para identificarte:")

if user_id:
    user_data = load_user_data(user_id)
    if not user_data:
        st.subheader("Información de perfil (solo la primera vez)")
        name = st.text_input("Nombre")
        company = st.text_input("Empresa")
        membership = st.text_input("Membresía (profesión)")

        if st.button("Guardar perfil"):
            save_user_data(user_id, name, company, membership)
            st.success("✅ Perfil guardado correctamente. ¡Ya puedes rellenar tu presentación semanal!")
            st.rerun()
    else:
        st.subheader(f"Bienvenido, {user_data['name']} de {user_data['company']} ({user_data['membership']})")

        with st.form("weekly_form"):
            list_number = st.text_input("Número en la lista esta semana")
            units_completed = st.number_input("Unidades de formación completadas", min_value=0)
            one_to_one = st.number_input("Reuniones 1 a 1 realizadas", min_value=0)
            business_closed_name = st.text_input("Nombre del miembro (negocio cerrado)")
            business_closed_amount = st.number_input("Importe negocio cerrado (€)", min_value=0)
            references_given = st.number_input("Número de referencias dadas", min_value=0)
            reference_type = st.radio("Tipo de referencia:", ["Interna", "Externa"])

            service_highlight = st.text_input("Servicio que quieres destacar esta semana")
            competitive_advantage = st.text_area("¿Cuál es tu ventaja competitiva?")
            story_example = st.text_area("Cuenta una historia o ejemplo real reciente")
            ideal_client = st.text_area("¿Qué tipo de cliente ideal buscas? (Sé muy específico)")

            duration = st.selectbox("Duración deseada", [30, 45, 60, 90])
            tone = st.selectbox("Tono deseado", ["Profesional", "Cercano", "Inspirador", "Humorístico"])

            submit = st.form_submit_button("Generar presentación")

            if submit:
                pitch = generate_pitch(
                    user_data,
                    list_number,
                    units_completed,
                    one_to_one,
                    business_closed_name,
                    business_closed_amount,
                    references_given,
                    reference_type,
                    service_highlight,
                    competitive_advantage,
                    story_example,
                    ideal_client,
                    duration,
                    tone
                )
                save_pitch_data(user_id, pitch)
                st.success("✅ ¡Presentación generada!")
                st.text_area("Aquí tienes tu presentación:", pitch, height=300)