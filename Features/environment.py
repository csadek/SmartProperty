from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(30)
    context.browser.maximize_window()


def after_all(context):
    context.browser.quit()