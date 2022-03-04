
class Preprocessor:
    def __init__(self, file_object, logger):
        self.file_object = file_object
        self.logger = logger

    def remove_columns(self, data, columns):
        self.logger.log(self.file_object, "Entered remove_column() method ")
        self.data = data
        self.columns = columns
        try:
            self.useful_data = self.data.drop(labels=self.columns, axis=1) # drop the labels specified in the columns
            self.logger.log(self.file_object, 'Column removal Successful.Exited the remove_columns method of the Preprocessor class')
            return self.useful_data
        except Exception as e:
            self.logger.log(self.file_object,'Exception occured in remove_columns method of the Preprocessor class. Exception message:  '+str(e))
            self.logger.log(self.file_object, 'Column removal Unsuccessful. Exited the remove_columns method of the Preprocessor class')
            raise Exception()

