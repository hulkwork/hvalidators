import os
import json

basedir = os.path.dirname(os.path.realpath(__file__))


def get_all_file_ext(dirname=os.path.join(basedir), ext=".json"):
    """

    :param dirname: 
    :param ext: 
    :return: 
    """
    files = os.listdir(dirname)
    res = {}
    for _file in files:
        if _file.endswith(ext):
            res[os.path.splitext(_file)[0]] = os.path.join(dirname,_file)
    return res




def load_all_json_schema(files={}):
    """
    
    :param files: 
    :return: 
    """
    tmp = {}
    for filename in files:
        tmp[filename] = json.load(open(files[filename]))
    return tmp
