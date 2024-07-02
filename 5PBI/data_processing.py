import pandas as pd

# Charger le fichier CSV
matchsdf = pd.read_csv('atp_matches_2010_to_2024.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)

# Convertir 'tourney_date' en datetime puisque pour aucunes raisons ça défait la procédure fait avant
matchsdf['tourney_date'] = pd.to_datetime(matchsdf['tourney_date'])

# Ligne pour enlever les tournois, et les triés et regroupé un seul tournois
df_unique = matchsdf.drop_duplicates(subset=['tourney_id'])

# Trie le DataFrame par 'tourney_date' pour avoir le dernier match en premier
matchsdf = matchsdf.sort_values(by='tourney_date', ascending=False)

# Extrait les âges des derniers matchs pour chaque 'winner_id' et 'loser_id'
winner_ages = matchsdf.drop_duplicates(subset='winner_id')[['winner_id', 'winner_age', 'winner_ioc']].rename(columns={'winner_age': 'age', 'winner_ioc': 'ioc'})
loser_ages = matchsdf.drop_duplicates(subset='loser_id')[['loser_id', 'loser_age', 'loser_ioc']].rename(columns={'loser_age': 'age', 'loser_ioc': 'ioc'})

# Compte le nombre de fois que chaque 'winner_id' apparait
winner_counts = matchsdf['winner_id'].value_counts().reset_index()
winner_counts.columns = ['winner_id', 'win_count']
# Compte le nombre de fois que chaque 'loser_id' apparait
loser_counts = matchsdf['loser_id'].value_counts().reset_index()
loser_counts.columns = ['loser_id', 'lose_count']

# Compte le nombre de tournois par joueur gagnant
nombre_tournois_par_gagnant = df_unique.groupby('winner_id')['tourney_id'].nunique().reset_index()
nombre_tournois_par_gagnant.columns = ['winner_id', 'participation_number']
# Compte le nombre de tournois par joueur perdant
nombre_tournois_par_perdant = df_unique.groupby('loser_id')['tourney_id'].nunique().reset_index()
nombre_tournois_par_perdant.columns = ['winner_id', 'participation_number']


# Compte le nombre total d'aces w_ace pour chaque joueur victoires
ace_counts_winner = matchsdf.groupby('winner_id')['w_ace'].sum().reset_index()
ace_counts_winner.columns = ['winner_id', 'total_aces']
# Compter le nombre total d'aces ('l_ace') pour chaque joueur (défaites)
ace_counts_loser = matchsdf.groupby('loser_id')['l_ace'].sum().reset_index()
ace_counts_loser.columns = ['loser_id', 'total_aces']


# Compter le nombre total de double fautes ('w_df') pour chaque joueur (victoires)
doubleF_counts_winner = matchsdf.groupby('winner_id')['w_df'].sum().reset_index()
doubleF_counts_winner.columns = ['winner_id', 'total_doubleF']
# Compter le nombre total de double fautes ('l_df') pour chaque joueur (défaites)
doubleF_counts_loser = matchsdf.groupby('loser_id')['l_df'].sum().reset_index()
doubleF_counts_loser.columns = ['loser_id', 'total_doubleF']

# Compte le nombre total de premiers services w_1stIn pour chaque joueur --> victoires
stIn_counts_winner = matchsdf.groupby('winner_id')['w_1stIn'].sum().reset_index()
stIn_counts_winner.columns = ['winner_id', 'total_1stIn']
# Compte le nombre total de premiers services l_1stIn pour chaque joueur --> défaites
stIn_counts_loser = matchsdf.groupby('loser_id')['l_1stIn'].sum().reset_index()
stIn_counts_loser.columns = ['loser_id', 'total_1stIn']

# Compte le nombre total de premiers services gagnés w_1stWon pour chaque joueur --> victoires
stWon_counts_winner = matchsdf.groupby('winner_id')['w_1stWon'].sum().reset_index()
stWon_counts_winner.columns = ['winner_id', 'total_1stWon']
# Compte le nombre total de premiers services gagnés l_1stWon pour chaque joueur --> défaites
stWon_counts_loser = matchsdf.groupby('loser_id')['l_1stWon'].sum().reset_index()
stWon_counts_loser.columns = ['loser_id', 'total_1stWon']

# Renomme les colonnes pour permettre la concaténation
ace_counts_loser = ace_counts_loser.rename(columns={'loser_id': 'winner_id'})
stIn_counts_loser = stIn_counts_loser.rename(columns={'loser_id': 'winner_id'})
stWon_counts_loser = stWon_counts_loser.rename(columns={'loser_id': 'winner_id'})

# Fusionne les données des aces, double faute , 1er services fait et services remportés pour les victoires et les défaites
ace_counts = pd.concat([ace_counts_winner, ace_counts_loser]).groupby('winner_id')['total_aces'].sum().reset_index()
doubleF_counts = pd.concat([doubleF_counts_winner, doubleF_counts_loser]).groupby('winner_id')['total_doubleF'].sum().reset_index()
total_1stIn = pd.concat([stIn_counts_winner, stIn_counts_loser]).groupby('winner_id')['total_1stIn'].sum().reset_index()
total_1stWon = pd.concat([stWon_counts_winner, stWon_counts_loser]).groupby('winner_id')['total_1stWon'].sum().reset_index()
nbrCompete = pd.concat([nombre_tournois_par_gagnant, nombre_tournois_par_perdant]).groupby('winner_id')['participation_number'].sum().reset_index()

# Ajoute les noms des gagnants en utilisant une jointure avec le DataFrame
winner_names = matchsdf[['winner_id', 'winner_name']].drop_duplicates()

# Fait une jointure de table pour ajouter les noms des gagnants
result = pd.merge(winner_counts, winner_names, on='winner_id')
result = result.rename(columns={'winner_name': 'player_name'})

# Ajout du comptages des défaites
result = pd.merge(result, loser_counts, left_on='winner_id', right_on='loser_id', how='left').drop(columns='loser_id')

# Enleve les NaN par 0 dans la colonne lose_count pour pouvoir faire apres le ratio victoire/défaite
result['lose_count'] = result['lose_count'].fillna(0).astype(int)

# Calcul du ratio victoire/défaite et arrondi au centième
result['win/lose_ratio'] = (result['win_count'] / result['lose_count']).replace([float('inf'), -float('inf')], 0).fillna(0).round(2)
result['Number_of_matchs'] = (result['win_count'] + result['lose_count']).replace([float('inf'), -float('inf')], 0).fillna(0).round(2)

# Ajoute les âges des gagnants et des perdants
result = pd.merge(result, winner_ages, on='winner_id', how='left')
result = pd.merge(result, loser_ages, left_on='winner_id', right_on='loser_id', how='left', suffixes=('', '_loser'))

# Fusionne les données des aces, double faute , 1er services fait et services remportés dans le dataframe result
result = pd.merge(result, ace_counts, on='winner_id', how='left')
result = pd.merge(result, doubleF_counts, on='winner_id', how='left')
result = pd.merge(result, total_1stIn, on='winner_id', how='left')
result = pd.merge(result, total_1stWon, on='winner_id', how='left')

# Ajoute le nombre de compétitions
result = pd.merge(result, nbrCompete, on='winner_id', how='left')

# Calcul du pourcentage de balle qui marque un point au premier service
result['FirstSvcMade/FirstSvcWon'] = (result['total_1stWon'] / result['total_1stIn']).fillna(0).round(4) * 100 

# Remplace les NaN par les valeurs correspondantes et supprime les colonnes inutiles
result['age'] = result['age'].combine_first(result['age_loser'])
result['ioc'] = result['ioc'].combine_first(result['ioc_loser'])
result = result.drop(columns=['age_loser', 'ioc_loser', 'loser_id'])

# Réorganise les colonnes pour avoir des colonnes dans un ordre correct (Tableau fait un peu n'importe comment ptdr)
result = result[['winner_id', 'player_name', 'age', 'ioc','participation_number','Number_of_matchs', 'win_count', 'lose_count', 'win/lose_ratio','total_aces','total_doubleF','total_1stIn','total_1stWon','FirstSvcMade/FirstSvcWon']]
result = result.rename(columns={'winner_id': 'player_id'})

# Enleve les valeurs NaN pour pouvoir trié dans powerbi sur le nombre de tournois participé 
result['participation_number'] = result['participation_number'].fillna(0).astype(int)

# Ajoute une colonne pour obtenir l'année de chaque tournoi
matchsdf['year'] = matchsdf['tourney_date'].dt.year

# Trie le DataFrame par tourney_date pour avoir le dernier match en premier par année
last_matches = matchsdf.sort_values('tourney_date').groupby(['year', 'winner_id']).tail(1)

# Extrait les colonnes nécessaires pour les gagnants
winner_ranks_points = last_matches[['year', 'winner_id', 'winner_rank', 'winner_rank_points']].rename(columns={
    'winner_id': 'player_id',
    'winner_rank': 'rank',
    'winner_rank_points': 'rank_points'
})

# Utilise pivot_table pour crée un tableau dynamique
pivot_table = winner_ranks_points.pivot_table(index='player_id', columns='year', values=['rank', 'rank_points'], aggfunc='first')

# Remplace les valeurs NaN par 99999 ou 0 pour éviter d'avoir des problemes lors des tries des rangs sur PowerBI, j'ai mis 99999 parce qu'il n'y pas autant de participants
pivot_table['rank'].fillna(99999, inplace=True)
pivot_table['rank'].replace({0: 99999}, inplace=True)
pivot_table['rank_points'].fillna(0, inplace=True)

# Converti les colonnes du dataset des rangs et points en entier pour pouvoir triés
pivot_table = pivot_table.astype(int)

# fait la somme horizontalement des points de rangs des colonnes rank_points 
pivot_table['total_rank_points'] = pivot_table['rank_points'].sum(axis=1)

# Renommer les colonnes ranks et etc... en mettant la date à la fin
pivot_table.columns = [f'{col[0]}_{col[1]}' for col in pivot_table.columns]

# Fusionne pivot_table avec result pour faire qu'un seul tableau
result = pd.merge(result, pivot_table, on='player_id', how='left')

# print(pivot_table.head(10))

print(result.head(25))

# Sauvegarde le nouveau dataframe dans un fichier CSV
result.to_csv('players_stats.csv', index=False)
