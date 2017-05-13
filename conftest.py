"""
pytest configuration file.
"""

import pytest

from globals import MACHINES


def pytest_addoption(parser):
    """
    Adds the machine command line option which defines which machines the tests will be run over.
    :param parser: built-in argparse pytest object
    """
    parser.addoption("--machines", required=True, choices=MACHINES.keys(), action="append", default=[],
                     help="input the machines the tests will be run over")


def pytest_generate_tests(metafunc):
    """
    Parameterize the whole test suite over the user defined machines from the command line
    :param metafunc: built-in pytest object
    """
    if 'machines' in metafunc.fixturenames:
        metafunc.parametrize("machines", metafunc.config.option.machines)



