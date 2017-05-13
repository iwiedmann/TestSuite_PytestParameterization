"""
pytest configuration file.
"""

import pytest

from globals import CONFIGURATIONS, MACHINES


def pytest_addoption(parser):
    """
    Adds the machine command line option which defines which machines the tests will be run over.
    :param parser: built-in argparse pytest object
    """
    available_machines = MACHINES.keys()
    parser.addoption(
        "--machines",
        required=True,
        choices=available_machines,
        action="append",
        default=[],
        help="Input the machines the tests will be run over.  Options: {machines}".format(machines=available_machines)
    )


# TODO: change to a singular "mahcine" if possible
def pytest_generate_tests(metafunc):
    """
    Parameterize the whole test suite over the user defined machines from the command line
    :param metafunc: built-in pytest object
    """
    if 'machines' in metafunc.fixturenames:
        metafunc.parametrize("machines", metafunc.config.option.machines)


@pytest.fixture(scope="session", autouse=True)
def machine_setup(machines, request):
    """
    Global setup and teardown fixture for each machine in the parameterized list of machines to run.  All tests will
    inherit this fixture and hence all tests will be run over all defined machines unless specified in the test.
    :param machines: current machine to run all tests over
    :param request: built-in pytest request object
    """
    # optional global machine setup
    if MACHINES[machines] == CONFIGURATIONS["config2"]:
        # do some global setup for config2
        pass
    # optional global machine teardown
    def teardown():
        if MACHINES[machines] == CONFIGURATIONS["config2"]:
            # do some global teardown for config2
            pass
    request.addfinalizer(teardown)
