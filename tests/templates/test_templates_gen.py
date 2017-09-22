import unittest

from templates import templates_gen
from utils import validators


# os.environ['FWA_ENV'] = os.path.abspath(__file__ + "/../../")


class Testtemplates(unittest.TestCase):
    def setUp(self):
        self.schema_tests = validators._schema
        self.input_item_type = {"type":"number","name":"price"}
    def test_templates_gen(self):
        print templates_gen.get_template_from_schema(self.schema_tests)
        #self.assertEquals(res, None)
    def test_input_with_type(self):
        res = templates_gen.get_input_form(self.input_item_type)
        self.assertEquals(res,'<input name="price" type="number">')

