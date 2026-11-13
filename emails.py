
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv('emails.csv')

# Preprocessing
df = df.drop_duplicates()
df = df.dropna()

# Separate features and target
X = df.drop(['Email No.', 'Prediction'], axis=1)
y = df['Prediction']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# KNN Model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

# SVM Model
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)

# Performance evaluation
print("KNN Accuracy:", accuracy_score(y_test, knn_pred))
print("SVM Accuracy:", accuracy_score(y_test, svm_pred))

print("KNN Confusion Matrix:\n", confusion_matrix(y_test, knn_pred))
print("SVM Confusion Matrix:\n", confusion_matrix(y_test, svm_pred))

print("KNN Report:\n", classification_report(y_test, knn_pred))
print("SVM Report:\n", classification_report(y_test, svm_pred))
