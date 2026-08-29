import streamlit as st  # Importa Streamlit para construir la aplicación web.
st.title("Calculadora de Grado API")  # Muestra el título principal de la app.
sg = st.number_input("Gravedad específica:", min_value=0.10, value=0.85, step=0.01)  # Crea un campo numérico para ingresar la gravedad específica.
if st.button("Calcular"):  # Crea el botón y ejecuta el bloque solo cuando el usuario lo presiona.
    api = (141.5 / sg) - 131.5  # Calcula el grado API con la fórmula estándar.
    st.write("Grado API:", round(api, 2))  # Presenta el resultado redondeado a dos decimales.
