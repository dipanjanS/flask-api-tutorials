from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello you are at the root level"

import socapp.modules.cat.routes
import socapp.modules.dog.routes
import socapp.modules.monkey.routes
