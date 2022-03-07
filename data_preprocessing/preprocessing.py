import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

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

    def is_null_present(self, data_X):
        self.logger.log(self.file_object, "Started checking if there is any null values in X")
        self.null_present = False
        try:
            self.null_counts = data_X.isna().sum()
            for i in self.null_counts:
                if i>0:
                    self.null_present = True
                    break
            return self.null_present
        except Exception as e:
            self.logger.log(self.file_object, 'Exception occured in is_null_present method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger.log(self.file_object, 'Finding missing values failed. Exited the is_null_present method of the Preprocessor class')
            raise Exception()

    def impute_missing_values(self, X):
        self.logger.log(self.file_object, 'Entered the impute_missing_values method of the Preprocessor class')
        self.data = X
        try:
            imputer = KNNImputer(n_neighbors=3, weights='uniform', missing_values=np.nan)
            self.new_array = imputer.fit_transform(self.data)  # impute the missing values
            # convert the nd-array returned in the step above to a Dataframe
            self.new_data = pd.DataFrame(data=self.new_array, columns=self.data.columns)
            self.logger.log(self.file_object, 'Imputing missing values Successful. Exited the impute_missing_values method of the Preprocessor class')
            return self.new_data
        except Exception as e:
            self.logger.log(self.file_object,'Exception occured in impute_missing_values method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger.log(self.file_object,'Imputing missing values failed. Exited the impute_missing_values method of the Preprocessor class')
            raise Exception()

    def get_columns_with_zero_std_deviation(self, data):
        self.logger.log(self.file_object, 'Entered the get_columns_with_zero_std_deviation method of the Preprocessor class')
        self.columns = data.columns
        self.data_n = data.describe()
        self.col_to_drop = []
        try:
            for x in self.columns:
                if (self.data_n[x]['std'] == 0):  # check if standard deviation is zero
                    self.col_to_drop.append(x)  # prepare the list of columns with standard deviation zero
            self.logger.log(self.file_object, 'Column search for Standard Deviation of Zero Successful. Exited the get_columns_with_zero_std_deviation method of the Preprocessor class')
            return self.col_to_drop

        except Exception as e:
            self.logger.log(self.file_object, 'Exception occured in get_columns_with_zero_std_deviation method of the Preprocessor class. Exception message:  ' + str(
                                       e))
            self.logger.log(self.file_object, 'Column search for Standard Deviation of Zero Failed. Exited the get_columns_with_zero_std_deviation method of the Preprocessor class')
            raise Exception()





