from selene import browser, have


class GithubPage():
    def __init__(self):
        self.button_sign_up = browser.element('.HeaderMenu-link--sign-up')
        self.button_content = browser.element('.Button-content')
        self.auth_form_header = browser.element(' #signup-form-fields')

    def open_main_page(self):
        browser.open('https://github.com')

    def should_be_clickable_button_desktop(self):
        self.button_sign_up.click()
        self.auth_form_header.should(have.exact_text('Sign up to GitHub'))

    def should_be_clickable_button_mobile(self):
        self.button_content.click()
        self.button_sign_up.click()
        self.auth_form_header.should(have.exact_text('Sign up to GitHub'))
