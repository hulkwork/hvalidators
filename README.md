# hvalidators
Validate and set your parameters (json) into hazelcast

#Usages :
- get all parameters available :
curl localhost:5000/getParams
- get "params1" parameter :
curl localhost:5000/getParams?name=params1


# Dockerfile
- docker pull hazelcast/hazelcast
- docker run -ti -p 5701:5701 hazelcast/hazelcast
- docker build .
- docker run -ti -p 5000:500 

# Requirements
-------------
- Flask
- jsonschema
- hazelcast-python-client

# To-Do:
--------
- delete params into error if valid
- delete schema into error if valid
- Make sure this Dockerfile works well
- Put log
- clean code
- refactor code