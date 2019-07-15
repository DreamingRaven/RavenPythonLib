# @Author: George Onoufriou <archer>
# @Date:   2019-07-15
# @Email:  george raven community at pm dot me
# @Filename: mongo_compat.py
# @Last modified by:   archer
# @Last modified time: 2019-07-15
# @License: Please see LICENSE in project root

from __future__ import print_function, absolute_import   # python 2-3 compat
import os
from pymongo import MongoClient, errors  # python 2 or python 3 versions


class Mongo(object):
    """Python2/3 compatible MongoDb unility wrapper."""

    def __init__(self, args=None, logger=None):
        """Init class with defaults.

        optionally accepts dictionary of default overides.
        """
        args = args if args is not None else dict()
        self.home = os.path.expanduser("~")
        defaults = {
            "mongoUser": "groot",
            "mongoPass": "iamgroot",
            "userRole": "readWrite",
            "mongoIp": "127.0.0.1",
            "mongoDbName": "RecSyst",
            "mongoCollName": "testColl",
            "mongoPort": "27017",
            "mongoUrl": "mongodb://localhost:27017/",
            "mongoPath": self.home + "/db",
            "mongoLogPath": self.home + "/db" + "/log",
            "mongoLogName": "mongoLog",
            "mongoCursorTimeout": 600000,
            "db": None,
            "pylog": logger if logger is not None else print,
        }
        self.args = self._merge_dicts(defaults, args)

    __init__.__annotations__ = {"args": dict, "return": None}

    def _merge_dicts(self, *dicts):
        """Given multiple dictionaries, merge together in order."""
        result = {}
        for dictionary in dicts:
            result.update(dictionary)  # merge each dictionary in order
        return result

    _merge_dicts.__annotations__ = {"dicts": dict, "return": None}

    def __setitem__(self, key, value):
        """Set a single arg or state by, (key, value)."""
        raise NotImplementedError("Data.__getitem__() is not yet implemented")
        self.args[key] = value

    __setitem__.__annotations__ = {"key": str, "value": any, "return": None}

    def __getitem__(self, key):
        """Get a single arg or state by, (key, value)."""
        raise NotImplementedError("Data.__getitem__() is not yet implemented")
        try:
            return self.args[key]
        except KeyError:
            return None  # does not exist is the same as None, gracefull catch

    __getitem__.__annotations__ = {"key": str, "return": any}

    def __delitem__(self, key):
        """Delete a single arg or state by, (key, value)."""
        raise NotImplementedError("Data.__getitem__() is not yet implemented")
        try:
            del self.args[key]
        except KeyError:
            pass  # job is not done but equivalent outcomes so will not error

    __delitem__.__annotations__ = {"key": str, "return": None}

    def __iter__(self):
        """Iterate through housed dictionary, for looping."""
        raise NotImplementedError("Data.__getitem__() is not yet implemented")
        return iter(self.args)

    __iter__.__annotations__ = {"return": any}

    def __len__(self):
        """Return the first order length of the dictionary."""
        raise NotImplementedError("Data.__getitem__() is not yet implemented")
        return len(self.args)

    __len__.__annotations__ = {"return": int}


def test():
    """Unit test of MongoDB compat."""
    db = Mongo({"test2": 2})
    # len(db)
    # for item in db:
    #     # print(item, "\t\t", db[item])
    #     db[item]
    # del db["test2"]
    # len(db)


if(__name__ == "__main__"):
    test()
