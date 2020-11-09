# -*- coding: utf-8 -*-
"""
@author: Jack W Beaver https://github.com/JackWBeaver
"""

import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Flask Project</h1><p>This site is an example showing how to use Flask.</p>"

app.run()