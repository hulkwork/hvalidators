import socket
import traceback
import sys
import logging
import json
from datetime import datetime
import os
from flask import Flask, request, jsonify, abort
from src.ressource import _params,_schema
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append("../")

start_time = datetime.now()

basedir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
base_url = '/hazel/'

app.add_url_rule("/setParams", view_func=_params, methods=['POST'])
app.add_url_rule("/getParams", view_func=_params, methods=['GET'])

app.add_url_rule("/setSchema", view_func=_schema, methods=['POST'])
app.add_url_rule("/getSchema", view_func=_schema, methods=['GET'])

