import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mi Biblioteca", layout="wide")

st.title("📚 Mi Buscador de Libros")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_excel("InventarioBiblioteca.xlsx")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# Buscador estilo iOS
busqueda = st.text_input("Buscar por nombre, género o estante...", placeholder="Ej: SALA-01")

if busqueda:
    mask = df.apply(lambda x: x.astype(str).str.contains(busqueda, case=False)).any(axis=1)
    resultados = df[mask]
else:
    resultados = df

# Mostrar resultados en tarjetas
for index, row in resultados.iterrows():
    with st.expander(f"📖 {row['Nombre']}"):
        st.write(f"**Géneros:** {row['Géneros1']} | {row['Géneros2']}")
        st.write(f"**Ubicación:** 📍 {row['Estante']}")