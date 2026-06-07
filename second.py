import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Character Wiinrates

dataFrameCharacters = pd.read_csv('input/characters.csv')
characters = dataFrameCharacters['Character'].tolist()
winrates = dataFrameCharacters['Win Rate'].tolist()

plt.bar(characters, winrates, color=['red','green','orange','purple','blue','black'])
plt.xlabel('Character')
plt.ylabel('Win Rate')
plt.title('Win Rates by Character')
plt.show()

#Act Death-Rates

dataFrameMonsters = pd.read_csv('input/encounters.csv')
monsterAct = dataFrameMonsters['Act'].tolist()
monsterLethality = dataFrameMonsters['Times Killed Player'].tolist()

avgKillsPerAct = dataFrameMonsters.groupby('Act')['Times Killed Player'].mean()
avgKillsPerAct = avgKillsPerAct.sort_index(ascending=False)

plt.bar(avgKillsPerAct.index, avgKillsPerAct.values, color=['blue','green','#C58F00','grey'])
plt.xlabel('Acts')
plt.ylabel('Avg Deaths')
plt.title('Avg Deaths by Act')
plt.show()

#Badges

dataFrameBadges = pd.read_csv('input/badges.csv')

badgeNames = dataFrameBadges['Badge'].tolist()
badgeBronze = dataFrameBadges['Bronze'].tolist()
badgeSilver = dataFrameBadges['Silver'].tolist()
badgeGold = dataFrameBadges['Gold'].tolist()

x = np.arange(len(badgeNames))  # evenly spaced positions                   # width of each bar

plt.bar(x - 0.25, badgeBronze, 0.25, color='#CD7F32', label='Bronze')
plt.bar(x, badgeSilver, 0.25, color='#C0C0C0', label='Silver')
plt.bar(x + 0.25, badgeGold, 0.25, color='#FFD700', label='Gold')

plt.xticks(x, badgeNames, rotation=45)
plt.xlabel('Badge')
plt.ylabel('Count')
plt.title('Badge Tiers')
plt.legend()
plt.tight_layout()
plt.show()
