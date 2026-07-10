from chargement import reviews_finale, courses
from filtrage import coursea
import pandas as pd

# Utilisateurs exemples à garder absolument
users_importants = [
    "By Abhishek S", "By Gabriela G", "By Pavel S"
    "By Muhammad A", "By David M", "By Lisa H",
    "By Benjamin W", "By Pratik K", "By Kelly C",
]

# Lignes de ces utilisateurs
lignes_importantes = reviews_finale[reviews_finale['reviewers'].isin(users_importants)]

# Reste du dataset sans ces utilisateurs
reste = reviews_finale[~reviews_finale['reviewers'].isin(users_importants)]

# Prendre 50 000 lignes au hasard dans le reste
reste_small = reste.sample(50000, random_state=42)

# Combiner les deux
reviews_small = pd.concat([lignes_importantes, reste_small])

# Sauvegarder
reviews_small.to_csv("Coursera_reviews_small.csv", index=False)
courses.to_csv("Coursera_courses_small.csv", index=False)
coursea.to_csv("coursea_data_small.csv", index=False)

print(f"reviews_small : {len(reviews_small)} lignes")
print(f"Utilisateurs importants inclus : {len(lignes_importantes)} lignes")
print("Fichiers créés avec succès !")