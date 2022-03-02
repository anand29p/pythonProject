from Data_Transform.DataTransformation import dataTransform
from application_logging.logger import App_Logger
from Raw_Data_Validation.rawValidation import Raw_Data_Validation

class data_validation:
    def __init__(self,batch_files_loc, main_log):
        self.file_object = open(main_log, 'a+')
        self.logger = App_Logger()
        self.rawdata = Raw_Data_Validation(batch_files_loc)
        self.dataTransform = dataTransform()

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
            self.rawdata.fileNameValidationAndTransferToGoodAndBadDataFolder(regex, LengthOfDateStampInFile, LengthOfTimeStampInFile)

            # validating column length in the file
            self.rawdata.validateColumnLength(noofcolumns)

            # validating if any column has all values missing
            self.rawdata.validateMissingValuesInWholeColumn()
            self.logger.log(self.file_object, "Raw Data Validation Complete!!")

            self.logger.log(self.file_object, "Starting Data Transforamtion!!")
            # replacing blanks in the csv file with "Null" values to insert in table
            self.dataTransform.replaceMissingWithNull()

            self.logger.log(self.file_object, "DataTransformation Completed!!!")

        except Exception as e:
            raise e