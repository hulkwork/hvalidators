import traceback
import json
from conf.apiVariables import MAP_PARAMS, KEY_VALID_PARAMS, KEY_ERROR_SCHEMA, \
    MAP_SCHEMA, KEY_VALID_SCHEMA

DEFAULT_CACHE_APP = None
try:
    from src import hazel
    parameters = hazel.client.get_map(MAP_PARAMS)
    schemas = hazel.client.get_map(MAP_SCHEMA)
    DEFAULT_CACHE_APP = 'HAZEL'
except Exception, e:
    from src import rediser
    parameters = rediser.redis_mongo
    schemas = parameters
    DEFAULT_CACHE_APP = 'REDIS'
    print traceback.format_exc()


def get_parameters_cache(cache_application_name=DEFAULT_CACHE_APP):
    if parameters is None:
        return {}, {}
    if cache_application_name.upper() == 'HAZEL':
        valid_params = parameters.get(KEY_VALID_PARAMS).result() if parameters.contains_key(
            KEY_VALID_PARAMS) else {}
        error_params = parameters.get(KEY_ERROR_SCHEMA).result() if parameters.contains_key(
            KEY_ERROR_SCHEMA) else {}
    else:
        valid_params = json.loads(parameters.get(KEY_VALID_PARAMS)) if parameters.exists(KEY_VALID_PARAMS) else {}
        error_params = json.loads(parameters.get(KEY_ERROR_SCHEMA)) if parameters.exists(KEY_ERROR_SCHEMA) else {}

    valid_params = valid_params if valid_params is not None else {}
    error_params = error_params if error_params is not None else {}
    return valid_params, error_params


def get_schema_cache(cache_application_name=DEFAULT_CACHE_APP):
    if schemas is None:
        return {}, {}
    if cache_application_name.upper() == 'HAZEL':
        valid_schema = schemas.get(KEY_VALID_SCHEMA).result() if schemas.contains_key(KEY_VALID_SCHEMA) else {}
        error_schema = schemas.get(KEY_ERROR_SCHEMA).result() if schemas.contains_key(KEY_ERROR_SCHEMA) else {}
    else:
        valid_schema = json.loads(schemas.get(KEY_VALID_SCHEMA)) if schemas.exists(KEY_VALID_PARAMS) else {}
        error_schema = json.loads(schemas.get(KEY_ERROR_SCHEMA)) if schemas.exists(KEY_ERROR_SCHEMA) else {}
    valid_schema = valid_schema if valid_schema is not None else {}
    error_schema = error_schema if error_schema is not None else {}
    return valid_schema, error_schema


def put_parameters_cache(key, value, cache_application_name=DEFAULT_CACHE_APP):
    if parameters is None:
        raise TypeError("Parameters is None")
    if cache_application_name.upper() == 'HAZEL':
        parameters.put(key, value)
    else:
        parameters.set(key, json.dumps(value))


def put_schema_cache(key, value, cache_application_name=DEFAULT_CACHE_APP):
    print schemas
    if schemas is None:
        raise TypeError("schemas is None")
    if cache_application_name.upper() == 'HAZEL':
        schemas.put(key, value)
    else:
        schemas.set(key, json.dumps(value))
