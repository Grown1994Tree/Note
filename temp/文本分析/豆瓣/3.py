def get_cluster_data(clustering_obj, book_data, feature_names, num_clusters, topn_features=10):
    cluster_details = {}
    # 获取cluster的center
    ordered_centroids = clustering_obj.cluster_centers_.argsort()[:, ::-1]
    # 获取每个cluster的关键特征
    # 获取每个cluster的书
    for cluster_num in range(num_clusters):
        cluster_details[cluster_num] = {}
        cluster_details[cluster_num]['cluster_num'] = cluster_num
        key_features = [feature_names[index]
                        for index
                        in ordered_centroids[cluster_num, :topn_features]]
        cluster_details[cluster_num]['key_features'] = key_features
        books = book_data[book_data['Cluster'] == cluster_num]['title'].values.tolist()
        cluster_details[cluster_num]['books'] = books
    
    return cluster_details


def print_cluster_data(cluster_data):
    for cluster_num, cluster_details in cluster_data.items():
        print('Cluster {} details: '.format(cluster_num))
        print('-' * 20)
        print('Key features: ', cluster_details['key_features'])
        print('Book in this cluster: ')
        print(', '.join(cluster_details['books']))
        print('=' * 40)
