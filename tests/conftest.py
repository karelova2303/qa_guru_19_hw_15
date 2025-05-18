import pytest
from selene import browser


@pytest.fixture()
def mobile_setup_browser():
    browser.config.window_width = '400'
    browser.config.window_height = '634'

    yield

    browser.quit()


@pytest.fixture()
def desktop_setup_browser():
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'

    yield

    browser.quit()


@pytest.fixture(params=['mobile', 'desktop'])
def setup_browser(request):
    if request.param == 'mobile':
        browser.config.window_width = '400'
        browser.config.window_height = '634'

    if request.param == 'desktop':
        browser.config.window_width = '1920'
        browser.config.window_height = '1080'

    yield

    browser.quit()


desktop_only = pytest.mark.parametrize('setup_browser', ['desktop'], indirect=True)
mobile_only = pytest.mark.parametrize('setup_browser', ['mobile'], indirect=True)

screen_size = [(400, 634), (360, 740), (1920, 1080), (1366, 768)]

@pytest.fixture(params=screen_size)
def open_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width < height:
        yield 'mobile'
    else:
        yield 'desktop'


    browser.quit()
