import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

#cargar dataset
df = pd.read_csv('Mall_Customers.csv')

print(df.head())

print("---------------------------------")
print(f"dimensions: {df.shape}")

#Seleccionar Clustering (Ingresos y Gastos)
X = df.iloc[:, [3, 4]].values

#Visualizar datos crudos sin agrupar
plt.figure(figsize=(10,6))
plt.scatter(X[:, 0], X[:, 1], s=50, c='gray', label='clientes')
plt.title("Distribución de cientes ")
plt.xlabel("Ingresos anuales (k$)")
plt.ylabel("Puntuación de gastos (1-100)")
plt.show()

#Lista para guardar los errores
wcss = []

#Prueba de 1 a 10 clusters
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

#Graficar resultado
plt.figure(figsize=(10,5))
plt.plot(range(1, 11), wcss, marker='o', color='red')
plt.title("El método del codo")
plt.xlabel("número de clusters (k)")
plt.ylabel("WCSS (Suma de errores cuadrados)")
plt.show()

#Crear modelos con 5 clústers
kmeans = KMeans(n_clusters=5, init="k-means++", random_state=42)
#Entrenar y, y predecir al grupo al que pertenece cada cliente
y_kmeans = kmeans.fit_predict(X)

#Visualización
plt.figure(figsize=(12,7))
#Cada cluster por separado
plt.scatter(X[y_kmeans==0, 0], X[y_kmeans==0, 1], s=100, c='red', label='cluster 1')
plt.scatter(X[y_kmeans==1, 0], X[y_kmeans==1, 1], s=100, c='blue', label='cluster 2')
plt.scatter(X[y_kmeans==2, 0], X[y_kmeans==2, 1], s=100, c='green', label='cluster 3')
plt.scatter(X[y_kmeans==3, 0], X[y_kmeans==3, 1], s=100, c='yellow', label='cluster 4')
plt.scatter(X[y_kmeans==4, 0], X[y_kmeans==4, 1], s=100, c='magenta', label='cluster 5')
#pintar centroides (cliente promedio de cada grupo)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c="cyan", label='Centroides')

plt.title("Segmentación de clientes (k-means)")
plt.xlabel("Ingresos anuales (k$")
plt.ylabel("Puntuación de gastos (1-100)")
plt.legend()
plt.show()

#Asignamos el cluster a cada cliente en el dataset original
df['cluster_IA'] = y_kmeans

#Explorar la base de datos "actualizada"
df.to_csv('Mall_Customers_IA.csv', index=False)

print("Éxito! Archivo 'Mall_Customers_IA.csv' guardado.")
print(df.head())