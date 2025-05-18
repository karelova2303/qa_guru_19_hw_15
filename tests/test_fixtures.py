"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from github_click_button.pages.page_button import PageButton

page_button = PageButton()


def test_github_desktop(desktop_setup_browser):
    page_button.open_main_page()
    page_button.should_be_clickable_button_desktop()


def test_github_mobile(mobile_setup_browser):
    page_button.open_main_page()
    page_button.should_be_clickable_button_mobile()
