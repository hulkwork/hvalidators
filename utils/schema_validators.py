import jsonschema
from jsonschema import Draft4Validator
import data
from conf.apiVariables import KEY_VALID_SCHEMA, KEY_ERROR_SCHEMA
from utils import cache_app


def get_validate(_json, schema):
    """
    
    :param _json: 
    :param schema: 
    :return: 
    """

    return jsonschema.validate(_json, schema)


def get_all_valid_schema():
    _schema_available = data.load_all_json_schema()
    _schema_valides = {}
    get_error_files = {}
    for key in _schema_available:
        try:
            Draft4Validator.check_schema(_schema_available[key])
            _schema_valides[key] = _schema_available[key]
        except Exception, e:
            get_error_files[key] = {
                "schema": _schema_available[key],
                "error": str(e)
            }

    return _schema_valides, get_error_files


def put_all_valid_schema():
    _schema_valides, _error_schema = get_all_valid_schema()

    valid_schema, error_schema = cache_app.get_schema_cache()
    for key_schema in _schema_valides:
        valid_schema[key_schema] = _schema_valides[key_schema]
        if key_schema in error_schema:
            del error_schema[key_schema]
    print error_schema
    for key_schema_error in _error_schema:
        error_schema[key_schema_error] = _error_schema[key_schema_error]
        if key_schema_error in valid_schema:
            del valid_schema[key_schema_error]

    cache_app.put_schema_cache(key=KEY_VALID_SCHEMA, value=valid_schema)
    cache_app.put_schema_cache(key=KEY_ERROR_SCHEMA, value=error_schema)


def get_hazel_schema():
    return cache_app.get_schema_cache()


put_all_valid_schema()
ALL_SCHEMA_FILES, schema_error = get_all_valid_schema()
