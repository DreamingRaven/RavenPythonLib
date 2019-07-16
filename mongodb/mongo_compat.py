# @Author: George Onoufriou <archer>
# @Date:   2019-07-15
# @Email:  george raven community at pm dot me
# @Filename: mongo_compat.py
# @Last modified by:   archer
# @Last modified time: 2019-07-16
# @License: Please see LICENSE in project root

from __future__ import print_function, absolute_import   # python 2-3 compat
import os
import subprocess
from pymongo import MongoClient, errors  # python 2 or python 3 versions


class Mongo(object):
    """Python2/3 compatible MongoDb utility wrapper.

    This wrapper saves its state in an internal overridable dictionary
    such that you can adapt it to your requirements, if you should need to do
    something unique, the caveat being it becomes harder to read.
    """

    def __init__(self, args=None, logger=None):
        """Init class with defaults.

        optionally accepts dictionary of default overides.
        """
        args = args if args is not None else dict()
        self.home = os.path.expanduser("~")
        defaults = {
            "mongoUser": "groot",
            "mongoPass": "iamgroot",
            "mongoAuth": "SCRAM-SHA-1",
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
            "pylog": logger if logger is not None else print,
            "mongoSsl": None,
            "db": None,
        }
        self.args = self._merge_dicts(defaults, args)

    __init__.__annotations__ = {"args": dict, "return": None}

    def connect(self):
        """Connect to a specific mongodb database defined in args.

        Uses mongoUrl, mongoUser, mongoPass, mongoDbName.
        """
        self.args["client"] = MongoClient(
            self.args["mongoUrl"],
            username=str(self.args["mongoUser"]),
            password=str(self.args["mongoPass"]),
            authSource=str(self.args["mongoDbName"]),
            authMechanism=str(self.args["mongoAuth"]))
        self.args["db"] = self.args["client"][self.args["mongoDbName"]]

    def login(self):
        """Log in to database, interupt, and availiable via cli."""
        loginArgs = [
            "mongo",
            "--port", str(self.args["mongoPort"]),
            "-u",   str(self.args["mongoUser"]),
            "-p", str(self.args["mongoPass"]),
            "--authenticationDatabase", str(self.args["mongoDbName"])
        ]
        subprocess.call(loginArgs)

    def start(self):
        """Launch the database."""
        pass
        raise NotImplementedError("start() is not yet implemented")

    def stop(self):
        """Stop a running local database."""
        pass
        raise NotImplementedError("strop() is not yet implemented")

    def addUser(self):
        """Add a user with given permissions to the authentication database."""
        self.args["pylog"]("Adding  mongodb user:",
                           str(self.args["mongoUser"]),
                           ", role:", str(self.args["userRole"]),
                           ", authdb:", str(self.args["mongoDbName"]))
        raise NotImplementedError("addUser() is not yet implemented")

    def debug(self):
        """Log function to help track the internal state of the class."""
        self.args["pylog"](self.args)

    def _merge_dicts(self, *dicts):
        """Given multiple dictionaries, merge together in order."""
        result = {}
        for dictionary in dicts:
            result.update(dictionary)  # merge each dictionary in order
        return result

    _merge_dicts.__annotations__ = {"dicts": dict, "return": None}

    def __setitem__(self, key, value):
        """Set a single arg or state by, (key, value)."""
        raise NotImplementedError("setitem() is not yet implemented")
        self.args[key] = value

    __setitem__.__annotations__ = {"key": str, "value": any, "return": None}

    def __getitem__(self, key):
        """Get a single arg or state by, (key, value)."""
        raise NotImplementedError("getitem() is not yet implemented")
        try:
            return self.args[key]
        except KeyError:
            return None  # does not exist is the same as None, gracefull catch

    __getitem__.__annotations__ = {"key": str, "return": any}

    def __delitem__(self, key):
        """Delete a single arg or state by, (key, value)."""
        raise NotImplementedError("delitem() is not yet implemented")
        try:
            del self.args[key]
        except KeyError:
            pass  # job is not done but equivalent outcomes so will not error

    __delitem__.__annotations__ = {"key": str, "return": None}

    def __iter__(self):
        """Iterate through housed dictionary, for looping."""
        raise NotImplementedError("iter() is not yet implemented")
        return iter(self.args)

    __iter__.__annotations__ = {"return": any}

    def __len__(self):
        """Return the first order length of the dictionary."""
        raise NotImplementedError("len() is not yet implemented")
        return len(self.args)

    __len__.__annotations__ = {"return": int}


def test():
    """Unit test of MongoDB compat."""
    db = Mongo({"test2": 2})
    db.debug()
    db.connect()
    db.debug()
    db.start()
    db.addUser()
    db.login()
    db.stop()
    # len(db)
    # for item in db:
    #     # print(item, "\t\t", db[item])
    #     db[item]
    # del db["test2"]
    # len(db)


if(__name__ == "__main__"):
    test()
