from application_logging.logger import App_Logger
from data_ingestion.dataLoader import Data_Getter
from data_preprocessing.preprocessing import Preprocessor


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
            if cols_to_drop:
                X = preprocessor.remove_columns(X, cols_to_drop)

        except Exception:
            # logging the unsuccessful Training
            self.logger.log(self.file_object, 'Unsuccessful End of Training')
            self.file_object.close()
            raise Exception