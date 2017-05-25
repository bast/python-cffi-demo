[![Build Status](https://travis-ci.org/bast/python-cffi-demo.svg?branch=master)](https://travis-ci.org/bast/python-cffi-demo/builds)
[![License](https://img.shields.io/badge/license-%20MPL--v2.0-blue.svg)](../master/LICENSE)


# python-cffi-demo

- Inspired by Armin Ronacher's ["Beautiful Native Libraries"](http://lucumr.pocoo.org/2013/8/18/beautiful-native-libraries/)

![](https://github.com/bast/python-cffi-demo/raw/master/img/darts.jpg "darts")


## How to build this demo

```
mkdir build
cd build
cmake ..
make
cd ..
PI_BUILD_DIR=build pytest -vv test.py
```
