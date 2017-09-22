from importer import *
import data

basedir = os.path.dirname(os.path.realpath(__file__))


def get_all_file_ext(dirname=os.path.join(basedir), ext=".json"):
    """

    :param dirname: 
    :param ext: 
    :return: 
    """

    return data.get_all_file_ext(dirname=dirname,ext=ext)


def load_all_json_schema(files=get_all_file_ext()):
    """

    :param files: 
    :return: 
    """

    return data.load_all_json_schema(files=files)
