import streamlit as st  # Importa la librería Streamlit con el alias st.
inicio = st.Page("inicio.py")  # Convierte inicio.py en una página de la aplicación.
api = st.Page("api.py")  # Convierte api.py en otra página de la aplicación.
pagina = st.navigation([inicio, api])  # Crea el menú de navegación con las dos páginas.
pagina.run()  # Ejecuta la página que el usuario haya seleccionado.
