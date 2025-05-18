"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest

from github_click_button.pages.page_button import PageButton
from tests.conftest import desktop_only, mobile_only

page_button = PageButton()

@desktop_only
def test_github_desktop(setup_browser):
    page_button.open_main_page()
    page_button.should_be_clickable_button_desktop()

@mobile_only
def test_github_mobile(setup_browser):
    page_button.open_main_page()
    page_button.should_be_clickable_button_mobile()
