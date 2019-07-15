# @Author: George Onoufriou <archer>
# @Date:   2019-07-15
# @Email:  george raven community at pm dot me
# @Filename: mongo_compat.py
# @Last modified by:   archer
# @Last modified time: 2019-07-15
# @License: Please see LICENSE in project root

from __future__ import print_function, absolute_import  # python 2-3 compat


class Mongo(object):
    """Python2/3 compatible MongoDb unility wrapper."""

    def __init__(self, dictionary=None):
        """Init class with defaults.

        optionally accepts dictionary of default overides.
        """
        pass

    __init__.__annotations__ = {"dictionary": dict, "return": None}


def test():
    """Unit test of MongoDB compat."""
    db = Mongo()


if(__name__ == "__main__"):
    test()
