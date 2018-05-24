# @Author: George Onoufriou <georgeraven>
# @Date:   2018-05-24
# @Filename: gitUpdate.py
# @Last modified by:   georgeraven
# @Last modified time: 2018-05-24
# @License: Please see LICENSE file in project root



class Gupdater(object):

    import os, sys
    from posixpath import basename, dirname

    def __init__(self, urls=[], pathTo="./"):
        self.urls = urls

    def update():
        try:
            # update self
            os.system("git pull")
            # update any listed dependencies
            for url in self.urls:
                if(os.path.exists("./" + basename(url)) == False):
                    os.system("git clone " + url)
                else:
                    os.system("cd " + basename(url) +  "; git pull; cd ..")
        except:
            None
