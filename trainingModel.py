from application_logging.logger import App_Logger
from data_ingestion.dataLoader import Data_Getter
from data_preprocessing.clustering import KMeansClustering
from data_preprocessing.preprocessing import Preprocessor
from sklearn.model_selection import train_test_split

class trainModel:
    def __init__(self):
        self.logger = App_Logger()
        self.file_object = open("Training_Logs/ModelTrainingLog.txt", 'a+')

    def trainingModel(self):
        # Logging the start of Training
        self.logger.log(self.file_object, 'Start of Training')
        try:
            # Getting the data from the source
            data_getter = Data_Getter(self.file_object, self.logger)
            data = data_getter.get_data()
#########################################################################################################
            # doing the data preprocessing
            preprocessor = Preprocessor(self.file_object, self.logger)
            data = preprocessor.remove_columns(data, ['Wafer'])  # remove the unnamed column as it doesn't contribute to prediction.

            # create separate features and labels
            X, Y = preprocessor.separate_label_feature(data, label_column_name='Output')

            # check if missing values are present in the dataset
            is_null_present = preprocessor.is_null_present(X)

            # if missing values are there, replace them appropriately.
            if (is_null_present):
                X = preprocessor.impute_missing_values(X)  # missing value imputation
#####################################################################################################
            # check further which columns do not contribute to predictions
            # if the standard deviation for a column is zero, it means that the column has constant values
            cols_to_drop = preprocessor.get_columns_with_zero_std_deviation(X)
            # drop the columns obtained above
            # Major change
            if cols_to_drop:
                X = preprocessor.remove_columns(X, cols_to_drop)
######################################################################################################
            """ Applying the clustering approach"""

            kmeans = KMeansClustering(self.file_object, self.logger)  # object initialization.
            number_of_clusters = kmeans.elbow_plot(X)  #  using the elbow plot to find the number of optimum clusters

            # Divide the data into clusters
            X = kmeans.create_clusters(X, number_of_clusters)

            # create a new column in the dataset consisting of the corresponding cluster assignments.
            X['Labels'] = Y

            # getting the unique clusters from our dataset
            list_of_clusters = X['Cluster'].unique()

            """parsing all the clusters and looking for the best ML algorithm to fit on individual cluster"""
            for i in list_of_clusters:
                cluster_data = X[X['Cluster'] == i]  # filter the data for one cluster

                # Prepare the feature and Label columns
                cluster_features = cluster_data.drop(['Labels', 'Cluster'], axis=1) #drop Labels and cluster columns
                cluster_label = cluster_data['Labels']

                # splitting the data into training and test set for each cluster one by one
                x_train, x_test, y_train, y_test = train_test_split(cluster_features, cluster_label, test_size=1 / 3, random_state=355)



        except Exception:
            # logging the unsuccessful Training
            self.logger.log(self.file_object, 'Unsuccessful End of Training')
            self.file_object.close()
            raise Exception