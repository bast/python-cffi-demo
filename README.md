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

These are combined in an example Python package that we call `pi`.


## Lower-level learning goals

- Approximate pi using the Monte Carlo
- Calling Fortran libraries from C(++)
- Calling C(++) libraries from Fortran
- Calling Fortran/C(++) libraries from Python using [Python CFFI](https://cffi.readthedocs.io)
- Automatically testing Fortran/C(++) libraries on Linux and Mac OS X using
  [pytest](https://docs.pytest.org) and [Travis CI](https://travis-ci.org)
- Hiding CMake infrastructure behind a simple `pip install`


## Higher-level learning goals

- Automatically test dynamic Fortran/C(++) libraries
- Write tests without recompiling the code
- Speed up your Python code
- Provide a Python API to your compiled library and leverage Python tools


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
and builds the code under the hood and makes it possible to install the demo
with `pip`:

```
virtualenv venv
source venv/bin/activate
pip install git+https://github.com/bast/python-cffi-demo.git
python -c 'import pi; print(pi.approximate_pi_c(100))'
```


## C(++) calling Fortran and vice versa

```shell
$ cd build

$ ./bin/pi_cpp.x
pi computed by c = 3.141664
pi computed by fortran = 3.141636

$ ./bin/pi_f90.x
pi computed by fortran =    3.1416358947753906
pi computed by c =    3.1416640000000000
```


## Timing the libraries through a Python interface

```shell
$ PI_BUILD_DIR=build python test.py

python  pi=3.14163 time spent: 1.755 sec
c       pi=3.14190 time spent: 0.042 sec
fortran pi=3.14225 time spent: 0.126 sec
```
