import jsonschema
from jsonschema import Draft4Validator
import data
from src import hazel
from conf.apiVariables import MAP_SCHEMA,KEY_VALID_SCHEMA,KEY_ERROR_SCHEMA


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
    schemas = hazel.client.get_map(MAP_SCHEMA)
    _schema_valides_hazel = {}
    _error_schema_hazel = {}
    if schemas.contains_key(KEY_VALID_SCHEMA):
        _schema_valides_hazel = schemas.get(KEY_VALID_SCHEMA).result()
    if schemas.contains_key(KEY_ERROR_SCHEMA):
        _error_schema_hazel = schemas.get(KEY_ERROR_SCHEMA).result()
    if _schema_valides_hazel == None:
        _schema_valides_hazel = {}
    if _error_schema_hazel ==None:
        _error_schema_hazel = {}
    for key_schema in _schema_valides:

        _schema_valides_hazel[key_schema] = _schema_valides[key_schema]
        if key_schema in _error_schema_hazel:
            del _error_schema_hazel[key_schema]
    for key_schema_error  in _error_schema:
        _error_schema_hazel[key_schema_error] = _error_schema[key_schema_error]
        if key_schema_error in _schema_valides_hazel:
            del _schema_valides_hazel[key_schema_error]

    schemas.put(KEY_VALID_SCHEMA,_schema_valides_hazel)
    schemas.put(KEY_ERROR_SCHEMA,_error_schema_hazel)




def get_hazel_schema():
    schemas = hazel.client.get_map(MAP_SCHEMA)
    _schema_valides = {}
    _error_schema = {}
    if schemas.contains_key(KEY_VALID_SCHEMA):
        _schema_valides = schemas.get(KEY_VALID_SCHEMA).result()
        if _schema_valides  == None:
            _schema_valides = {}
    if schemas.contains_key(KEY_ERROR_SCHEMA):
        _error_schema = schemas.get(KEY_ERROR_SCHEMA).result()
        if _error_schema == None:
            _error_schema = {}


    return _schema_valides,_error_schema


put_all_valid_schema()
ALL_SCHEMA_FILES, schema_error = get_all_valid_schema()
