import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

combined_data = pd.merge(stats, injury, left_on='Player', right_on='Relinquished', how='left')

combined_data = pd.merge(combined_data, full_hand, on=['Date', 'Acquired', 'Relinquished', 'Notes'], how='inner')

relevant_columns = ['Player', 'Age', 'G', 'MP', 'FG%', '3P%', 'FT%', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PTS', 'Player_Score', 'Date', 'Acquired', 'Relinquished', 'Notes']
combined_data = combined_data[relevant_columns]

combined_data['Injury'] = pd.notna(combined_data['Acquired']).astype(int)


print(combined_data.head())

data = combined_data

label_encoder_player = LabelEncoder()
label_encoder_notes = LabelEncoder()

data['Player'] = label_encoder_player.fit_transform(data['Player'])
data['Notes'] = label_encoder_notes.fit_transform(data['Notes'])

X = data[['Player', 'Player_Score']]
y = data['Notes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=100000000)

nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

y_pred = nb_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

