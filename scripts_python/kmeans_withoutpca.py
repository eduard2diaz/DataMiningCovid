import pandas as pd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np

def purity_score(y_true, y_pred):
    # compute contingency matrix (also called confusion matrix)
    contingency_matrix = metrics.cluster.contingency_matrix(y_true, y_pred)
    print("Matriz de contingencia")
    print(contingency_matrix)
    numerador=np.sum(np.amax(contingency_matrix, axis=0))
    denominador=np.sum(contingency_matrix)
    return numerador / denominador


dataset = pd.read_csv('../Data/data.csv')
features = dataset.iloc[:, 0:30]
target = dataset.iloc[:, -1]
columnas=features.columns
descripcion=features.describe()
#PCA
#dicha funcion scale lo que hace es centrar y escalar los datos
scaled_data=preprocessing.scale(features)

"""
#Analizamos la cantidad de cluster a partir de la informacion obtenida de la relacion lineal del pca
#Aplico el metodo del codo sobre el conjunto de datos
wcss = []
for i in range(1, 7):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 7), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
"""

#Aplico k-means sobre el conjunto brindado por pca
kmeans = KMeans(n_clusters = 2, init = 'k-means++',max_iter=30,n_init=10,random_state=1)
y_kmeans = kmeans.fit_predict(scaled_data)
initial_centroids=kmeans.cluster_centers_
etiquetas=kmeans.labels_

"""
print("Centroides iniciales")
initial_centroids_desnormalize=[]
for instance in initial_centroids:
    print(instance)
"""

silhouette_avg = metrics.silhouette_score(scaled_data, y_kmeans)
print ('El coeficiente de silueta del agrupamiento es = ', silhouette_avg)
purity = purity_score(target, y_kmeans)
print ('Pureza del clustering realizado = ', purity)

#Planteamos los datos como la relacion lineal de solamente dos componentes
modelo_pca = PCA(n_components = 2)
dataset_questions_pca = modelo_pca.fit(scaled_data)
pca=modelo_pca.transform(scaled_data)
centroides_pca=modelo_pca.transform(initial_centroids)
colores=['blue','red']
colores_cluster=[colores[etiquetas[i]] for i in range(len(pca))]

plt.scatter(pca[:,0],pca[:,1],c=colores_cluster,marker='o',alpha=0.4)
plt.scatter(centroides_pca[:,0],centroides_pca[:,1],marker='x',s=100,linewidths=3,c=colores)

xvector=modelo_pca.components_[0]*max(pca[:,0])
yvector=modelo_pca.components_[1]*max(pca[:,1])
plt.show()
