import os
import unittest

import data

basedir = os.path.dirname(os.path.realpath(__file__))


class TestData(unittest.TestCase):
    def setUp(self):
        self.path_json = os.path.join(basedir, "../mockdata/")
        self.files = {'schema_test':
                          '/home/s637041/PycharmProjects/hazelForm/tests/data/../mockdata/schema_test.json'}

    def test_get_all_files_ext(self):
        res = data.get_all_file_ext(dirname=self.path_json, ext=".json")

        self.assertEquals(res, self.files)

    def test_load_all_json_schema(self):
        res = data.load_all_json_schema(files=self.files)
        self.assertEquals(res, {'schema_test':
            {
                u'type': u'object',
                u'properties':
                    {
                        u'price':
                            {
                                u'type': u'number'
                            },
                        u'name':
                            {
                                u'type': u'string'
                            }
                    }
            }
        })
