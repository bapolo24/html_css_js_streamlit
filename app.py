import streamlit as st  # Importa Streamlit para crear la aplicación.
st.markdown("<style>.stApp {background-color: #EAF2F8;} .titulo {background-color: #163A5F; color: white; padding: 18px; border-radius: 12px;} .resultado {background-color: white; padding: 18px; border-radius: 12px; margin-top: 15px;} div.stButton > button {background-color: #1177CC; color: white; border: none; border-radius: 10px; padding: 10px 24px; font-weight: bold;}</style>", unsafe_allow_html=True)  # Define estilos para fondo, tarjetas y botón de Streamlit.
st.markdown('<div class="titulo"><h1>Calculadora de Grado API</h1></div>', unsafe_allow_html=True)  # Crea una tarjeta HTML para el título.
sg = st.number_input("Gravedad específica:", min_value=0.10, value=0.85, step=0.01)  # Solicita la gravedad específica.
if st.button("Calcular"):  # Crea el botón ahora personalizado mediante CSS.
    api = (141.5 / sg) - 131.5  # Calcula el grado API.
    st.markdown(f'<div class="resultado"><h2>{api:.2f} °API</h2><p>Resultado calculado</p></div>', unsafe_allow_html=True)  # Muestra el resultado dentro de una tarjeta.

