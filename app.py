import streamlit as st  # Importa Streamlit para crear la aplicación.
st.markdown("<style>.stApp {background-color: #EAF2F8;} .titulo {background-color: #163A5F; color: white; padding: 18px; border-radius: 12px;} .resultado {background-color: white; padding: 18px; border-radius: 12px; margin-top: 15px; transition: 0.3s;} .resultado:hover {transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.15);} div.stButton > button {background-color: #1177CC; color: white; border: none; border-radius: 10px; padding: 10px 24px; font-weight: bold;}</style>", unsafe_allow_html=True)  # Añade una transición y un efecto hover a la tarjeta del resultado.
st.markdown('<div class="titulo"><h1>Calculadora de Grado API</h1></div>', unsafe_allow_html=True)  # Muestra el título dentro de una tarjeta.
sg = st.number_input("Gravedad específica:", min_value=0.10, value=0.85, step=0.01)  # Permite ingresar la gravedad específica.
if st.button("Calcular"):  # Ejecuta el cálculo cuando el usuario presiona el botón.
    api = (141.5 / sg) - 131.5  # Calcula el grado API.
    st.markdown(f'<div class="resultado"><h2>{api:.2f} °API</h2><p>Pasa el mouse sobre esta tarjeta</p></div>', unsafe_allow_html=True)  # Presenta el resultado dentro de una tarjeta que se anima al pasar el mouse.
