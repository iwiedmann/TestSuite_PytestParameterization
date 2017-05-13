# TestSuite_ProofOfConcept
Test suite to showcase basic selenium and pytest concepts.

##### Note:
These instructions are for installing and running the test suite on Ubuntu using
Firefox.  It should work on other operating systems, but this has not been
tested.

## Requirements
Requirements needed before test suite installation.

### The basics
Install and setup the latest versions of the following if you haven't
already:
* [Python 2.x with pip and setuptools](https://www.python.org/downloads/)
* [Firefox](https://www.mozilla.org/en-US/firefox/new/)
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

### GeckoDriver
Selenium needs GeckoDriver installed in order to work with the latest version
of Firefox.
* [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)
* Unzip the downloaded file:
```bash
$ tar -xvzf geckodriver<version>.tar.gz
```
* Move `geckodriver` to the `/usr/local/bin` directory to put it in your
`PATH`:
```bash
$ sudo mv geckodriver /usr/local/bin
```

## Install the test suite
Clone and install the test suite.

### Clone
If you haven't already, then
[clone](https://help.github.com/articles/cloning-a-repository/) this repository.

### Navigate to the test directory
```bash
$ cd TestSuite_ProofOfConcept
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
$ pytest --driver Firefox
```

### Run a set of marked tests
Run all the home page tests:
```bash
$ pytest --driver Firefox -m home_page_tests
```
Run all the about us page tests:
```bash
$ pytest --driver Firefox -m about_us_page_tests
```

### Run a single test
Run just the test `test_navigate_to_about_us_page()`:
```bash
$ pytest --driver Firefox -k "test_navigate_to_about_us_page"
```
