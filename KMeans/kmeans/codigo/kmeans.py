'''
Integrantes:
- Amauri Pietropaolo
- Arthur Resende
- Heitor Freitas
- Pedro Leale
- Rafael Azambuja
'''

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from kneed import KneeLocator

data = pd.read_csv('dataset/IRIS.csv')

x = data.iloc[:, [0, 1, 2, 3]].values

sse = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters= i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(x)
    sse.append(kmeans.inertia_)

plt.plot(range(1, 11), sse)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.show()

# Find elbow point using KneeLocator
# This method is used to find the elbow point in the graph, wich is the point where the SSE starts to decrease in a linear fashion
kl = KneeLocator(range(1, 11), sse, curve="convex", direction="decreasing")

kmeans = KMeans(n_clusters=kl.elbow, 
                init='k-means++', 
                max_iter=300, 
                n_init=10, 
                random_state=42) 
y_kmeans = kmeans.fit_predict(x)

sse.append(kmeans.inertia_)
print(sse)

# Visualising the clusters
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 50, c = 'cyan', label = 'Setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 50, c = 'blue', label = 'Versicolor')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 50, c = 'gray', label = 'Virginica')

#Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 50, c = 'red', label = 'Centroides')
plt.legend()
plt.show()

ground_truth = pd.crosstab(index=data["species"],
                              columns="count")      
print(ground_truth)

result = pd.crosstab(data["species"], y_kmeans)
print(result)