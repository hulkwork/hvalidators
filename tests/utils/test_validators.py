import unittest

from utils import validators



class TestValidators(unittest.TestCase):
    def setUp(self):
        self.json_test = {
            "price": 10,
            "name": "CallMeMaybe"
        }
        self.schema_test = {
            "type": "object",
            "properties": {
                "price": {"type": "number"},
                "name": {"type": "string"},
            },
        }
        self.schema_test_object = {
            "type": "object",
            "properties": {
                "benefecaire": {
                    "type": "object",
                    "properties": {
                        "dateNaissance": {"type": "string"}
                    }

                },
                "name": {"type": "string"},
            },
        }
        self.json_test_object = {
            "benefecaire": {"dateNaissance": "1"},
            "name": "CallMeMaybe"
        }

    def test_validation(self):
        res = validators.get_validate(self.json_test, self.schema_test)
        self.assertEquals(res, None)

    def test_nested(self):
        res = validators.get_validate(self.json_test_object, self.schema_test_object)
        self.assertEquals(res, None)

    def test_get_all_valide_schema(self):
        schema_valide, errors = validators.get_all_valide_schema()

        self.assertEquals(schema_valide, {'schema_test': {u'type': u'object',
                                                          u'properties': {u'price': {u'type': u'number'},
                                                                          u'name': {u'type': u'string'}}}})
        self.error = {'schema_error': {
            'error': "u'strong' is not valid under any of the given schemas\n\nFailed validating u'anyOf' in schema[u'properties'][u'properties'][u'additionalProperties'][u'properties'][u'type']:\n    {u'anyOf': [{u'$ref': u'#/definitions/simpleTypes'},\n                {u'items': {u'$ref': u'#/definitions/simpleTypes'},\n                 u'minItems': 1,\n                 u'type': u'array',\n                 u'uniqueItems': True}]}\n\nOn instance[u'properties'][u'price'][u'type']:\n    u'strong'",
            'schema': {u'type': u'object',
                       u'properties': {u'price': {u'type': u'strong'}, u'name': {u'type': u'string'}}}}}
        self.assertEquals(errors, self.error)
