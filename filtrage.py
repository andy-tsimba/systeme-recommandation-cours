import pandas as pd

from chargement import reviews_finale, courses

import os

if os.path.exists("coursea_data_small.csv"):
    coursea = pd.read_csv("coursea_data_small.csv")
else:
    coursea = pd.read_csv("coursea_data.csv")

notes_moyennes = reviews_finale.groupby('course_id')['rating'].mean().reset_index()
# groupby('course_id') regroupe toutes les lignes par cours
# ['rating'].mean() calcule la moyenne des notes pour chaque cours
# .reset_index() transforme l'index en colonne
notes_moyennes.columns = ['course_id', 'note_moyenne']
# .columns = [...] sert à renommer les colonnes proprement

# Le dictionnaire
domaines = {
    "Data Science" : ["python", "data", "machine-learning", "sql", "statistics", "analytics", "deep-learning", "neural", "ai"],
    "Business": ["business", "finance", "marketing", "management", "strategy", "accounting", "leadership"],
    "Langues": ["english", "korean", "french", "writing", "grammar", "communication", "speak"],
    "Santé": ["health", "medicine", "clinical", "nutrition", "psychology", "brain", "addiction"],
    "Technologie": ["cloud", "aws", "security", "blockchain", "programming", "git", "java", "web"]
}

# La foncction
def recommander_par_domaine(domaine, niveau, n_resultats = 10):
    # 1. Filtrer les cours du bon domaine
    mots_cles = domaines[domaine]
    masque = courses['course_id'].str.contains('|'.join(mots_cles), case = False, na = False)
    cours_domaine = courses[masque]
    # 2. Fusionner avec les notes moyennes
    cours_notes = cours_domaine.merge(notes_moyennes, on = 'course_id', how = 'left')
    # 3. Fusionner avec le niveau depuis coursea_data
    cours_niveau = cours_notes.merge(
        coursea[['course_title', 'course_difficulty']],
        left_on='name',
        right_on='course_title',
        how='left'
    )
    # 4. Filtrer par niveau si choisi
    if niveau != "All":
        cours_niveau = cours_niveau[cours_niveau['course_difficulty'] == niveau]
    # 5. Trier par note moyenne et retourner les meilleurs
    return cours_niveau[cours_niveau['note_moyenne'] >= 3][['name', 'institution', 'note_moyenne', 'course_difficulty', 'course_url']].sort_values('note_moyenne', ascending = False).head(n_resultats)