
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Load dataset
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# Select numerical features
X = df[['QUANTITYORDERED', 'PRICEEACH', 'SALES',
        'MSRP', 'QTR_ID', 'MONTH_ID']]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method
wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, random_state=42, n_init=10)
    km.fit(X_scaled)
    wcss.append(km.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method')
plt.show()

# K-Means Clustering (assume optimal k = 3)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['KMeans_Cluster'] = kmeans.fit_predict(X_scaled)

# Hierarchical Clustering
plt.figure(figsize=(10, 5))
Z = linkage(X_scaled[:100], method='ward')
dendrogram(Z)
plt.title('Hierarchical Clustering Dendrogram')
plt.show()

hc = AgglomerativeClustering(n_clusters=3, linkage='ward')
df['Hierarchical_Cluster'] = hc.fit_predict(X_scaled)

# Display results
print(df[['KMeans_Cluster', 'Hierarchical_Cluster']].head())
