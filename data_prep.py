import pandas as pd
import numpy as np
full_df = pd.read_csv('data/lol_worlds_2019.csv', na_values = ' ').drop(['url', 'league', 'split', 'date', 'patchno', 'playerid'], axis = 1).set_index('gameid', drop = False)

game_col = ['gameid', 'week', 'game', 'gamelength', 'fbtime', 'fdtime', 'fttime', 'fbarontime',
           'heraldtime', 'ckpm']

team_col = ['side', 'team', 'ban1', 'ban2', 'ban3', 'ban4', 'ban5', 'result', 'k', 'd', 'a',
        'teamkills', 'teamdeaths', 'fb','kpm', 'okpm', 'fd', 
        'teamdragkills', 'oppdragkills', 'elementals', 'oppelementals', 'firedrakes', 'waterdrakes',
        'earthdrakes', 'airdrakes', 'elders', 'oppelders', 'herald',
        'heraldtime', 'ft', 'firstmidouter', 'firsttothreetowers',
        'teamtowerkills', 'opptowerkills', 'fbaron',
        'teambaronkills', 'oppbaronkills', 'epicmonsterkills']

players_col = ['position', 'player', 'team',
       'champion', 'k', 'd', 'a' ,'doubles',
       'triples', 'quadras', 'pentas', 'fb', 'fbassist', 'fbvictim', 'fbtime',
       'kpm', 'okpm','dmgtochamps', 'dmgtochampsperminute', 'dmgshare',
       'earnedgoldshare', 'wards', 'wpm', 'wardshare', 'wardkills', 'wcpm',
       'visionwards', 'visionwardbuys', 'totalgold', 'earnedgpm', 'goldspent',
       'gspd', 'minionkills', 'monsterkills', 'monsterkillsownjungle',
       'monsterkillsenemyjungle', 'cspm', 'goldat10', 'oppgoldat10', 'gdat10',
       'goldat15', 'oppgoldat15', 'gdat15', 'xpat10', 'oppxpat10', 'xpdat10',
       'csat10', 'oppcsat10', 'csdat10', 'csat15', 'oppcsat15', 'csdat15']

full_df.earnedgoldshare = np.round(full_df.earnedgoldshare * 100, decimals = 2)
full_df.wardshare = np.round(full_df.wardshare * 100, decimals = 2)
full_df.dmgshare = np.round(full_df.dmgshare * 100, decimals = 2)
full_df['epicmonsterkills'] = full_df.teamdragkills + full_df.teambaronkills + full_df.herald

team_df = full_df[full_df.position == "Team"]
team_df = team_df.dropna(axis = 1, how = 'all')

players_df = full_df[full_df.position != "Team"]
players_df = players_df.dropna(axis = 1, how = 'all')
players_df['kda'] = (players_df.k + players_df.a) / players_df.d.replace(0, 1)

gamelen_df = team_df[['gamelength']][team_df.result == 1]

cs_df = players_df[['position', 'csat10', 'csat15']]
xp_df = players_df[['position','xpat10']]

stats_df = players_df[['result', 'position', 'dmgshare', 'earnedgoldshare', 'earnedgpm', 'wardshare', 'kda']]

bans_df = team_df.melt(id_vars= 'gameid',value_vars=['ban1','ban2', 'ban3', 'ban4', 'ban5']).drop('variable', axis = 1).set_index('gameid').rename(columns={'value': 'bans'})
pick_df = players_df[['result','champion', 'position']]

red_df = team_df[['result', 'epicmonsterkills', 'teamdragkills','herald', 'teambaronkills', 'elders']][team_df.side == 'Red']
blue_df = team_df[['result', 'epicmonsterkills', 'teamdragkills','herald', 'teambaronkills', 'elders']][team_df.side == 'Blue']

drakes_df = team_df[['result','teamdragkills', 'fd','fdtime', 'firedrakes', 'waterdrakes','earthdrakes', 'airdrakes', 'elders']]
herald_df = team_df[['result','herald', 'heraldtime']]
baron_df = team_df[['result', 'teambaronkills', 'fbaron','fbarontime']]
turrets_df = team_df[['result','ft', 'fttime','teamtowerkills', 'firsttothreetowers']]

nb_games = team_df[team_df.result == 1].shape[0]
nb_teams = team_df.team.unique().shape[0]
nb_players = players_df.player.unique().shape[0]