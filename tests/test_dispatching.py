"""
Dispatching tests.
"""

import pytest

from TestSuite_PytestParameterization.globals import CONFIGURATIONS, MACHINES


pytestmark = pytest.mark.dispatching_tests


# fixtures

@pytest.fixture()
def setup_dispatching(machine):
    """
    Setup and teardown fixture for all the dispatching tests.
    :param machine: global machine fixture
    :return: machine: current machine to run all tests over
    """
    # setup some crap (note, decided that a teardown is not needed here)
    return machine


# tests

@pytest.mark.parametrize("some_setting", [
    "some_value1",
    "some_value2"
])
@pytest.mark.parametrize("another_setting", [
    "another_value1",
    pytest.mark.skipif(True, reason="a bug for another_value2")("another_value2"),
    "another_value3"
])
def test_dispatch1(setup_dispatching, some_setting, another_setting):
    """
    Parameterized test over two sets of settings.
    :param some_setting: some setting
    :param another_setting: another setting
    """
    # test some crap
    pass


def test_dispatch2(machine):
    """
    Test dispatching number 2.
    """
    print "The machine is:"
#    print pytest.config.getvalue("machine")
    print "Done printing the machine"


def test_dispatch3():
    """
    Test dispatching number 3.
    """
    print "running test dispatch 3"
