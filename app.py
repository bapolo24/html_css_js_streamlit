import streamlit as st  # Importa Streamlit para construir la aplicación web.
st.markdown("<style>.stApp {background-color: #EAF2F8;}</style>", unsafe_allow_html=True)  # Inserta CSS y cambia el color de fondo de toda la app.
st.title("Calculadora de Grado API")  # Muestra el título principal de la app.
sg = st.number_input("Gravedad específica:", min_value=0.10, value=0.85, step=0.01)  # Crea el campo donde se ingresa la gravedad específica.
if st.button("Calcular"):  # Crea el botón y ejecuta el cálculo al presionarlo.
    api = (141.5 / sg) - 131.5  # Calcula el grado API.
    st.write("Grado API:", round(api, 2))  # Presenta el resultado redondeado.
