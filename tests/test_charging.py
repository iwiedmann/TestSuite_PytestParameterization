"""
Tests for the Sunverge about us page.
"""

import pytest
import testfixtures

from TestSuite_ProofOfConcept.pages.about_us_page import AboutUsPage


pytestmark = pytest.mark.about_us_page_tests


# fixtures

@pytest.fixture
def setup_about_us_page(selenium):
    """
    Setup fixture to directly navigate to the about us page and check that it loaded correctly.
    :param selenium: pytest-selenium fixture
    :return: about_us_pg: object for the about us page
    """
    about_us_pg = AboutUsPage(selenium)
    about_us_pg.go_to_about_us_page()
    return about_us_pg


# tests

@pytest.mark.parametrize("sub_menu_link_locator", AboutUsPage.get_sub_menu_link_locator_names())
def test_sub_menu_navigation_bar(setup_about_us_page, sub_menu_link_locator):
    """
    Parameterized test to test all the links in the green sub menu navigation bar.  Each link is clicked and then it is
    checked that all the sections are still visible.
    TODO: A possibly better test (or possibly worse) might check that the page scrolled to the correct section after
    clicking each link; however, this test could be fragile depending on browsers and window size.
    :param sub_menu_link_locator: each sub menu link locator to run a test for
    """
    about_us_pg = setup_about_us_page
    # scroll to the bottom of the page so that the sub menu navigation bar is always on screen, the link clicking won't
    # work properly otherwise
    about_us_pg.scroll_to_bottom()
    # click the link
    about_us_pg.click_sub_menu_link_locator(sub_menu_link_locator)
    # check the results
    expected_visibility_results = about_us_pg.expect_all_sections_visible
    visibility_results = about_us_pg.check_all_sections_visibility()
    testfixtures.compare(
        expected_visibility_results, visibility_results, prefix="There are about us page sections that are not visible"
    )
