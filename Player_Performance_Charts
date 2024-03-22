import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

stats.loc[:, 'Year'] = pd.to_datetime(stats['Year'], format='%Y')

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

    return overall_avg_before, overall_avg_after

achilles_before, achilles_after = analyze_performance(achilles_df, stats, 'Achilles')
hand_before, hand_after = analyze_performance(full_hand, stats, 'Hand/Finger')
acl_before, acl_after = analyze_performance(acl_df, stats, 'ACL')
conc_before, conc_after = analyze_performance(concussion, stats, 'Concussion')


injury_types = ['Achilles', 'Hand/Finger', 'ACL', 'Concussion']
before_scores = [achilles_before, hand_before, acl_before, conc_before ]
after_scores = [achilles_after, hand_after, acl_after, conc_after]

plt.figure(figsize=(10, 6))
plt.bar(injury_types, before_scores, color='#FFB81C', label='Before Injury')
plt.bar(injury_types, after_scores, color='#154734', label='After Injury', alpha=0.7)
plt.xlabel('Injury Type')
plt.ylabel('Average Player Score')
plt.title('Average Player Scores Before and After Injury')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))

# Plot bars for before and after scores
plt.bar(injury_types, before_scores, color='#FFB81C', label='Before Injury')
plt.bar(injury_types, after_scores, color='#154734', label='After Injury', alpha=0.7)

# Add labels to the bars
for i in range(len(injury_types)):
    plt.text(i, before_scores[i] + 0.2, f'{before_scores[i]:.2f}', ha='center', va='bottom', color='black')
    plt.text(i, after_scores[i] - 0.8, f'{after_scores[i]:.2f}', ha='center', va='bottom', color='white')


# Add titles and legend
plt.xlabel('Injury Type')
plt.ylabel('Average Player Score')
plt.title('Average Player Scores Before and After Injury')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))  

plt.plot(rose_stats['Year'], rose_stats['Player_Score'], marker='o', linestyle='-', color='r', label='Derrick Rose')


plt.axvline(x=2013, color='k', linestyle='--', label='ACL Tear (2013)')

plt.title('Derrick Rose Player Score Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12) 
plt.ylabel('Player Score', fontsize=12)  
plt.xticks(fontsize=10) 
plt.yticks(fontsize=10)  
plt.grid(True) 

plt.legend(loc='upper right', fontsize=12)


plt.tight_layout()  
plt.show()

plt.figure(figsize=(10, 6))  

plt.plot(paul_stats['Year'], paul_stats['Player_Score'], marker='o', linestyle='-', color='g', label='Chris Paul')

plt.axvline(x=2012, color='k', linestyle='--', label='Hand Injury (2012)')
plt.axvline(x=2014, color='k', linestyle='--', label='Hand Injury (2014)')

plt.title('Chris Paul Player Score Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Player Score', fontsize=12) 
plt.xticks(fontsize=10) 
plt.yticks(fontsize=10) 
plt.grid(True)  

plt.legend(loc='upper right', fontsize=12)

plt.tight_layout()  
plt.show()

plt.figure(figsize=(10, 6))  

plt.plot(horford_stats['Year'], horford_stats['Player_Score'], marker='o', linestyle='-', color='black', label='Al Horford')

plt.axvline(x=2014, color='k', linestyle='--', label='Concussion (2014)')

plt.title('Al Horford Player Score Over Time', fontsize=16, fontweight='bold') 
plt.xlabel('Year', fontsize=12) 
plt.ylabel('Player Score', fontsize=12) 
plt.xticks(fontsize=10) 
plt.yticks(fontsize=10)  
plt.grid(True)  

plt.legend(loc='upper right', fontsize=12)

plt.tight_layout()  
plt.show()

plt.figure(figsize=(10, 6)) 

plt.plot(lopez_stats['Year'], lopez_stats['Player_Score'], marker='o', linestyle='-', color='yellow', label='Brook Lopez')


plt.axvline(x=2013, color='k', linestyle='--', label='Achilles Injury (2013)')

plt.title('Brook Lopez Player Score Over Time', fontsize=16, fontweight='bold') 
plt.xlabel('Year', fontsize=12) 
plt.ylabel('Player Score', fontsize=12) 
plt.xticks(fontsize=10)  
plt.yticks(fontsize=10) 
plt.grid(True)  

plt.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.show()
