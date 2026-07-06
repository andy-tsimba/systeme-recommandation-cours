from sklearn.metrics.pairwise import cosine_similarity

from chargement import matrice_full, tab_matrice_finale, courses

similarities = cosine_similarity(matrice_full)

def recommand(username, n_neigh = 50, seuil = 3):
    pst = list(matrice_full.index).index(username) # Numéro de ligne de l'user dans la matrice
    order = similarities[pst].argsort()[::-1] # Récupération de ses similarités et tri (plus similaire au moins)
    neigh_pst = order[1 : n_neigh+1] # Positions des n voisins (débuter par 1 pour ignorer le concerné)
    neigh_noms = matrice_full.index[neigh_pst] # Numéros de position deviennent Vrais noms d'user
    neigh_rnkgs = tab_matrice_finale.loc[neigh_noms] # Récupérat° des notes des voisins (matrice avec NaN pour une vraie moyenne, 0 fausse le calcul)
    neigh_moy = neigh_rnkgs.mean() # Moyenne par cours (NaN ignorés automatiquement)
    trgt_ranking = matrice_full.loc[username] # Récupérat° des notes du concerné (matrice avec 0 pour détecter les cours non vus)
    trgt_ranking = trgt_ranking.reindex(neigh_moy.index, fill_value = 0)  # # Force la cible à avoir les mêmes cours que les voisins pour pouvoir les comparer
    rec = neigh_moy[(neigh_moy >= seuil) & (trgt_ranking == 0)] # On garde les cours bien notés par les voisins ET non vus par le concerné
    return rec.sort_values(ascending = False) # On retourne les récommandations (du meilleur score au moins bon)
