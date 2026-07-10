import pandas as pd
import os

# Si les fichiers réduits existent (Streamlit Cloud), on les utilise
# Sinon on utilise les fichiers complets (en local)
if os.path.exists("Coursera_reviews_small.csv"):
    reviews = pd.read_csv("Coursera_reviews_small.csv")
    courses = pd.read_csv("Coursera_courses_small.csv")
else:
    reviews = pd.read_csv("Coursera_reviews.csv")
    courses = pd.read_csv("Coursera_courses.csv")


# On supprime les comptes supprimés
reviews = reviews[reviews['reviewers'] != "By Deleted A"]

# On filtre les utilisateurs peu actifs (en utilisant un seuil >= 50)
nb_avis_par_user = reviews['reviewers'].value_counts()
users_actifs = nb_avis_par_user[nb_avis_par_user >= 50]
reviews_finale = reviews[reviews['reviewers'].isin(users_actifs.index)]

# On construction les matrices
tab_matrice_finale = reviews_finale.pivot_table(
    index = 'reviewers',
    columns = 'course_id',
    values = 'rating'
)
matrice_full = tab_matrice_finale.fillna(0)

