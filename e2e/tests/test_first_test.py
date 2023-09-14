import re, pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.ab_testing_page import ABTestingPage

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://the-internet.herokuapp.com/")
    yield

def test_has_title(page: Page):
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("The Internet"))

def test_ab_testing_link(page: Page): 
    hp = HomePage(page)
    abtp = ABTestingPage(page)
    
    # Click the A/B Testing link.
    hp.ab_testing_link.click()

    # Expects page to have a heading with the name of Installation.
    expect(abtp.ab_testing_page_heading, 'AB test title is incorrect or not visible').to_be_visible()