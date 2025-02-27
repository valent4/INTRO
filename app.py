import streamlit as st
from PIL import Image 


st.title("Hello word")

st.header("En este espacio comienzo a desarrollar mis apps de interfaces multimodales")
st.write("Facilmente puedo hacer backed y fortend")
image = Image.open("04_01_2014.jpg")

st.image(image, caption="04_01_2014")

texto = st.text_input("El mejor jugador de la historia"," Un crack goles de cabeza, pierna derecha, pierna izquierda, alto, veloz, fuerte")
st.write("Esto es el fucking futbol",texto)

st.subheader("Ahora hay dos columnas")

col1,col2 = st.columns(2)

with col1:
  st.subheader("primera columna")
  st.write("Todo es mejor si programando estoy")
  respecto = st.checkbox("Estoy de acuerdo")
  if respecto:
    st.write("Buenisima")

with col2:
  st.subheader("Segunda columna")
  modo = st.radio("Tu que prefieres backed o fronted",("backend","fronted","ninguna"))
  if modo == "backend":
    st.write("Eres de los mios siuuuuuu")
  if modo == "fronted":
    st.write("Eres una mierda gasss")
  if modo == "ninguna":
    st.write("Que estas haciendo aqui entonces")
