from flask import Flask
from flask import request
import requests
from lxml import etree
import re
import json
import os
from google import get_google_result

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/google', methods=['GET'])
def hello1():
    key=request.args.get('key','')
    result = get_google_result(key)
    
    return result

if __name__ ==  '__main__':
    app.run(host='0.0.0.0', port=port)
