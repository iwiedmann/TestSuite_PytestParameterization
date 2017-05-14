"""
Charging tests.
"""

import pytest
import testfixtures

from TestSuite_PytestParameterization.globals import CONFIGURATIONS, MACHINES


pytestmark = pytest.mark.charging_tests


# fixtures

@pytest.fixture(params=["CLP", "MLP"])
def setup_charging(machine, request):
    """
    Setup and teardown fixture for all the charging tests.  All tests are parameterized over the CLP and MLP.
    :param machine: global machine fixture
    :param request: built-in pytest request object
    :return: machine: current machine to run all tests over
    """
    # setup the load
    load_type = request.param
    if load_type == "CLP":
        # do some setup crap
        pass
    elif load_type == "MLP":
        # do some setup crap
        pass

    # optional machine setup
    if MACHINES[machine] == CONFIGURATIONS["config1"]:
        # do some setup for config1
        pass

    # teardown
    def teardown():
        # teardown the load
        # optional machine teardown
        if MACHINES[machine] == CONFIGURATIONS["config1"]:
            # do some teardown for config1
            pass
    request.addfinalizer(teardown)
    return machine


# tests

@pytest.mark.parametrize("power, expected_output", [
    ("1000W", 800),
    ("1500W", 1300)
])
def test_charge1(setup_charging, power, expected_output):
    """
    Parameterized test to test charging under different load powers.
    :param power: load power
    :param expected_output: expected result
    """
    output = 0
    # do some stuff
    if power == "1000W":
        output = 800
    elif power == "1500W":
        output = 1300
    # check the result
    testfixtures.compare(expected_output, output, prefix="The output for {power} is not correct".format(power=power))


def test_charge2(machine):
    """
    Test charging number 2.  Test over all machines, but only test on the CLP
    """
    # setup the CLP
    # test some crap
    # teardown the CLP
    pass
