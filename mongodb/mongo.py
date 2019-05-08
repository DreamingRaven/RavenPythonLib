# @Author: George Onoufriou <archer>
# @Date:   2018-05-24
# @Filename: mongo.py
# @Last modified by:   archer
# @Last modified time: 2018-08-21
# @License: Please see LICENSE file in project root



class Mongo(object):



    # imports for whole class (kept between all classes)
    import os, sys, json, subprocess, json
    from pymongo import MongoClient, errors
    import pandas as pd




    # default values which will be set once and unchanged for all Mongo objects
    home = os.path.expanduser("~")
    className = "Mongo"
    prePend = "[ " + os.path.basename(sys.argv[0]) + " -> " + className + "] "



    # default constructor TODO: make this an input dict for simplicity
    def __init__(self, isDebug=None, mongoUser=None, mongoPass=None,
                 mongoIp=None, mongoDbName=None, mongoCollName=None,
                 mongoPort=None, mongoUrl=None, mongoPath=None,
                 mongoLogPath=None, mongoLogName=None, userRole=None,
                 mongoCursorTimeout=None):

        # set defaults in non obstructive well defined manner
        self.isDebug = isDebug if isDebug is not None else False
        self.mongoUser = mongoUser if mongoUser is not None else "groot"
        self.mongoPass = mongoPass if mongoPass is not None else "iamgroot"
        self.mongoIp = mongoIp if mongoIp is not None else "127.0.0.1"
        self.mongoDbName = mongoDbName if mongoDbName is not None else "RecSyst"
        self.mongoCollName = mongoCollName if mongoCollName is not None else "testColl"
        self.mongoPort = mongoPort if mongoPort is not None else "27017"
        self.mongoUrl = mongoUrl if mongoUrl is not None else "mongodb://localhost:27017/"
        self.mongoPath = mongoPath if mongoPath is not None else str(self.home + "/db")
        self.mongoLogPath = mongoLogPath if mongoLogPath is not None else str(self.mongoPath + "/log")
        self.mongoLogInclusivePath = str(self.mongoLogPath + "/" + self.mongoLogName) if mongoLogName is not None else str(self.mongoLogPath + "/mongoLog")
        self.userRole = str(userRole) if userRole is not None else "readWrite"
        self.mongoCursorTimeout = mongoCursorTimeout if mongoCursorTimeout is not None else 600000 # 10 minutes
        self.db = None



    def login(self):
        loginArgs = [
            "mongo",
            "--port", str(self.mongoPort),
            "-u",   str(self.mongoUser),
            "-p", str(self.mongoPass),
            "--authenticationDatabase", str(self.mongoDbName)
        ]
        self.subprocess.call(loginArgs)



    def connect(self):
        # set up individual client
        self.client = self.MongoClient(self.mongoUrl,
                                  username=str(self.mongoUser),
                                  password=str(self.mongoPass),
                                  authSource=str(self.mongoDbName),
                                  authMechanism=str('SCRAM-SHA-1'))

        self.db = self.client[self.mongoDbName]



    # check to make sure everything is set properly
    def debug(self, print=print):
        print(self.prePend +
              "\n\tDebug = "        +       str(self.isDebug)       +
              "\n\tUsername = "     +       str(self.mongoUser)     +
              "\n\tPassword = "     +       str("***")              +
              "\n\tDb Ip = "        +       str(self.mongoIp)       +
              "\n\tDb Name = "      +       str(self.mongoDbName)   +
              "\n\tColl Name = "    +       str(self.mongoCollName) +
              "\n\tDb Port = "      +       str(self.mongoPort)     +
              "\n\tDb Url = "       +       str(self.mongoUrl)      +
              "\n\tDb Path = "      +       str(self.mongoPath)     +
              "\n\tDb logPath = "   +       str(self.mongoLogPath)  +
              "\n\tDb cursorTimeout = "   + str(self.mongoCursorTimeout)  +
              "\n\tDb logIncPath = "+       str(self.mongoLogInclusivePath),
              0 # used in logger to set min level
              )



    # starts a database
    def start(self, print=print, auth=False):
        print(self.prePend + "Starting mongodb: auth=" + str(auth), 3)
        mongoArgs = []

        try:
            # create paths if they dont already exist
            self.subprocess.call(["mkdir", "-p",
                str(self.mongoPath),
                str(self.mongoLogPath)
                ])

            # change mongo arguments depending if authenticating or not
            if(auth==True):
                mongoArgs = [
                    "mongod"    ,
                    "--bind_ip" ,       str(self.mongoIp)       ,
                    "--port"    ,       str(self.mongoPort)     ,
                    "--dbpath"  ,       str(self.mongoPath)     ,
                    "--logpath" ,       str(self.mongoLogInclusivePath)  ,
                    "--setParameter",   str("cursorTimeoutMillis=" + str(self.mongoCursorTimeout)),
                    "--auth"    ,
                    "--quiet"
                    ]
                print("Auth db launching", 3)
            else:
                mongoArgs = [
                    "mongod"    ,
                    "--bind_ip" ,   str(self.mongoIp)       ,
                    "--port"    ,   str(self.mongoPort)     ,
                    "--dbpath"  ,   str(self.mongoPath)     ,
                    "--logpath" ,   str(self.mongoLogInclusivePath)  ,
                    "--quiet"
                    ]
                print("No auth db launching...", 3)
            # call mongodb with arguments adjusted prior
            self.mongoProcess = self.subprocess.Popen(mongoArgs)
            print(str(type(self.mongoProcess))+ str(self.mongoProcess), 3)

        except:
            print(self.prePend + "could not START mongodb:\n" +
                str(self.sys.exc_info()[0]) + " " +
                str(self.sys.exc_info()[1]), 1)



    # stops a running database on local system
    def stop(self, print=print):
        print(self.prePend + "Stopping mongodb", 3)
        try:
            # this will only work on local system purposefully!
            # this will only work on linux systems too apparentley
            self.subprocess.Popen(["mongod", "--dbpath", str(self.mongoPath),
                "--shutdown"])

        except:
            print(self.prePend + "could not STOP mongodb:\n" +
                str(self.sys.exc_info()[0]) + " " +
                str(self.sys.exc_info()[1]) , 1)



    # adds new user to database and warns if user could not be added
    def addUser(self, username=None, password=None, role=None, print=print):

        # just incase user arguments wanted are different from initial args
        self.mongoUser = username if username is not None else self.mongoUser
        self.mongoPass = password if password is not None else self.mongoPass
        self.userRole  = role     if role is not     None else self.userRole

        print(self.prePend + "Adding mongoDb User: " + str(self.mongoUser) +
            ", Role:" + str(self.userRole), 3)

        try:
            client = self.MongoClient(self.mongoUrl)
            db = client[self.mongoDbName]

            if(self.userRole == "all"):
                db.command("createUser", self.mongoUser, pwd=self.mongoPass, roles=["readWrite", "dbAdmin"])
            else:
                db.command("createUser", self.mongoUser, pwd=self.mongoPass, roles=[self.userRole])

        except:
            print(self.prePend + "could not ADD mongodb USER:\n" +
                str(self.sys.exc_info()[0]) + " " +
                str(self.sys.exc_info()[1]) ,
                1)



    def importCsv(self, path, collName=None, print=print):
        try:
            if(self.db != None):
                collName = collName if collName is not None else self.mongoCollName
                df = self.pd.read_csv(path)
                # to make life easier find all columns that are constant by name
                constColumns = (df != df.iloc[0]).any() != True
                # first element in constant columns as dictionary
                constData = df.loc[0, constColumns]
                # slightly counter intuitive loop that changes all constant columns from
                # their original pandas types E.g np.int64 to int
                counter = 0
                for i in constData:
                    try:
                        constData.iloc[counter] = i.item()
                    except:
                        None
                    counter = counter + 1
                constData = constData.to_dict()
                # remove the constant data in dataframe now that it has been saved
                df = df.loc[:, constColumns != True]
                # constData = self.json.loads(self.json.dumps(constData))
                dataDict = self.json.loads(df.to_json(orient='table'))
                del dataDict["schema"] # removing dict key that was created without desire by funcs
                dataDict.update(constData)
                collection = self.db[collName]
                collection.insert_one(dataDict)
            else:
                raise RuntimeError(self.prePend +
                    " please connect to database using <you're Mongo() object>.connect()")

        except:
            print("could not import csv: " + path + "\n" +
                str(self.sys.exc_info()[0]) + " " +
                str(self.sys.exc_info()[1]) ,
            2)



    def existanceCheck(self, collName=None):
        # check that db connected
        if (self.db != None):
            nameToCheck = collName if collName is not None else self.mongoCollName

            # display collections
            print(self.prePend, self.db.collection_names())
            if( nameToCheck in self.db.collection_names() ):
                return 1    # if collection exists
            return 0        # if collection does not exist

        else:
            print(self.prePend,
                  "please connect to database using <you're Mongo() object>.connect()")
            return 0



# # # # # # TODO: Everything below this line needs updating



    def getData(self, pipeline=None, query=None, collName=None, findOne=False):
        collName = collName if collName is not None else self.mongoCollName

        # check that db connected
        if (self.db != None):

            # check which args are present and call relevant funcs
            if  (findOne == True):
                return self._getDataFindOne(query=query, collName=collName)
            elif(pipeline != None) and (query == None):  # if pipeline used
                return self._getDataThroughPipe(pipeline=pipeline, collName=collName)
            elif(pipeline == None) and (query != None):  # if query used
                return self._getDataThroughFilter(query=query, collName=collName)
            else:
                print(self.prePend,
                      'please provide either a pipeline or query argument')
                return -1
        else:
            print(self.prePend,
                  "please connect to database using <your Mongo() object>.connect()")
            return 0



    def _getDataThroughPipe(self, pipeline, collName):
        collection = self.db[collName]
        return collection.aggregate(pipeline, allowDiskUse=True)



    def _getDataThroughFilter(self, query, collName):
        collection = self.db[collName]
        return collection.find(query)



    def _getDataFindOne(self, query, collName):
        collection = self.db[collName]
        return collection.find_one(query)



    def getMostRecent(self, query=None, collName=None):
        collName = collName if collName is not None else self.mongoCollName
        collection = self.db[collName]
        return collection.find(query).limit(1).sort([("_id", -1)])



    def shoveJson(self, dict, collName=None):
        if(self.db != None):
            collName = collName if collName is not None else self.mongoCollName
            collection = self.db[collName]
            collection.insert_one(dict)



    def setData(self, data, collName=None):

        if(self.db != None):
            destinationCollection = collName if collName is not None else self.mongoCollName
            # set up collection connection
            collection = self.db[destinationCollection]

            # transform data to json
            jsonPayload = self.json.loads(data.to_json(orient='table'))

            # insert json data
            collection.insert_one(jsonPayload)
        else:
            print(self.prePend,
                  "please connect to database using <your Mongo() object>.connect()")



if __name__ == "__main__":

    import pandas as pd
    #TODO: add unit tests here
