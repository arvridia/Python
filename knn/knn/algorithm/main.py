import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Load the data
data = pd.read_csv('knn/datasets/diabetes.csv')
# Calculate the correlation matrix
correlation_matrix = data.corr()

# Select features with correlation above a threshold
threshold = 0.2  # Adjust as needed
relevant_features = correlation_matrix[abs(correlation_matrix['Outcome']) > threshold].index.tolist()
relevant_features.remove('Outcome')  # Remove the target variable
print("Selected features:", relevant_features)

# Separate the features and the target variable
y = data['Outcome']
X = data[relevant_features]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, train_size=0.7, random_state=42)

# Feature Scaling
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Experiment with different number of neighbors
number_of_neighbors = 14
clf = KNeighborsClassifier(n_neighbors=number_of_neighbors, weights='distance')

# Fit the model
clf.fit(X_train_scaled, y_train)

# Make predictions
y_pred = clf.predict(X_test_scaled)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Cross-validation
cv_accuracy = cross_val_score(clf, X_train_scaled, y_train, cv=5, scoring='accuracy').mean()
print(f"Cross-validated Accuracy: {cv_accuracy}")

# Criar a matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão:")
print(conf_matrix)

print(classification_report(y_test, y_pred))