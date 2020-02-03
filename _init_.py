from flask import Flask
import os 

os.path.dirname(_name_)
DIR = os.path.dirname(_file_)
DIR += '/'
app = Flask(__name__)

@app.route("/")
def root():
    return "Hello world!"

if __name__ == "__main__":
    app.debug = True
    app.run()
