import pandas as pd


pd.set_option('display.max_rows', None)  # Afficher toutes les lignes
pd.set_option('display.max_columns', None)  # Afficher toutes les colonnes
#pd.set_option('display.max_colwidth', None)  # Afficher tout le contenu des colonnes

df0 = pd.read_csv('tennis_dataset/atp_matches_2010.csv')
df1 = pd.read_csv('tennis_dataset/atp_matches_2011.csv')
df2 = pd.read_csv('tennis_dataset/atp_matches_2012.csv')
df3 = pd.read_csv('tennis_dataset/atp_matches_2013.csv')
df4 = pd.read_csv('tennis_dataset/atp_matches_2014.csv')
df5 = pd.read_csv('tennis_dataset/atp_matches_2015.csv')
df6 = pd.read_csv('tennis_dataset/atp_matches_2016.csv')
df7 = pd.read_csv('tennis_dataset/atp_matches_2017.csv')
df8 = pd.read_csv('tennis_dataset/atp_matches_2018.csv')
df9 = pd.read_csv('tennis_dataset/atp_matches_2019.csv')
df10 = pd.read_csv('tennis_dataset/atp_matches_2020.csv')
df11 = pd.read_csv('tennis_dataset/atp_matches_2021.csv')
df12 = pd.read_csv('tennis_dataset/atp_matches_2022.csv')
df13 = pd.read_csv('tennis_dataset/atp_matches_2023.csv')
df14 = pd.read_csv('tennis_dataset/atp_matches_2024.csv')

# Concaténation des dataframes
newDf = pd.concat([df0,df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14])



total_rows = newDf.shape[0]
# print(f"\nNombre total de lignes dans le DataFrame : {total_rows}")
# print("\n")

# Conveesion en format Datetime pour éviter le XX/XX/XXXX et pour transformer en XXXX-XX-XX
newDf['tourney_date'] = pd.to_datetime(newDf['tourney_date'], format='%Y%m%d')

duplicate_rows = newDf.duplicated().sum() 
print(f" Nombre de ligne dupliqué : {duplicate_rows} ")


# Typages des autres colonnes possédant une valeur ronde et pour faire en sorte de pouvoir faire du tri décroissant ou croissant
newDf['winner_ht'] = newDf['winner_ht'].fillna(0)
newDf['winner_ht'] = newDf['winner_ht'].astype(int)

newDf['winner_age'] = newDf['winner_age'].fillna(0)
newDf['winner_age'] = newDf['winner_age'].astype(int)

newDf['loser_ht'] = newDf['loser_ht'].fillna(0)
newDf['loser_ht'] = newDf['loser_ht'].astype(int)

newDf['loser_age'] = newDf['loser_age'].fillna(0)
newDf['loser_age'] = newDf['loser_age'].astype(int)

newDf['minutes'] = newDf['minutes'].fillna(0)
newDf['minutes'] = newDf['minutes'].astype(int)

newDf['w_ace'] = newDf['w_ace'].fillna(0)
newDf['w_ace'] = newDf['w_ace'].astype(int)

newDf['w_df'] = newDf['w_df'].fillna(0)
newDf['w_df'] = newDf['w_df'].astype(int)

newDf['w_svpt'] = newDf['w_svpt'].fillna(0)
newDf['w_svpt'] = newDf['w_svpt'].astype(int)

newDf['w_1stIn'] = newDf['w_1stIn'].fillna(0)
newDf['w_1stIn'] = newDf['w_1stIn'].astype(int)

newDf['w_1stWon'] = newDf['w_1stWon'].fillna(0)
newDf['w_1stWon'] = newDf['w_1stWon'].astype(int)

newDf['w_2ndWon'] = newDf['w_2ndWon'].fillna(0)
newDf['w_2ndWon'] = newDf['w_2ndWon'].astype(int)

newDf['w_SvGms'] = newDf['w_SvGms'].fillna(0)
newDf['w_SvGms'] = newDf['w_SvGms'].astype(int)

newDf['w_bpSaved'] = newDf['w_bpSaved'].fillna(0)
newDf['w_bpSaved'] = newDf['w_bpSaved'].astype(int)

newDf['w_bpFaced'] = newDf['w_bpFaced'].fillna(0)
newDf['w_bpFaced'] = newDf['w_bpFaced'].astype(int)

newDf['l_ace'] = newDf['l_ace'].fillna(0)
newDf['l_ace'] = newDf['l_ace'].astype(int)

newDf['l_df'] = newDf['l_df'].fillna(0)
newDf['l_df'] = newDf['l_df'].astype(int)

newDf['l_svpt'] = newDf['l_svpt'].fillna(0)
newDf['l_svpt'] = newDf['l_svpt'].astype(int)

newDf['l_1stIn'] = newDf['l_1stIn'].fillna(0)
newDf['l_1stIn'] = newDf['l_1stIn'].astype(int)

newDf['l_1stWon'] = newDf['l_1stWon'].fillna(0)
newDf['l_1stWon'] = newDf['l_1stWon'].astype(int)

newDf['l_2ndWon'] = newDf['l_2ndWon'].fillna(0)
newDf['l_2ndWon'] = newDf['l_2ndWon'].astype(int)

newDf['l_SvGms'] = newDf['l_SvGms'].fillna(0)
newDf['l_SvGms'] = newDf['l_SvGms'].astype(int)

newDf['l_bpSaved'] = newDf['l_bpSaved'].fillna(0)
newDf['l_bpSaved'] = newDf['l_bpSaved'].astype(int)

newDf['l_bpFaced'] = newDf['l_bpFaced'].fillna(0)
newDf['l_bpFaced'] = newDf['l_bpFaced'].astype(int)

newDf['winner_rank'] = newDf['winner_rank'].fillna(0)
newDf['winner_rank'] = newDf['winner_rank'].astype(int)

newDf['winner_rank_points'] = newDf['winner_rank_points'].fillna(0)
newDf['winner_rank_points'] = newDf['winner_rank_points'].astype(int)

newDf['loser_rank'] = newDf['loser_rank'].fillna(0)
newDf['loser_rank'] = newDf['loser_rank'].astype(int)

newDf['loser_rank_points'] = newDf['loser_rank_points'].fillna(0)
newDf['loser_rank_points'] = newDf['loser_rank_points'].astype(int)

print(newDf.head(10))
print(newDf.dtypes)

# Sauvegarde du nouveau dataset
newDf.to_csv('atp_matches_2010_to_2024.csv', index=False)










