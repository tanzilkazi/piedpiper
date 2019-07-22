# running thread outside flask: https://networklore.com/start-task-with-flask/
# kill thread: fuser 8080/tcp

import requests
import threading
import time, os
from flask import Flask
from sensor_temp import readTemp

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def before_app():
    def looper():
        while True:
            readTemp()
            time.sleep(1)

    thread = threading.Thread(target=looper)
    thread.start()
     

if __name__ == "__main__":
    try:
        before_app()
        app.run(debug=False, host='172.20.10.2', port=int(os.getenv('PORT', '5000')), threaded=True)
    except EOFError as eofe:
        print("Caught:", repr(eofe))
        print("Exiting.")
