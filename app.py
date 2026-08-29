import streamlit as st  # Importa Streamlit para construir la aplicación web.
st.markdown("<style>.stApp {background-color: #EAF2F8;} .titulo {background-color: #163A5F; color: white; padding: 18px; border-radius: 12px;}</style>", unsafe_allow_html=True)  # Define el fondo y crea el estilo CSS de la tarjeta del título.
st.markdown('<div class="titulo"><h1>Calculadora de Grado API</h1></div>', unsafe_allow_html=True)  # Usa un div como contenedor y un h1 como título dentro de la tarjeta.
sg = st.number_input("Gravedad específica:", min_value=0.10, value=0.85, step=0.01)  # Solicita la gravedad específica mediante un widget numérico.
if st.button("Calcular"):  # Crea el botón que activa el cálculo.
    api = (141.5 / sg) - 131.5  # Calcula el grado API.
    st.write("Grado API:", round(api, 2))  # Muestra el resultado del cálculo.
