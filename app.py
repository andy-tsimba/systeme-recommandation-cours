import streamlit as st
from modele import recommand
from chargement import courses
from filtrage import recommander_par_domaine

st.title("Système de Recommandation de Cours")
st.write("Découvrez les meilleurs cours Coursera selon vos intérêts !")

onglet1, onglet2 = st.tabs(["Par domaine", "Par utilisateur"])

# ONGLET 1 : Mode principal
with onglet1:
    st.subheader("Trouvez des cours par domaine")
    domaine = st.selectbox("Domaine \n",
                           ["Data Science", "Business", "Langues", "Santé", "Technologie"])
    niveau = st.selectbox("Niveau \n",
                          ["All", "Beginner", "Intermediate", "Advanced"])
    n = st.slider("Nombre de cours à afficher \n", 5, 20, 10)

    if st.button("Recommander", key = "btn1"):
        resultats = recommander_par_domaine(domaine, niveau, n)
        if resultats.empty:
            st.info("Aucun cours trouvé pour cette combinaison.")
        else:
            st.success(f"{len(resultats)} cours trouvés !")
            st.dataframe(resultats)

# ONGLET 2 — Mode secondaire
with onglet2:
    st.subheader("Recommandation personnalisée")
    st.caption("Entrez votre nom d'utilisateur Coursera pour des recommandations basées sur vos goûts.")

    # Exemples d'utilisateurs
    st.info("""
     Exemples d'utilisateurs à tester 
    - By Abhishek S
    - By Gabriela G
    - By Muhammad A
    - By David M
    - By Lisa H
    - By Benjamin W
    - By Pratik K
    - By Kelly C
    - By Pavel S
    """)

    st.caption("⚠️ Les noms d'utilisateurs commencent toujours par 'By' (en anglais), pas 'Par'.")

    username = st.text_input("Nom d'utilisateur Coursera \n")

    if st.button("Recommander", key = "btn2"):
        if username == " ":
            st.warning("Veuillez entrer un nom d'utilisateur \n")
        else:
            try:
                recom = recommand(username, n_neigh = 50, seuil = 2)
                recom_nc = recom.reset_index()
                recom_nc = recom_nc.rename(columns={0 : 'note_moyenne'})
                recom_final = recom_nc.merge(courses, on = 'course_id', how = 'left')
                if recom_final.empty:
                    st.info("Aucune recommandation trouvée pour cet utilisateur.")
                else:
                    st.success(f"{len(recom_final)} cours recommandés !")
                    st.dataframe(recom_final[['name', 'institution', 'note_moyenne']])
            except:
                st.error("Utilisateur introuvable ! Vérifiez le nom ou essayez un exemple.")