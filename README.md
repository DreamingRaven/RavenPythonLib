# RavenPythonLib
A library of any generic and reusable code samples for use in other projects.
This was initially created by splitting the reusable classes in [Nemesyst](https://github.com/DreamingRaven/Nemesyst)

## [loggers](https://github.com/DreamingRaven/RavenPythonLib/tree/master/loggers)
Any classes that can be used as near drop in replacements for pythons in built print()
Currently only [basicLog](https://github.com/DreamingRaven/RavenPythonLib/blob/master/loggers/basicLog.py) is available which replaces print() with a logLevel system of both displaying prints at all based on thresholds and the colours of the respective prints.

## [mongodb](https://github.com/DreamingRaven/RavenPythonLib/tree/master/mongodb)
Any classes that can be used to wrap pymongo or a mongoDb interface to streamline operations. Currently only [mongo](https://github.com/DreamingRaven/RavenPythonLib/blob/master/mongodb/mongo.py) is available which encapsulates all sorts of nice functionality, E.G dumping CSV's in one command to mongoDb collections.

## [plotters](https://github.com/DreamingRaven/RavenPythonLib/tree/master/plotters)
Any classess that can be re-used as simple plotting systems, although while I was implementing these I found that the interface would almost certainly be identical to SNS, the only gain I could possibly add here are config files to make plotting simpler per-plot.

## [updaters](https://github.com/DreamingRaven/RavenPythonLib/tree/master/updaters)
Any classes that can be used to update firmware/software of whatever system these updaters are used on. Currently only [Gupdater]() is available (Git Updater) which handles both subdir dependencies in the dependency array and allows for quick updating scripts to be written.
