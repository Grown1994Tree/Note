from sklearn.cluster import KMeans

def k_means(feature_matrix, num_clusters=10):
    km = KMeans(n_clusters=num_clusters, max_iter=10000)
    km.fit(feature_matrix)
    clusters = km.labels_
    
    return km, clusters

num_clusters = 10
km_obj, clusters = k_means(feature_matrix=feature_matrix, num_clusters=num_clusters)
book_data['Cluster'] = clusters

book_data.head()
