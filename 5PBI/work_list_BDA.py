import pandas as pd


pd.set_option('display.max_rows', None)  # Afficher toutes les lignes
pd.set_option('display.max_columns', None)  # Afficher toutes les colonnes
pd.set_option('display.max_colwidth', None)  # Afficher tout le contenu des colonnes

players_result = pd.read_csv('players_stats.csv')


################## Liste des 100 meilleurs joueurs ##########################
# Filtrage sur les joueurs ayant plus de 10 matchs (useless)
df_filtered = players_result[players_result['Number_of_matchs'] > 10]
# Trie sur le nombre total de points
df_sorted = df_filtered.sort_values(by='total_rank_points_', ascending=False)
# Sélectionner les 100 premiers joueurs
top_100_players = df_sorted.head(101)

print(top_100_players)


############### Liste des 10 meilleurs joueurs par pays (Serbie,France,Canada) #############################

min_matches = 0  # Variable pour le minimun de matchs

# Filtrer et trier les joueurs de Serbie par nombre de matchs, puis trie sur le nombre total de points
df_serbia = players_result[(players_result['ioc'] == 'SRB') & (players_result['Number_of_matchs'] > min_matches)]
df_serbia_sorted_by_matches = df_serbia.sort_values(by='Number_of_matchs', ascending=False)
df_serbia_sorted = df_serbia_sorted_by_matches.sort_values(by='total_rank_points_', ascending=False)
top_10_serbia = df_serbia_sorted.head(10)

# Filtrer et trier les joueurs de France par nombre de matchs, puis trie sur le nombre total de points
df_france = players_result[(players_result['ioc'] == 'FRA') & (players_result['Number_of_matchs'] > min_matches)]
df_france_sorted_by_matches = df_france.sort_values(by='Number_of_matchs', ascending=False)
df_france_sorted = df_france_sorted_by_matches.sort_values(by='total_rank_points_', ascending=False)
top_10_france = df_france_sorted.head(10)

# Filtrer et trier les joueurs du Canada par nombre de matchs, puis trie sur le nombre total de points
df_canada = players_result[(players_result['ioc'] == 'CAN') & (players_result['Number_of_matchs'] > min_matches)]
df_canada_sorted_by_matches = df_canada.sort_values(by='Number_of_matchs', ascending=False)
df_canada_sorted = df_canada_sorted_by_matches.sort_values(by='total_rank_points_', ascending=False)
top_10_canada = df_canada_sorted.head(10)


print("Top 10 joueurs de Serbie:")
print(top_10_serbia)
print("\nTop 10 joueurs de France:")
print(top_10_france)
print("\nTop 10 joueurs du Canada:")
print(top_10_canada)


################## Liste des 10 meilleurs joueurs dans les tranches d'age ######################################
# trie aussi sur le nombre de matchs et puis sur le total de points , d'ailleurs bien que je le mettes, j'ai "désactivé" le tries sur le nombre de matchs parce que pour la plupart, il n'y pas assez de joueurs

min_matches = 0  # Variable pour le minimun de matchs

# Tranche d'âge 18-24
df_18_24 = players_result[(players_result['age'] >= 18) & (players_result['age'] <= 24) & (players_result['Number_of_matchs'] > min_matches)]
df_18_24_sorted_by_matches = df_18_24.sort_values(by='Number_of_matchs', ascending=False)
df_18_24_sorted = df_18_24_sorted_by_matches.sort_values(by='total_rank_points_', ascending=False)
top_10_18_24 = df_18_24_sorted.head(10)

# Tranche d'âge 25-30
df_25_30 = players_result[(players_result['age'] >= 25) & (players_result['age'] <= 30) & (players_result['Number_of_matchs'] > min_matches)]
df_25_30_sorted_by_matches = df_25_30.sort_values(by='Number_of_matchs', ascending=False)
df_25_30_sorted = df_25_30_sorted_by_matches.sort_values(by='total_rank_points_', ascending=False)
top_10_25_30 = df_25_30_sorted.head(10)

# Tranche d'âge 31-35
df_31_35 = players_result[(players_result['age'] >= 31) & (players_result['age'] <= 35) & (players_result['Number_of_matchs'] > min_matches)]
df_31_35_sorted_by_matches = df_31_35.sort_values(by='Number_of_matchs', ascending=False)
df_31_35_sorted = df_31_35_sorted_by_matches.sort_values(by='total_rank_points_', ascending=False)
top_10_31_35 = df_31_35_sorted.head(10)

# Tranche d'âge 35 et au-dela
df_35_plus = players_result[(players_result['age'] > 35) & (players_result['Number_of_matchs'] > min_matches)]
df_35_plus_sorted_by_matches = df_35_plus.sort_values(by='Number_of_matchs', ascending=False)
df_35_plus_sorted = df_35_plus_sorted_by_matches.sort_values(by='total_rank_points_', ascending=False)
top_10_35_plus = df_35_plus_sorted.head(10)


print("Top 10 joueurs de 18-24 ans:")
print(top_10_18_24)
print("\nTop 10 joueurs de 25-30 ans:")
print(top_10_25_30)
print("\nTop 10 joueurs de 31-35 ans:")
print(top_10_31_35)
print("\nTop 10 joueurs de plus de 35 ans:")
print(top_10_35_plus)



