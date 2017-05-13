"""
Tests for the Sunverge corporate home page.
"""

import pytest

from TestSuite_ProofOfConcept.pages.home_page import HomePage


pytestmark = pytest.mark.home_page_tests


# fixtures

@pytest.fixture
def setup_home_page(selenium):
    """
    Setup fixture to directly navigate to the Sunverge home page and check that it loaded correctly.
    :param selenium: pytest-selenium fixture
    :return: home_pg: object for the home page
    """
    home_pg = HomePage(selenium)
    home_pg.go_to_home_page()
    return home_pg


# tests

def test_sunverge_logo(setup_home_page):
    """
    Test that the Sunverge logo is visible.
    """
    home_pg = setup_home_page
    assert home_pg.is_sunverge_logo_visible(), "Sunverge logo is not visible"


def test_navigate_to_about_us_page(setup_home_page):
    """
    Test that you can navigate to the about us page through the link.
    """
    home_pg = setup_home_page
    about_us_pg = home_pg.go_to_about_us_page()
    about_us_pg.check_page_title()
