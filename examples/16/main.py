# This file will demonstrate what Flask is in Python

# Firstly you'll need to import Flask with pipenv
# For example:
# pipenv install flask
# Then you can use the Flask module
# For example:
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
# This will output the following:
# Hello, World!
# You can also run the server with the following command:
# python main.py
# This will output the following:
#  * Running on http://
#
# You can also run the server with the following command:
# FLASK_APP=main.py flask run
# This will output the following:
#  * Running on http://
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 123-456-789
#  * Running on http://
