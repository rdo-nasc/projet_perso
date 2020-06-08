import pandas as pd
import numpy as np
import data_prep as data
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, metavar='filename')
args = parser.parse_args()
filename = args.filename

full_df, team_df, players_df = data.createFTPDf(filename)

def vizGamelen(team_df):
    df = data.createGamelenDf(team_df)
    cell_text = [[str(np.round(x)) for x in df.gamelength.describe().values]]
    columns = df.gamelength.describe().index.values
    plt.table(cellText=cell_text,
                      colLabels=columns,
                      loc='bottom')
    plt.grid(True)
    plt.boxplot(df.gamelength, showmeans=True)
    plt.title('Longueur des parties')
    plt.show()

def showPerPosStats(df, column, title='', flag='Median'):
    if flag == 'Median':
        ax = data.getMedianPerPos(df, column).plot.bar(rot=0, title=title)
    else:
        ax = data.getMeanPerPos(df, column).plot.bar(rot=0, title=title)
    plt.show()

def vizStats(players_df):
    cs_df,xp_df = data.createCsXpDf(players_df)
    stats_df = data.createStatsDf(players_df)
    showPerPosStats(cs_df, 'csat15', 'Mediane de cs a 15 minutes par position (cs)')
    showPerPosStats(xp_df, 'xpat10', "Mediane de l'expérience a 10 minutes par position(xp)")
    showPerPosStats(stats_df, 'kda', "Mediane du kda par position")
    showPerPosStats(stats_df, 'dmgshare', "Mediane de la répartition des dégats par position(%)")
    showPerPosStats(stats_df, 'earnedgoldshare', "Mediane de la répartition de l'or par position(%)")

def getChampsPie(df, title):
    ax= df[df.picks > 0].prerate.sort_values(ascending = False)[:10].plot.bar(rot=90)
    plt.title(title + ' Prescence Rate')
    plt.show()
    ax = df[df.picks > 0].pickrate.sort_values(ascending = False)[:10].plot.bar(rot=90)
    plt.title(title + ' Pick Rate')
    plt.show()
    ax =df[df.picks >= 5].winrate.sort_values(ascending = False)[:10].plot.bar(rot=90)
    plt.title(title + ' Win Rate')
    plt.show()

def vizChamps(players_df, team_df):
    pick_df = data.createPickDf(players_df)
    bans_df = data.createBansDf(team_df)
    top_df, jgl_df, mid_df, bot_df, sup_df = [data.createChampDf(pick_df[pick_df.position == x], bans_df) for x in ['Top','Jungle', 'Middle', 'ADC', 'Support']]
    ax = top_df.banrate.sort_values(ascending = False)[:15].plot.bar(rot=90)
    plt.title('Ban Rate')
    plt.show()
    getChampsPie(top_df, 'Top')
    getChampsPie(jgl_df, 'Jgl')
    getChampsPie(mid_df, 'Mid')
    getChampsPie(bot_df, 'Bot')
    getChampsPie(sup_df, 'Sup')
    
def vizSides(team_df):
    red_df, blue_df = data.createRedBlueDf(team_df)
    ax = red_df.describe()[1:].plot.bar(rot=90)
    plt.title('Red Side')
    plt.show()
    ax = blue_df.describe()[1:].plot.bar(rot=90)
    plt.title('Blue Side')
    plt.show()

def getDrakeWinrate(drakes_df, col):
    res = {}
    for i in range(4):
        rate = drakes_df[(drakes_df[col] == i) & (drakes_df.result == 1)].shape[0] / drakes_df[(drakes_df[col] == i)].shape[0] * 100
        res[col + "_" + str(i)] = (np.round(rate), drakes_df[(drakes_df[col] == i) & (drakes_df.result == 1)].shape[0])
    return pd.DataFrame(res).T.rename(columns={0: "Winrate", 1: "Effectif"})

def getBaronWinrate(baron_df):
    res = {}
    for i in range(3):
        rate = np.round(baron_df[(baron_df.result == 1) & (baron_df.teambaronkills == i)].shape[0] / baron_df[(baron_df.teambaronkills == i)].shape[0] *100)
        res["baron_" + str(i)] = (rate, baron_df[(baron_df.result == 1) & (baron_df.teambaronkills == i)].shape[0])
    return pd.DataFrame(res).T.rename(columns={0: "Winrate", 1: "Effectif"})

def getTurretWinrate(df):
    res = {}
    for i in range(5, 12):
        rate = np.round(df[(df.result == 1) & (df.teamtowerkills == i)].shape[0] / df[df.teamtowerkills == i].shape[0] *100)
        res["Turrets_" + str(i)] = (rate, df[(df.result == 1) & (df.teamtowerkills == i)].shape[0])
    return pd.DataFrame(res).T.rename(columns={0: "Winrate", 1: "Effectif"})

def vizObj(team_df):
    drakes_df, herald_df, baron_df, turrets_df = data.createObjDf(team_df)
    df = getDrakeWinrate(drakes_df, 'teamdragkills')
    ax = df.plot.bar(rot=0)
    plt.title('Winrate by number of dragons taken')
    plt.show()
    df = getBaronWinrate(baron_df)
    ax = df.plot.bar(rot=0)
    plt.title('Winrate by number of Baron taken')
    plt.show()
    df = getTurretWinrate(turrets_df)
    ax = df.plot.bar(rot=0)
    plt.title('Winrate by number of turrets taken')
    plt.show()

vizGamelen(team_df)
vizStats(players_df)
vizChamps(players_df, team_df)
vizSides(team_df)
vizObj(team_df)
