import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def Algo(row):
    score = (1.35 * row['PTS'] +
             0.6 * row['TRB'] +
             0.9 * row["AST"] +
             0.9 * row["STL"] +
             0.9 * row["BLK"] -
             0.5 * row['FG%'] -
             0.35 * row['FT%'] -
             0.25 * row['TOV'])
    
    score /= row['G']
    
    return score


stats['Player_Score'] = stats.apply(Algo, axis = 1)
    
stats = stats[stats['Player_Score'] >= 0]
stats = stats.drop_duplicates(subset=['Year', 'Player'], keep='first')


stats

lebron_stats = stats[stats['Player'] == 'LeBron James']
lebron_stats

rose_stats = stats[stats['Player'] == 'Derrick Rose']
rose_stats

paul_stats = stats[stats['Player'] == 'Chris Paul']
paul_stats

lopez_stats = stats[stats['Player'] == 'Brook Lopez']
lopez_stats

horford_stats = stats[stats['Player'] == 'Al Horford']
horford_stats


def sep_algo(row):
    f = (1.35 * row['PTS'] +
         0.6 * row['TRB'] +
         0.9 * row["AST"] +
         0.9 * row["STL"] +
         0.9 * row["BLK"] -
         0.5 * row['FG%'] -
         0.35 * row['FT%'] -
         0.25 * row['TOV'])
    return f

stats['Overall_Score'] = stats.apply(sep_algo, axis=1)

stats = stats[stats['Overall_Score'] >= 0]

stats = stats.drop_duplicates(subset=['Year', 'Player'], keep='first')


def analyze_performance(injury_df, stats_df, injury_type):
    avg_scores_before = []
    avg_scores_after = []

    for index, injury in injury_df.iterrows():
        player_name = injury['Relinquished']  
        injury_date = pd.to_datetime(injury['Date'])

        player_stats = stats_df[stats_df['Player'] == player_name]
        before_injury = player_stats[player_stats['Year'] < injury_date]
        after_injury = player_stats[player_stats['Year'] > injury_date]

        if not before_injury.empty:
            avg_scores_before.append(before_injury['Overall_Score'].mean())
        if not after_injury.empty:
            avg_scores_after.append(after_injury['Overall_Score'].mean())

    overall_avg_before = sum(avg_scores_before) / len(avg_scores_before) if avg_scores_before else 0
    overall_avg_after = sum(avg_scores_after) / len(avg_scores_after) if avg_scores_after else 0

    print(f"Average player score before {injury_type} injuries: {overall_avg_before:.2f}")
    print(f"Average player score after {injury_type} injuries: {overall_avg_after:.2f}")
    print(f"Change in performance due to {injury_type} injury: {(overall_avg_after - overall_avg_before):.2f}\n")

analyze_performance(achilles_df, stats, 'Achilles')
analyze_performance(full_hand, stats, 'Hand/Finger')
analyze_performance(acl_df, stats, 'ACL')
analyze_performance(concussion, stats, 'Concussion')
