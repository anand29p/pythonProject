from application_logging.logger import App_Logger
from data_ingestion.dataLoader import Data_Getter


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

        except Exception:
            # logging the unsuccessful Training
            self.logger.log(self.file_object, 'Unsuccessful End of Training')
            self.file_object.close()
            raise Exception