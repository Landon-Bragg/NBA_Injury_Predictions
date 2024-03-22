import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# Ensure labels are encoded properly
label_encoder_player = LabelEncoder()
label_encoder_notes = LabelEncoder()

data['Player'] = label_encoder_player.fit_transform(data['Player'])
data['Notes'] = label_encoder_notes.fit_transform(data['Notes'])

X = data[['Player', 'Player_Score']]
y = data['Notes']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=100000000)

# Train Gaussian Naive Bayes classifier
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = nb_classifier.predict(X_test)

# Ensure y_test and y_pred have the same set of unique labels
unique_labels = np.unique(np.concatenate((y_test, y_pred)))
y_test_filtered = y_test[y_test.isin(unique_labels)]
y_pred_filtered = y_pred[y_test.isin(unique_labels)]

# Create confusion matrix
conf_matrix = confusion_matrix(y_test_filtered, y_pred_filtered, labels=unique_labels)

# Slice unique labels array to include only every 13th label
unique_labels_sliced = unique_labels[::13]

# Slice confusion matrix to include every 13th row and column, as well as values within 6 blocks away
conf_matrix_sliced = conf_matrix[::13, ::13]
for i in range(len(conf_matrix_sliced)):
    for j in range(len(conf_matrix_sliced)):
        start_row = i * 13
        start_col = j * 13
        end_row = min(start_row + 13, len(conf_matrix))
        end_col = min(start_col + 13, len(conf_matrix))
        conf_matrix_sliced[i, j] = np.sum(conf_matrix[start_row:end_row, start_col:end_col])

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_sliced, annot=True, cmap='Greens', fmt='g', xticklabels=unique_labels_sliced, yticklabels=unique_labels_sliced)
plt.xlabel('Prediction')
plt.ylabel('Truth')
plt.title('Confusion Matrix (Every 13th Label with Adjacent Blocks within 6 Blocks)')
plt.show()
