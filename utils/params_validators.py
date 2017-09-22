import jsonschema
from jsonschema import Draft4Validator
import params
from src import hazel
from conf.apiVariables import MAP_PARAMS,KEY_VALID_PARAMS,KEY_ERROR_SCHEMA
from utils import schema_validators


def put_all_valid_params():
    _get_json_prams = params.load_all_json_schema()
    parameters = hazel.client.get_map(MAP_PARAMS)
    valid_params_hazel = parameters.get(KEY_VALID_PARAMS).result() if parameters.contains_key(KEY_VALID_PARAMS) else {}
    error_params_hazel = parameters.get(KEY_ERROR_SCHEMA).result() if parameters.contains_key(KEY_ERROR_SCHEMA) else {}
    valid_params_hazel = valid_params_hazel if valid_params_hazel != None else {}
    error_params_hazel = error_params_hazel if error_params_hazel != None else {}

    _schemas_hazel,_error_schema_hazel = schema_validators.get_hazel_schema()
    for key_params in  _get_json_prams:
        if key_params in _schemas_hazel:
            try:
                jsonschema.validate(_get_json_prams[key_params],_schemas_hazel[key_params])
                valid_params_hazel[key_params] = _get_json_prams[key_params]
                if key_params in error_params_hazel:
                    del error_params_hazel[key_params]

            except Exception,e:
                error_params_hazel[key_params] = {
                    "params" : _get_json_prams[key_params],
                    "error"  : str(e)

                }
        else:
            error_params_hazel[key_params] = {
                "params": _get_json_prams[key_params],
                "error": "< %s > schema not found" % key_params

            }


    parameters.put(KEY_VALID_PARAMS, valid_params_hazel)
    parameters.put(KEY_ERROR_SCHEMA, error_params_hazel)

def get_hazel_params():
    parameters = hazel.client.get_map(MAP_PARAMS)
    valid_params_hazel = parameters.get(KEY_VALID_PARAMS).result() if parameters.contains_key(KEY_VALID_PARAMS) else {}
    error_params_hazel = parameters.get(KEY_ERROR_SCHEMA).result() if parameters.contains_key(KEY_ERROR_SCHEMA) else {}
    valid_params_hazel = valid_params_hazel if valid_params_hazel != None else {}
    error_params_hazel = error_params_hazel if error_params_hazel != None else {}
    return valid_params_hazel,error_params_hazel

put_all_valid_params()