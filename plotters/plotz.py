# @Author: George Onoufriou <archer>
# @Date:   2018-05-24
# @Filename: mongo.py
# @Last modified by:   archer
# @Last modified time: 2018-09-26
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
    def __init__(self, plot_args=None):
        # rebind args to new variable
        self.args = plot_args
        self.plotz = None



    def doArgsExist(self, argsGiven_dict, argsWanted_list):
        if(argsGiven_dict != None):
            argMissing_bool = False
            for arg in argsWanted_list: # for each wanted arg
                if(not arg in argsGiven_dict): # check if this particular arg is not in dict
                    print(self.prePend, "arg missing:", arg) # display
                    argMissing_bool= True

            if(argMissing_bool == False):
                return True
        print(self.prePend,
            "Could not find required args, please check args are not None and each needed arg exists")
        return False



    def plot_density(self, plot_args=None):
        args = plot_args if plot_args is not None else self.args
        print(self.prePend, "plotting density graph")
        if(self.doArgsExist(argsGiven_dict=args, argsWanted_list=["x", "y", "z"])):
            None




if __name__ == "__main__":
    plot = Plotz()
    dictArgs = {
        "x":"1",
        "y":"2"
    }
    plot.plot_density(plot_args=dictArgs)
    # print(plot.doArgsExist(argsGiven_dict=dictArgs, argsWanted_list=["x", "y", "z"]))
