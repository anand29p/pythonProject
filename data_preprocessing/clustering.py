import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from kneed import KneeLocator # pip install kneed
from model.ml_model import Model
class KMeansClustering():
    def __init__(self, file_object, logger):
        self.file_object = file_object
        self.logger = logger

    def elbow_plot(self, data):
        self.logger.log(self.file_object, 'Entered the elbow_plot method of the KMeansClustering class')
        wcss = []  # initializing an empty list
        try:
            for i in range(1, 11):
                kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)  # initializing the KMeans object
                kmeans.fit(data)  # fitting the data to the KMeans Algorithm
                wcss.append(kmeans.inertia_)
            plt.plot(range(1, 11), wcss)  # creating the graph between WCSS and the number of clusters
            plt.title('The Elbow Method')
            plt.xlabel('Number of clusters')
            plt.ylabel('WCSS')
            # plt.show()
            plt.savefig('preprocessing_data/K-Means_Elbow.PNG')  # saving the elbow plot locally
            # finding the value of the optimum cluster programmatically
            self.kn = KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')
            self.logger.log(self.file_object, 'The optimum number of clusters is: ' + str(self.kn.knee) + ' . Exited the elbow_plot method of the KMeansClustering class')
            return self.kn.knee

        except Exception as e:
            self.logger.log(self.file_object, 'Exception occured in elbow_plot method of the KMeansClustering class. Exception message:  ' + str(e))
            self.logger.log(self.file_object, 'Finding the number of clusters failed. Exited the elbow_plot method of the KMeansClustering class')
            raise Exception()

    def create_clusters(self, data, number_of_clusters):
        self.logger.log(self.file_object, 'Entered the create_clusters method of the KMeansClustering class')
        self.data = data
        try:
            self.kmeans = KMeans(n_clusters=number_of_clusters, init='k-means++', random_state=42)
            self.y_kmeans = self.kmeans.fit_predict(data)  # divide data into clusters
            # Saving Model
            self.model_obj = Model(self.file_object, self.logger)
            self.save_model = self.model_obj.save_model(self.kmeans, 'KMeans')  # saving the KMeans model to directory
            # passing 'Model' as the functions need three parameters
            # add a new column in data
            self.data['Cluster'] = self.y_kmeans  # create a new column in dataset for storing the cluster information
            self.logger.log(self.file_object, 'successfully created ' + str(self.kn.knee) + 'clusters. Exited the create_clusters method of the KMeansClustering class')
            return self.data
        except Exception as e:
            self.logger.log(self.file_object, 'Exception occured in create_clusters method of the KMeansClustering class. Exception message:  ' + str(e))
            self.logger.log(self.file_object, 'Fitting the data to clusters failed. Exited the create_clusters method of the KMeansClustering class')
            raise Exception()

