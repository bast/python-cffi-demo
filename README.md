[![Build Status](https://travis-ci.org/bast/python-cffi-demo.svg?branch=master)](https://travis-ci.org/bast/python-cffi-demo/builds)
[![License](https://img.shields.io/badge/license-%20MPL--v2.0-blue.svg)](../master/LICENSE)


# python-cffi-demo

Inspired by Armin Ronacher's
["Beautiful Native Libraries"](http://lucumr.pocoo.org/2013/8/18/beautiful-native-libraries/).


## Example

In this example we imagine we are on a desert island and wish to compute pi by
throwing darts:

![](../master/img/darts.jpg "darts")

This example is implemented in 3 different languages (C++, Fortran, Python) and
we demonstrate how to call this functionality across languages.


## How to configure, build, and test this demo

```
mkdir build
cd build
cmake ..
make
cd ..
PI_BUILD_DIR=build pytest -vv test.py
```


## Installing with pip

This example comes with a full-fledged setup script which configures
and builds the code under the hood and makes it possible to install the code
with `pip`:

```
virtualenv venv
source venv/bin/activate
pip install git+https://github.com/bast/python-cffi-demo.git
python -c 'import pi; print(pi.approximate_pi_c(100))'
```
