import os
from . import utils
import json

def path():
    this_file = __file__
    path_file_dir = os.path.dirname(os.path.dirname(this_file)) # PATH is parent dir
    with open(os.path.join(path_file_dir, "PATH"), "r") as f:
        return f.read().rstrip()

PATH = path()
print("TS-Data path: {}".format(PATH))

def data_info(name):
    """
    Returns JSON containing dataset information
    """
    dirname = os.path.join(PATH, name)
    with open(os.path.join(dirname, "meta"))as f:
        info = json.load(f)
    return info

def load_data(name):
    """
    Returns tuple with 5 elements: X_train, y_train, X_test, y_train, info
    """

    info = data_info(name)
    train_file = os.path.join(PATH, name, "train")
    test_file = os.path.join(PATH, name, "test")

    if info["n_timestamps"] == -1:
        X_train, y_train = utils.parse_variable_length_file(train_file, info)
        X_test, y_test = utils.parse_variable_length_file(test_file, info)
    else:
        X_train, y_train = utils.parse_fixed_length_file(train_file, info)
        X_test, y_test = utils.parse_fixed_length_file(test_file, info)

    return X_train, y_train, X_test, y_test, info

def list_datasets():
    """
    Returns list of datasets available
    """
    return os.listdir(PATH)
