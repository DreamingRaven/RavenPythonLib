# @Author: George Onoufriou <georgeraven>
# @Date:   2018-05-24
# @Filename: gitUpdate.py
# @Last modified by:   georgeraven
# @Last modified time: 2018-05-31
# @License: Please see LICENSE file in project root



class Gupdater(object):

    import os, sys
    from posixpath import basename, dirname



    def __init__(self, urls=[], path="./"):
        self.urls = urls
        self.path = path

        self.name = self.os.path.basename(self.sys.argv[0])
        self.prePend =  "[ " + self.name + " ] "


    def installer(self, path=None, urls=None):
        urls = urls if urls is not None else self.urls
        path = path if path is not None else self.path

        # neat trick to always ensure path ends in seperator '/' by appending empty
        path = self.os.path.join(path, "") # e.g "/usr/bin" vs "/usr/bin/"

        for url in urls:
            if (self.os.path.exists(path + self.os.path.basename(url)) == False):
                print(self.prePend, "find=false installing:",
                path + self. os.path.basename(url))
                try:
                    self.os.system("cd " + path + "; git clone " + url)
                except:
                    print(self.prePend,
                    "Could not install:", url , "to",
                    path + self.os.path.basename(url) )

    def install(self, path=None, urls=None):
        self.installer(path=path, urls=urls)



    def updater(self, path=None, urls=None):
        urls = urls if urls is not None else self.urls
        path = path if path is not None else self.path
        # neat trick to force filenames to always end in seperator "/"
        path = self.os.path.join(path, "") # e.g "/usr/bin" vs "/usr/bin/"

        # attempt self update if permission availiable
        try:
            print(self.prePend + " Updating self:")
            self.os.system("cd " + path + "; git pull")
        except:
            print(self.prePend + " Could not update self" +
                str(self.sys.exc_info()[1]), 1)

        for url in urls:
            # update any dependancies
            print(self.prePend, "Updating", self.os.path.basename(url) + ":" )
            try:
                self.os.system("cd " + path + self.os.path.basename(url) +
                    "; git pull")
            except:
                print("could not update, falling back: " +
                    str(self.sys.exc_info()[1]), 1)

    def update(self, path=None, urls=None):
        self.updater(path=path, urls=urls)
