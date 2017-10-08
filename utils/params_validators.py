import jsonschema
import params
from conf.apiVariables import KEY_VALID_PARAMS, KEY_ERROR_SCHEMA
from utils import schema_validators
cache_app = schema_validators.cache_app # That make only call for caceh_app

def put_all_valid_params():
    _get_json_prams = params.load_all_json_schema()
    valid_params,  error_params = cache_app.get_parameters_cache()
    _schemas_hazel, _error_schema_hazel = schema_validators.get_hazel_schema()
    for key_params in _get_json_prams:
        if key_params in _schemas_hazel:
            try:
                jsonschema.validate(_get_json_prams[key_params], _schemas_hazel[key_params])
                valid_params[key_params] = _get_json_prams[key_params]
                if key_params in error_params:
                    del error_params[key_params]

            except Exception, e:
                error_params[key_params] = {
                    "params": _get_json_prams[key_params],
                    "error": str(e)

                }
        else:
            error_params[key_params] = {
                "params": _get_json_prams[key_params],
                "error": "< %s > schema not found" % key_params

            }

    cache_app.put_parameters_cache(key=KEY_VALID_PARAMS, value=valid_params)
    cache_app.put_schema_cache(key=KEY_ERROR_SCHEMA, value=error_params)


def get_hazel_params():
    return cache_app.get_parameters_cache()


put_all_valid_params()
