from importer import *

basedir = os.path.dirname(os.path.realpath(__file__))

metadata = json.load(open(os.path.join(basedir,'../metadata.json')))

settings = {
    "hazelcast-adress" : {"node1":"localhost:5701"},
    "log-location" : "debug.log"
}