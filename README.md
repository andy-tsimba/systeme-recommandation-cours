# Sujet de stage : Système de Recommandation de Cours

# Description
Un système de recommandation de cours basé sur le filtrage collaboratif 
et la similarité cosinus, développé sur un dataset Coursera 
(1 454 711 avis, 623 cours).

# Dataset utilisé
Source : https://www.kaggle.com/datasets/imuhammad/course-reviews-on-coursera

# Structure du projet
1) chargement.py : chargement et nettoyage des données
2) modele.py : calcul de la similarité cosinus et fonction de recommandation
3) main.py : interface utilisateur

# Utilisation
1. Télécharger le dataset depuis Kaggle
2. Placer les fichiers CSV dans le dossier du projet
3. Lancer `main.py` et entrer le nom d'un utilisateur

# Technologies
Python, pandas, scikit-learn, numpy