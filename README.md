# hvalidators
Validate and set your parameters (json) into hazelcast or Redis (Persistence is not include)

#Usages :
Launch api :
``
python launch.py
``
- get all parameters available : 
``
curl localhost:5000/getParams
``
- get "params1" parameter :
``
curl localhost:5000/getParams?name=params1
``
- get all schema available : 
``
curl localhost:5000/getSchema
``
- get "schema1" parameter :
``
curl localhost:5000/getSchema?name=schema1
``

# Dockerfile
- docker pull hazelcast/hazelcast or use redis docker pull redis
- docker run -ti -p 5701:5701 hazelcast/hazelcast
- docker build .
- docker run -ti -p 5000:500 

# Requirements
-------------
- Flask
- jsonschema
- hazelcast-python-client
- redis

# TODO:
--------
- delete params into error if valid
- delete schema into error if valid
- Make sure this Dockerfile works well
- Put log
- clean code
- refactor code