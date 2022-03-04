
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

    def separate_label_feature(self, data, label_column_name):
        self.logger.log(self.file_object,"Process of separating X and Y value starts")
        try:
            self.X = data.drop(labels = label_column_name, axis=1)
            self.Y = data[label_column_name]
            self.logger.log(self.file_object, "Separated X and Y")
            return self.X, self.Y
        except Exception as e:
            self.logger.log(self.file_object, 'Exception occured in separate_label_feature method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger.log(self.file_object, 'Label Separation Unsuccessful. Exited the separate_label_feature method of the Preprocessor class')
            raise Exception()


