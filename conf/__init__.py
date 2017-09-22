import json
import os

basedir = os.path.dirname(os.path.realpath(__file__))

metadata = json.load(open(os.path.join(basedir,'../metadata.json')))