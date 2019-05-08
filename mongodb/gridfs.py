# @Author: George Onoufriou <archer>
# @Date:   2018-05-24
# @Filename: mongo.py
# @Last modified by:   archer
# @Last modified time: 2019-05-08T15:17:28+01:00
# @License: Please see LICENSE file in project root


class Gridfs(object):
    """
    Gridfs: A MongoDB wrapper for handling GridFS virtual filesystem, and all
        associated functionality, such as instantiating users,  authentication,
        connection, disconnection, storage, and retrieval.
    """
    # imports for whole class (kept between all classes)
    import os, sys, json, subprocess, json, copy
    from pymongo import MongoClient, errors
    import pandas as pd
    import gridfs

    # default values which will be set once and unchanged for all Mongo objects
    home = os.path.expanduser("~")
    className = "Mongo"
    prePend = "[ " + os.path.basename(sys.argv[0]) + " -> " + className + "] "

    def __init__(self, mongodb, argfs):
        """
        Initialisation function for gridfs

        self: just a gridfs object as standard,

        argfs: a dictionary containing all the relevant overloading arguments
            argfs, is a dictionary in this manner to cut down on the need for
            repettition so that args alone can be passed to everything rather
            thank having to explicitly state a plethora of inputs.

            {
                "db" : "a pymongo mongodb object; will be wrapped as gridfs",
            }
        """
        pass
        self.args = self.copy.deepcopy(self._without_keys(argfs, ["db"]))
        self.args["db"] = mongodb
        self.args["gridfs"] = self.gridfs.Gridfs(self.args["db"])
        # self.grid = self.gridfs.gridfs(self.args["db"])

    def _without_keys(self, dict, keys):
        """
        get subset of dictionary by excluding keys
        Thanks to: https://stackoverflow.com/a/31434038

        --- expects ---

        dict: a dictionary of key value pars which has values which should be
            excluded

        keys: a list or dict of keys to exclude

        --- returns ---

        a dictionary excluding key-value pairs listed in keys
        """
        return {x: dict[x] for x in dict if x not in keys}

    def debug(self):
        return self.args


if __name__ == "__main__":

    import time
    import copy
    import pandas as pd
    from RavenPythonLib.mongodb.mongo import Mongo

    mongodb = Mongo(isDebug=True)
    mongodb.debug()

    # creating user
    # stopping just in case it is already running
    mongodb.stop()
    time.sleep(2)  # delay to ensure db is closed properly
    mongodb.start()
    time.sleep(2)  # similar delay but for startup
    mongodb.addUser()
    mongodb.stop()  # stopping database ready for future use
    time.sleep(2)  # delay to ensure db is closed properly

    # starting true database with authentication
    mongodb.start(print=print, auth=True)
    time.sleep(2)

    temp_args = {
        "db": mongodb,
        "test1": 1,
        "test2": "eggsbert",
        "&&3245": "eggsbell",
    }
    # Gridfs(temp_args)

    # unwanted = ["db"]
    # def without_keys(dict, keys):
    #     """
    #     get subset of dictionary by excluding keys
    #     Thanks to: https://stackoverflow.com/a/31434038
    #
    #     --- expects ---
    #
    #     dict: a dictionary of key value pars which has values which should be
    #         excluded
    #
    #     keys: a list or dict of keys to exclude
    #
    #     --- returns ---
    #
    #     a dictionary excluding key-value pairs listed in keys
    #     """
    #     return {x: dict[x] for x in dict if x not in keys}
    #
    # print(temp_args)
    # temp_args = without_keys(temp_args, unwanted)
    # print(temp_args)
    # temp_args2 = copy.deepcopy(temp_args)
    # print(temp_args2)

    # mongodb.login()

    #TODO: add unit tests here
