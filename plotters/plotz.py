# @Author: George Onoufriou <archer>
# @Date:   2018-05-24
# @Filename: mongo.py
# @Last modified by:   archer
# @Last modified time: 2018-09-24
# @License: Please see LICENSE file in project root



class Plotz(object):



    # imports for whole class (kept between all classes)
    import os, sys
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt



    # default values which will be set once and unchanged for all Mongo objects
    home = os.path.expanduser("~")
    className = "Plotz"
    prePend = "[ " + os.path.basename(sys.argv[0]) + " -> " + className + "] "



    # in this file I will be testing just using an args array, as the amount of
    # possible args would be overwhelming
    def __init__(self, args):
        # rebind args to new variable
