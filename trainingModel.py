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

        except Exception:
            # logging the unsuccessful Training
            self.logger.log(self.file_object, 'Unsuccessful End of Training')
            self.file_object.close()
            raise Exception