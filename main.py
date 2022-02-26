import os
from wsgiref import simple_server
from flask import Flask
from flask import Response


app = Flask(__name__)



@app.route("/train", methods=['GET']) # Changed from POST

def trainRouteClient():

    try:
        path = 'Training_Batch_Files'

    except Exception as e:

        return Response("Error Occurred! %s" % e)

    return Response("Training successfull!!")



port = int(os.getenv("PORT",5003))
if __name__ == "__main__":
    host = '0.0.0.0'
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()