import streamlit as st
from PIL import Image

# Configurar el título y el ícono de la pestaña
st.set_page_config(page_title="Explorando la Naturaleza", page_icon="🌱")

# --------- ESTILOS PERSONALIZADOS ---------
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
    }
    .main {
        background-color: #e8f5e9;
        padding: 2rem;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #2e7d32;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #2e7d32;
    }
    .st-bx {
        background-color: #c8e6c9;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --------- CONTENIDO DE LA PÁGINA ---------
st.title("🌿 Bienvenidos al Paraíso Natural")

st.header("Un espacio para conectar con la naturaleza a través de la tecnología")
st.write("Aquí combino mis habilidades de desarrollo backend y frontend para crear experiencias interactivas que celebren nuestro entorno natural.")

# Mostrar imagen
image = Image.open("valen.jpeg")
st.image(image, caption="Un rincón de paz en la Tierra", use_column_width=True)

# Entrada de texto
texto = st.text_input("¿Qué representa la naturaleza para ti?", "Es vida, equilibrio y belleza.")
st.write("💬 Tu reflexión:", texto)

# Sección con dos columnas
st.subheader("Explora más...")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌳 Conexión")
    st.write("¿Sientes que la naturaleza influye en tu bienestar?")
    acuerdo = st.checkbox("Sí, totalmente")
    if acuerdo:
        st.success("🌞 ¡Qué hermoso reconocerlo!")

with col2:
    st.subheader("🍃 Tu Rol")
    preferencia = st.radio("¿Cómo te gusta ayudar al planeta?", 
                           ("Cuidando el agua", "Plantando árboles", "Reduciendo residuos"))
    if preferencia:
        st.info(f"🌍 Cada acción cuenta: {preferencia}")

# Pie de página
st.markdown("---")
st.markdown("🌸 *Gracias por visitar este pequeño homenaje a la naturaleza.*")

