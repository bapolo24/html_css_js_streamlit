import streamlit as st  # Importa Streamlit para crear la interfaz.
st.markdown("<style>.stApp {background-color: #EAF2F8;} .titulo {background-color: #163A5F; color: white; padding: 18px; border-radius: 12px;} .resultado {background-color: white; padding: 18px; border-radius: 12px; margin-top: 15px;}</style>", unsafe_allow_html=True)  # Agrega CSS para fondo, tarjeta del título y tarjeta del resultado.
st.markdown('<div class="titulo"><h1>Calculadora de Grado API</h1></div>', unsafe_allow_html=True)  # Presenta el título dentro de una tarjeta HTML.
sg = st.number_input("Gravedad específica:", min_value=0.10, value=0.85, step=0.01)  # Permite ingresar la gravedad específica.
if st.button("Calcular"):  # Ejecuta las líneas internas cuando se presiona el botón.
    api = (141.5 / sg) - 131.5  # Calcula el grado API.
    st.markdown(f'<div class="resultado"><h2>{api:.2f} °API</h2><p>Resultado calculado</p></div>', unsafe_allow_html=True)  # Inserta el resultado dentro de una tarjeta con h2 y un párrafo.

