# TestSuite_ProofOfConcept
Test suite to showcase pytest parameterization concepts.

## Requirements
Requirements needed before test suite installation.

### The basics
Install and setup the latest versions of the following if you haven't
already:
* [Python 2.x with pip and setuptools](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)

### Upgrade pip and setuptools
```bash
$ pip install --upgrade pip setuptools
```

### Python virtualenv package
Install the [virtualenv](https://virtualenv.pypa.io/en/stable/) package if
you haven't already:
```bash
$ sudo pip install virtualenv
```

## Install the test suite
Clone and install the test suite.

### Clone
If you haven't already, then
[clone](https://help.github.com/articles/cloning-a-repository/) this repository.

### Navigate to the test directory
```bash
$ cd TestSuite_PytestParameterization
```

### Create a Python virtual environment
```bash
$ virtualenv venv
```

### Activate the Python virtual environment
```bash
$ . venv/bin/activate
```
You should see `(venv)` at the start of your command prompt.  Verify that the
Python path is to your virtual environment:
```bash
$ which python
```

### Install the required test suite Python packages
```bash
$ pip install -r requirements.txt
```

## Run the test suite
There are many ways to run tests with
[pytest](http://doc.pytest.org/en/latest/contents.html), but here are the basics
for this test suite.  Make sure your virtual environment is activated before
running tests:
```bash
$ . venv/bin/activate
```
Deactivate the virtual environment if you move out of the test suite directory:
```bash
$ deactivate 
```

### Run all the tests
```bash
$ pytest --machine all
```

### Run a set of marked tests
Run all the charging tests:
```bash
$ pytest --machine all -m charging_tests
```

### Run a single test
Run just the test `TBD()`:
```bash
$ pytest --machine m2 -k "TBD"
```
