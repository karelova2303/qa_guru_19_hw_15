"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest

from github.pages.github_page import GithubPage
from tests.conftest import desktop_only, mobile_only

page_button = GithubPage()

@desktop_only
def test_github_desktop(setup_browser):
    page_button.open_main_page()
    page_button.should_be_clickable_button_desktop()

@mobile_only
def test_github_mobile(setup_browser):
    page_button.open_main_page()
    page_button.should_be_clickable_button_mobile()
