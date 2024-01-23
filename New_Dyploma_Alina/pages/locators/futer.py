import os
from New_Dyploma_Alina.pages.base_page import WebPage
from New_Dyploma_Alina.pages.elements import WebElement
from New_Dyploma_Alina.pages.elements import ManyWebElements


class FuterBtn(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("FUTER") or 'https://goldapple.by/'

        super().__init__(web_driver, url)

    # О компании
    btn_futer_about = WebElement(xpath='//footer//a[@href="https://blog.onliner.by/about"]')

    # Контакты редакции
    btn_futer_contacts = WebElement(xpath='//footer//a[@href="https://people.onliner.by/contacts"]')

    # Инпут быстрого поиска на главной страницы
    input_fast_search = WebElement(xpath='//input[@class="fast-search__input"]')

    # Вывод результата поиска
    count_fast_search_result = ManyWebElements(xpath='//li[@class="b-main-navigation__item b-main-navigation__item_arrow"]')

    # Вывод результата поиска
    btn_button = WebElement(css_selector='a[class="yt-simple-endpoint style-scope ytd-topbar-menu-button-renderer"]')

    # Вывод результата поиска
    btn_endpoint = WebElement(xpath='(//div[@id="primary-text-container"])[7]')

    # Вывод результата поиска
    btn_close = WebElement(css_selector='button[class="help-panel-header__close-button"]')

