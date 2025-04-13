import streamlit as st
import pandas as pd
st.title("Ma première application Streamlit")
st.write("Bienvenue dans ce cours !")
nom = st.text_input("Quel est votre nom ?")
if nom:
    st.success(f"Enchanté, {nom} ! ")
age = st.slider("Quel est votre âge ?", 0, 100, 25)
st.write(f"Vous avez {age} ans")
genre = st.radio("Quel est votre genre ?", ["Homme", "Femme"])
st.write(f"Genre choisi : {genre}")
if st.button("Cliquez ici"):
    st.balloons()
import pandas as pd
import numpy as np
df = pd.DataFrame(
np.random.randn(10, 3),
columns=['Colonne A', 'Colonne B', 'Colonne C']
)
st.subheader("Tableau de données")
st.dataframe(df)
st.subheader("Graphique en courbes")
st.line_chart(df)

uploaded_file = st.file_uploader("Chargez un fichier CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :")
    st.dataframe(df.head())
    st.write("Statistiques descriptives :")
    st.write(df.describe())
    colonne = st.selectbox("Choisissez une colonne numérique :",df.select_dtypes(include=np.number).columns)
    st.line_chart(df[colonne])
    
def show_sheets_page():
    st.title("Lecture de Google Sheets dans Streamlit")

    # Remplace cet ID par celui de ta feuille Google Sheets
    sheet_id = "141zRmgsPVjZk9t1jn0vVUckNKfDKs2WGIr9WJb4-Yqw"
    sheet_name = "ensamte"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    try:
        df = pd.read_csv(url)
        st.success("Données chargées avec succès depuis Google Sheets !")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
