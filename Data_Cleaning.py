import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

injury = pd.read_csv('Data/Injury.csv')

index_names = injury[injury['Date'] > '2018-06-18'].index
injury.drop(index_names, inplace=True)
injury = injury.drop(columns = ['Unnamed: 0', 'Team'])

injury

stats = pd.read_csv('Data/Stats.csv')

index_names = stats[stats['Year'] < 2010].index
stats.drop(index_names, inplace=True)

stats = stats.drop(columns = ['Unnamed: 0', 'Season', 'Pos', 'Tm', 'GS', 'FG', 'FGA', '3P', '3PA', '2P', 
                              '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'ORB', 'DRB', 'PF'])

stats = stats.fillna(0)

stats

# Looking at all achilles injuries
achilles = injury['Notes'].str.contains('achilles', case=False)

achilles_df = injury[achilles]

achilles_df.head()

# Looking at all hand injuries

hand = injury['Notes'].str.contains('hand', case=False)
finger = injury['Notes'].str.contains('finger', case = False)

hand_df = injury[hand]
finger_df = injury[finger]

full_hand = pd.concat([hand_df, finger_df], axis = 0)

full_hand

# Looking at all ACL injuries

acl = injury['Notes'].str.contains('acl', case=False)

acl_df = injury[acl]

acl_df.head()

# Looking at all Concussions

concussion = injury['Notes'].str.contains('concussion', case=False)

concussion = injury[concussion]

concussion.head()

