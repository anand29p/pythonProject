import os
from wsgiref import simple_server
from flask import Flask
from flask import Response

from validation.data_valid import data_validation

app = Flask(__name__)



@app.route("/train", methods=['GET']) # Changed from POST

def trainRouteClient():

    try:
        batch_files_loc = 'Training_Batch_Files'
        main_log = "Training_Logs/Training_Main_Log.txt"
        schemaValidationLog = "Training_Logs/valuesfromSchemaValidationLog.txt"

        train_val_obj = data_validation(batch_files_loc, main_log)
        train_val_obj.data_validation_process()

    except Exception as e:

        return Response("Error Occurred! %s" % e)

    return Response("Training successfull!!")



port = int(os.getenv("PORT",5003))
if __name__ == "__main__":
    host = '0.0.0.0'
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()