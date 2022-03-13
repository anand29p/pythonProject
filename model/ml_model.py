import os
import shutil
import pickle

class Model:
    def __init__(self, file_object, logger):
        self.file_object = file_object
        self.logger = logger
        self.model_directory = 'models/'

    def save_model(self, model, filename):
        self.logger.log(self.file_object, 'Entered the save_model method of the Model class')
        try:
            path = os.path.join(self.model_directory, filename)  # create seperate directory for each cluster
            if os.path.isdir(path):  # remove previously existing models for each clusters
                shutil.rmtree(self.model_directory)
                os.makedirs(path)
            else:
                os.makedirs(path)  #
            with open(path + '/' + filename + '.sav', 'wb') as f:
                pickle.dump(model, f)  # save the model to file
            self.logger.log(self.file_object, 'Model File ' + filename + ' saved. Exited the save_model method of the Model_Finder class')

            return 'success'
        except Exception as e:
            self.logger.log(self.file_object, 'Exception occured in save_model method of the Model_Finder class. Exception message:  ' + str(e))
            self.logger.log(self.file_object, 'Model File ' + filename + ' could not be saved. Exited the save_model method of the Model_Finder class')
            raise Exception()

        
        