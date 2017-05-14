"""
Dispatching tests.
"""

import pytest

from TestSuite_PytestParameterization.globals import CONFIGURATIONS, MACHINES


pytestmark = pytest.mark.dispatching_tests


# fixtures

@pytest.fixture(scope="module")
def setup_dispatching(request, setup_machine):
    """
    Setup and teardown fixture for all the dispatching tests.
    :param request: built-in pytest request object
    :param setup_machine: global machine setup fixture
    :return: machine: current machine to run all tests over
    """
    machine = setup_machine     # rename the machine from the fixture so it is clear
    # setup some crap (note, decided that a teardown is not needed here)
    return machine


# tests

@pytest.mark.parametrize("some_setting, another_setting", [
    ("some_value1", "some_value2"),
    ("another_value1", pytest.mark.skipif(True, reason="a bug for another_value2")("another_value2"), "another_value3")
])
def test_dispatch1(setup_dispatching, some_settings, some_more_settings):
    """
    Parameterized test over two sets of settings.
    :param some_setting: some setting
    :param another_setting: another setting
    """
    # test some crap
    pass


def test_charge2(setup_machine):
    """
    Test charging number 2.  Test over all machines, but only test on the CLP
    """
    # setup the CLP
    # test some crap
    # teardown the CLP
    print "The machine is:"
    print pytest.config.getvalue("machines")
    print "Done printing the machine"
