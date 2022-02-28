import json
import os
import shutil

from application_logging.logger import App_Logger
""""
    Data validation step
        1. Data collected from schema file ==> def valuesFromSchemaFile()
        2. Manual creation of Regex ==> def manualRegexCreation() 
        3. Validate Filename against manual regex ==> validationOfFilename()
            a. Delete existing bad data folder ==> deleteExistingBadDataFolder()
            b. Delete existing good data folder ==> deleteExistingGoodDataFolder()
    Company: IT Department, SRM IST
    Version: 1.0
    Revision: NIL
"""
class Raw_Data_Validation:
    def __init__(self, batch_files_loc):
        self.logger = App_Logger()
        self.schemaPath = "schema_training.json"

    def valuesFromSchemaFile(self):
        '''
            The method tries to fetch the values from schema file schema_training.json
            :return: LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, NumberofColumns
        '''
        try:
            with open(self.schemaPath, 'r') as f:
                dic = json.load(f)
                f.close()
                pattern = dic["SampleFileName"]
                LengthOfDateStampInFile = dic["LengthOfDateStampInFile"]
                LengthOfTimeStampInFile = dic["LengthOfTimeStampInFile"]
                NumberofColumns = dic['NumberofColumns']
                column_names = dic['ColName']
                file = open("Training_Logs/valuesfromSchemaValidationLog.txt", 'a+')
                message = "LengthOfDateStampInFile:: %s" % LengthOfDateStampInFile + "\t" + "LengthOfTimeStampInFile:: %s" % LengthOfTimeStampInFile + "\t " + "NumberofColumns:: %s" % NumberofColumns + "\n"
                self.logger.log(file, message)

                file.close()

        except Exception as e:
            file = open("Training_Logs/valuesfromSchemaValidationLog.txt", 'a+')
            self.logger.log(file, str(e))
            file.close()
            raise e

        return LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, NumberofColumns

    def manualRegexCreation(self):
        # wafer_08012020_120000.csv
        regex = "['wafer']+['\_'']+[\d_]+[\d]+\.csv"
        # regex = "['wafer\_']+[\d_]+[\d]+['.csv'}"
        return regex

    def validationOfFilename(self, regex, LengthOfDateStampInFile, LengthOfTimeStampInFile):
        # Delete Good and Bad data folder if existing
        self.deleteExistingBadDataFolder()
        self.deleteExistingGoodDataFolder()

    def deleteExistingBadDataFolder(self):
        try:
            path = 'Training_Raw_files_validated/'
            if os.path.isdir(path + 'Bad_Raw/'):
                shutil.rmtree(path + 'Bad_Raw/')
                file = open("Training_Logs/GeneralLog.txt", 'a+')
                self.logger.log(file,"BadRaw directory deleted before starting validation!!!")
                file.close()
        except OSError as s:
            file = open("Training_Logs/GeneralLog.txt", 'a+')
            self.logger.log(file,"Error while Deleting Directory : %s" %s)
            file.close()
            raise OSError

    def deleteExistingGoodDataFolder(self):
        try:
            path = 'Training_Raw_files_validated/'
            if os.path.isdir(path + 'Good_Raw/'):
                shutil.rmtree(path + 'Good_Raw/')
                file = open("Training_Logs/GeneralLog.txt", 'a+')
                self.logger.log(file, "GoodRaw directory deleted before starting validation!!!")
                file.close()
        except OSError as s:
            file = open("Training_Logs/GeneralLog.txt", 'a+')
            self.logger.log(file, "Error while Deleting Directory : %s" % s)
            file.close()
            raise OSError




