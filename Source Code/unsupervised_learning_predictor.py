"""
-----------------------------------------------------------------------------------------
THE SPARKS FOUNDATION - DATA SCIENCE AND BUSINESS ANALYTICS INTERNSHIP (GRIP JULY 2021)
-----------------------------------------------------------------------------------------
TASK 2: PREDICTION USING UNSUPERVISED MACHINE LEARNING
GOAL: From the given 'Iris' dataset, predict the optimum number of clusters and represent it visually.
MODEL: KMeans Clustering (Unsupervised Learning).

AUTHORS:
- Amey Thakur (https://github.com/Amey-Thakur)
- Mega Satish (https://github.com/msatmod)

REPOSITORY: https://github.com/Amey-Thakur/TSF-UNSUPERVISED-MACHINE-LEARNING

DESCRIPTION:
This scholarly implementation demonstrates the application of unsupervised machine learning 
heuristics, specifically KMeans Clustering, to partition the classical Iris dataset. 
The analysis involves data ingestion, exploratory variance analysis using the 'Elbow Method', 
centroid optimization, and a high-fidelity visual representation of the derived clusters.

TECHNOLOGIES: Python 3, Scikit-learn, Pandas, NumPy, Matplotlib.
DATA SOURCE: Iris.csv
-----------------------------------------------------------------------------------------
"""

# =========================================================================================
# STEP 1: IMPORTING ESSENTIAL SCHOLARLY LIBRARIES
# =========================================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Facilitating inline plotting and aesthetic consistency
plt.style.use('ggplot')

def main():
    """
    Main execution pipeline for the Unsupervised Learning Task.
    """

    # =====================================================================================
    # STEP 2: DATA ACQUISITION AND INITIAL EXPLORATION
    # =====================================================================================
    dataset_path = "Iris.csv"
    try:
        data = pd.read_csv(dataset_path)
        print("[INFO] Dataset successfully loaded from '{}'.".format(dataset_path))
    except FileNotFoundError:
        print("[ERROR] 'Iris.csv' not found. Please ensure it is in the correct directory.")
        return

    # Structural overview of the empirical data
    print("\n--- Structural Overview ---")
    print("Dataset Shape: {}".format(data.shape))
    print(data.head())

    # =====================================================================================
    # STEP 3: FEATURE EXTRACTION AND CLUSTER OPTIMIZATION (ELBOW METHOD)
    # =====================================================================================
    # Selecting the relevant features (SepalLength, SepalWidth, PetalLength, PetalWidth)
    # We omit the Index and Species columns for the clustering process
    x = data.iloc[:, [1, 2, 3, 4]].values

    # Calculating Within-Cluster Sum of Squares (WCSS) for range of cluster counts
    wcss = []
    print("\n[INFO] Calculating WCSS for cluster optimization...")
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=10)
        kmeans.fit(x)
        wcss.append(kmeans.inertia_)

    # Plotting the Elbow Curve to determine the optimal K
    print("[V] Generating Elbow Method visualization...")
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 11), wcss, marker='o', color='blue')
    plt.title('The Elbow Method: Optimal K Determination')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
    plt.grid(True)
    plt.show()

    # Observation: The 'elbow' occurs at K=3
    print("[RESULT] The Elbow Method identifies K=3 as the optimal number of clusters.")

    # =====================================================================================
    # STEP 4: MODEL TRAINING AND CLASSIFICATION
    # =====================================================================================
    # Initializing the KMeans classifier with optimized parameters
    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=10)
    
    # Executing the clustering algorithm on the feature space
    y_kmeans = kmeans.fit_predict(x)
    print("[INFO] KMeans model training and cluster assignment complete.")

    # =====================================================================================
    # STEP 5: SCHOLARLY VISUALIZATION OF CLUSTER PARTITIONING
    # =====================================================================================
    print("[V] Generating final cluster visualization...")
    plt.figure(figsize=(10, 8))

    # Plotting the observations categorized by cluster
    plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s=100, c='blue', label='Iris-setosa')
    plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s=100, c='green', label='Iris-versicolor')
    plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s=100, c='yellow', label='Iris-virginica')

    # Mapping the centroids for each cluster
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
                s=200, c='red', marker='X', label='Centroids')

    plt.title('Iris Dataset Clustering: Centroid Mapping & Spatial Partitioning')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
