import streamlit as st
from PIL import Image

# Configurar el título y el ícono de la pestaña
st.set_page_config(page_title="Explorando la Naturaleza", page_icon="🌱")

# Título principal
st.title("🌿 Bienvenidos al Paraíso Natural")

# Subtítulo introductorio
st.header("Un espacio para conectar con la naturaleza a través de la tecnología")
st.write("Aquí combino mis habilidades de desarrollo backend y frontend para crear experiencias interactivas que celebren nuestro entorno natural.")

# Imagen destacada
image = Image.open("valen.jpeg")
st.image(image, caption="Un rincón de paz en la Tierra", use_container_width=True)

# Entrada de texto
texto = st.text_input("¿Qué representa la naturaleza para ti?", "Es vida, equilibrio y belleza.")
st.write("💬 Tu reflexión:", texto)

# Subtítulo para la sección de columnas
st.subheader("Explora más...")

# Crear dos columnas
col1, col2 = st.columns(2)

# Primera columna
with col1:
    st.subheader("🌳 Conexión")
    st.write("¿Sientes que la naturaleza influye en tu bienestar?")
    acuerdo = st.checkbox("Sí, totalmente")
    if acuerdo:
        st.success("🌞 ¡Qué hermoso reconocerlo!")

    # NUEVAS OPCIONES DE CONEXIÓN
    actividad = st.selectbox(
        "¿Qué actividad te hace sentir más conectad@ con la naturaleza?",
        ("Caminar descalzo en el pasto", 
         "Escuchar el sonido del bosque",
         "Observar el cielo estrellado", 
         "Tocar plantas o árboles")
    )
    st.write(f"🍃 Actividad elegida: {actividad}")

# Segunda columna
with col2:
    st.subheader("🍃 Tu Rol")
    preferencia = st.radio("¿Cómo te gusta ayudar al planeta?", 
                           ("Cuidando el agua", "Plantando árboles", "Reduciendo residuos"))
    if preferencia:
        st.info(f"🌍 Cada acción cuenta: {preferencia}")

# Pie de página
st.markdown("---")
st.markdown("🌸 *Gracias por visitar este pequeño homenaje a la naturaleza.*")


