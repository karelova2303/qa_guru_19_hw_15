"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest

from github.pages.github_page import GithubPage

page_button = GithubPage()


def test_github_desktop(open_browser):
    if open_browser == 'mobile':
        pytest.skip(reason='Pазрешение экрана для мобильных тестов')
    page_button.open_main_page()
    page_button.should_be_clickable_button_desktop()

def test_github_mobile(open_browser):
    if open_browser == 'desktop':
        pytest.skip(reason='Pазрешение экрана для десктопных тестов')
    page_button.open_main_page()
    page_button.should_be_clickable_button_mobile()




