from application_logging.logger import App_Logger
from Raw_Data_Validation.rawValidation import Raw_Data_Validation

class data_validation:
    def __init__(self,batch_files_loc, main_log):
        self.file_object = open(main_log, 'a+')
        self.logger = App_Logger()
        self.rawdata = Raw_Data_Validation(batch_files_loc)

    def data_validation_process(self):
        try:
            self.logger.log(self.file_object, 'Start of Validation on files!!')

            # extracting values from prediction schema in schema_training.json
            LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, noofcolumns =  self.rawdata.valuesFromSchemaFile()

            # Manual Regex creation
            regex = self.rawdata.manualRegexCreation()

            # Delete Good and Bad data folder if existing and create them afresh
            self.rawdata.deleteExistingBadDataFolder()
            self.rawdata.deleteExistingGoodDataFolder()
            self.rawdata.createBadDataFolder()
            self.rawdata.createGoodDataFolder()

            # validating filename against manual regex
            self.rawdata.fileTransferToGoodAndBadDataFolder(regex, LengthOfDateStampInFile, LengthOfTimeStampInFile)

        except Exception as e:
            raise e