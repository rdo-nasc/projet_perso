import pandas as pd
import numpy as np

def createFullDf(filename):
        full_df = pd.read_csv(filename, na_values = ' ').drop(['url', 'league', 'split', 'date', 'patchno', 'playerid'], axis = 1).set_index('gameid', drop = False)
        full_df.earnedgoldshare = np.round(full_df.earnedgoldshare * 100, decimals = 2)
        full_df.wardshare = np.round(full_df.wardshare * 100, decimals = 2)
        full_df.dmgshare = np.round(full_df.dmgshare * 100, decimals = 2)
        full_df['epicmonsterkills'] = full_df.teamdragkills + full_df.teambaronkills + full_df.herald
        return full_df

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


def createTeamDf(full_df):
        team_df = full_df[full_df.position == "Team"]
        team_df = team_df.dropna(axis = 1, how = 'all')
        return team_df

def createPlayersDf(full_df):
        players_df = full_df[full_df.position != "Team"]
        players_df = players_df.dropna(axis = 1, how = 'all')
        players_df['kda'] = (players_df.k + players_df.a) / players_df.d.replace(0, 1)
        return players_df

def createFTPDf(filename):
        full_df = createFullDf(filename)
        players_df = createPlayersDf(full_df)
        team_df = createTeamDf(full_df)
        return full_df, team_df, players_df

def createGamelenDf(team_df):
        return team_df[['gamelength']][team_df.result == 1]

def createCsXpDf(players_df):
        cs_df = players_df[['position', 'csat10', 'csat15']]
        xp_df = players_df[['position','xpat10']]
        return cs_df, xp_df

def createStatsDf(players_df):
        return players_df[['result', 'position', 'dmgshare', 'earnedgoldshare', 'earnedgpm', 'wardshare', 'kda']]

def createBansDf(team_df):
        return team_df.melt(id_vars= 'gameid',value_vars=['ban1','ban2', 'ban3', 'ban4', 'ban5']).drop('variable', axis = 1).set_index('gameid').rename(columns={'value': 'bans'})

def createPickDf(players_df):
        return players_df[['result','champion', 'position']]

def createRedBlueDf(team_df):
        red_df = team_df[['result', 'epicmonsterkills', 'teamdragkills','herald', 'teambaronkills', 'elders']][team_df.side == 'Red']
        blue_df = team_df[['result', 'epicmonsterkills', 'teamdragkills','herald', 'teambaronkills', 'elders']][team_df.side == 'Blue']
        return red_df, blue_df

def createObjDf(team_df):
        drakes_df = team_df[['result','teamdragkills', 'fd','fdtime', 'firedrakes', 'waterdrakes','earthdrakes', 'airdrakes', 'elders']]
        herald_df = team_df[['result','herald', 'heraldtime']]
        baron_df = team_df[['result', 'teambaronkills', 'fbaron','fbarontime']]
        turrets_df = team_df[['result','ft', 'fttime','teamtowerkills', 'firsttothreetowers']]
        return drakes_df, herald_df, baron_df, turrets_df

def getMeanPerPos(df, column):
    top = int(np.round(df[df.position == 'Top'][column].mean()))
    jgl = int(np.round(df[df.position == 'Jungle'][column].mean()))
    mid = int(np.round(df[df.position == 'Middle'][column].mean()))
    bot = int(np.round(df[df.position == 'ADC'][column].mean()))
    sup = int(np.round(df[df.position == 'Support'][column].mean()))
    return pd.DataFrame([top,jgl,mid,bot,sup], index = ['top','jgl', 'mid', 'bot', 'sup'], columns=['Mean'])

def getMedianPerPos(df, column):
    top = int(np.round(df[df.position == 'Top'][column].median()))
    jgl = int(np.round(df[df.position == 'Jungle'][column].median()))
    mid = int(np.round(df[df.position == 'Middle'][column].median()))
    bot = int(np.round(df[df.position == 'ADC'][column].median()))
    sup = int(np.round(df[df.position == 'Support'][column].median()))
    return pd.DataFrame([top,jgl,mid,bot,sup], index = ['top','jgl', 'mid', 'bot', 'sup'], columns=['Median'])

def createChampDf(pick_df, bans_df):
    nb_games = pick_df[pick_df.result == 1].shape[0]
    champ_df = pd.read_csv('data/champions_list.csv', header = None).T.set_index(0)
    champ_df['bans'] = bans_df.bans.value_counts()
    champ_df.bans = champ_df.bans.fillna(0)
    champ_df['picks'] = pick_df.champion.value_counts()
    champ_df.picks = champ_df.picks.fillna(0)
    champ_df['wins'] = pick_df[pick_df.result == 1].champion.value_counts()
    champ_df.wins = champ_df.wins.fillna(0)
    champ_df['presence'] = champ_df.bans + champ_df.picks
    champ_df['prerate'] = np.round(champ_df.presence / nb_games * 100).astype(int)
    champ_df['banrate'] = np.round(champ_df.bans / nb_games * 100).astype(int)
    champ_df['pickrate'] = np.round(champ_df.picks / nb_games * 100).astype(int)
    champ_df['winrate'] = np.round(champ_df.wins / champ_df.picks * 100).fillna(0).astype(int)
    return champ_df

if __name__ == "__main__":
    pass