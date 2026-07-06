from modele import recommand
from chargement import courses

username = input("Entrez le nom de l'utilisateur \n")

# Appel de la fonction
recom = recommand(username)

# Transformer l'index en colonne
recom_nc = recom.reset_index()

# Renommer la colonne 0 en note_moyenne
recom_nc = recom_nc.rename(columns = {0 : 'note_moyenne'})

# Fusionner avec courses
recom_final = recom_nc.merge(courses, on = 'course_id', how = 'left')

# Afficher le résultat
print(recom_final[['name', 'institution', 'note_moyenne']])
