"""
pytest configuration file.
"""

import pytest

from globals import CONFIGURATIONS, MACHINES


def pytest_addoption(parser):
    """
    Adds the "--machine" command line option which defines which machine the tests will be run over.  Multiple machines
    can be run by repeating the "--machine" option with another machine.
    :param parser: built-in argparse pytest object
    """
    available_machines = MACHINES.keys()
    parser.addoption(
        "--machine",
        required=True,
        choices=available_machines,
        action="append",
        default=[],
        help="Input the machines the tests will be run over.  Options: {machines}.".format(machines=available_machines)
    )


def pytest_generate_tests(metafunc):
    """
    Parameterize the whole test suite over the user defined machines from the command line
    :param metafunc: built-in pytest object
    """
    if "machine" in metafunc.fixturenames:
        metafunc.parametrize("machine", metafunc.config.option.machine)


@pytest.fixture(scope="session")
def machine(request):
    """
    Global setup and teardown fixture for each machine in the parameterized list of machines to run.  All tests that
    inherit this fixture will be run over all defined machines unless specified in the test.
    :param request: built-in pytest request object
    :return: machine: current machine to run all tests over
    """
    machine = request.param
    # optional global machine setup
    if MACHINES[machine] == CONFIGURATIONS["config2"]:
        # do some global setup for config2
        pass
    # optional global machine teardown
    def teardown():
        if MACHINES[machine] == CONFIGURATIONS["config2"]:
            # do some global teardown for config2
            pass
    request.addfinalizer(teardown)
    return machine
