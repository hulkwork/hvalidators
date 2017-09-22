import jsonschema
from jsonschema import Draft4Validator
import data


def get_validate(_json, schema):
    """
    
    :param _json: 
    :param schema: 
    :return: 
    """


    return jsonschema.validate(_json, schema)


def get_all_valide_schema():
    _json_available = data.get_all_file_ext()
    _schema_available = data.load_all_json_schema(_json_available)
    _schema_valides = {}
    get_error_files = {}
    for key in _schema_available:
        try:
            Draft4Validator.check_schema(_schema_available[key])
            _schema_valides[key] = _schema_available[key]
        except Exception,e:
            get_error_files[key] = {
                "schema": _schema_available[key],
                "error": str(e)
            }

    return _schema_valides,get_error_files



ALL_SCHEMA,schema_error = get_all_valide_schema()
