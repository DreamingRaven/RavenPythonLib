# @Author: George Onoufriou <archer>
# @Date:   2019-07-15
# @Email:  george raven community at pm dot me
# @Filename: mongo_compat.py
# @Last modified by:   archer
# @Last modified time: 2019-07-15
# @License: Please see LICENSE in project root

from __future__ import print_function, absolute_import   # python 2-3 compat


class Mongo(object):
    """Python2/3 compatible MongoDb unility wrapper."""

    def __init__(self, args=None):
        """Init class with defaults.

        optionally accepts dictionary of default overides.
        """
        args = args if args is not None else dict()
        defaults = {
            "test": "test",
        }
        self.args = self._merge_dicts(defaults, args)
        print(self.args)

    __init__.__annotations__ = {"args": dict, "return": None}

    def _merge_dicts(self, *dicts):
        """Given multiple dictionaries, merge together in order."""
        result = {}
        for dictionary in dicts:
            result.update(dictionary)  # merge each dictionary in order
        return result

    _merge_dicts.__annotations__ = {"dicts": dict, "return": None}


def test():
    """Unit test of MongoDB compat."""
    db = Mongo({"test2": 2})


if(__name__ == "__main__"):
    test()
