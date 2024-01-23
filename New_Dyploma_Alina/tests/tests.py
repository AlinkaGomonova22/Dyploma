import time

import pytest_check as check
import allure

from New_Dyploma_Alina.pages.locators.header_locators import Header
from New_Dyploma_Alina.conftest import web_browser

@allure.feature('Смоук тест')
@allure.story('Поиск продукта и проверка его отображения')
def test_click_header(web_browser):
    """ Убеждаемся, что ссылки/кнопки футера
        кликабельные и переход на страницу корректный. """

    page = Header(web_browser)

    with allure.step("Проверка кнопки Поиск'"):
        page.search_button.click()


    # with allure.step("Проверка кнопки Поиск'"):
    #     if check.equal(page.btn_futer_about.get_text(), 'О компании')
    #         check.equal(page.btn_futer_about.get_attribute('href'), 'https://blog.onliner.by/about')
    #         page1 = page.get_current_url()
    #         page.btn_futer_about.click(1)
    #         check.equal(page1, page.get_current_url())
    #         check.is_true(page.btn_futer_about.wait_for_visibility())
    #         check.is_true(page.btn_futer_about.wait_to_be_clickable())
    #
    # with allure.step("Проверка кнопки 'Контакты редакции'"):
    #     if check.equal(page.btn_futer_contacts.get_text(), 'Контакты редакции'):
    #         check.equal(page.btn_futer_contacts.get_attribute('href'), 'https://people.onliner.by/contacts')
    #         page1 = page.get_current_url()
    #         page.btn_futer_contacts.click(1)
    #         check.equal(page1, page.get_current_url())
    #         check.is_true(page.btn_futer_contacts.wait_for_visibility())
    #         check.is_true(page.btn_futer_contacts.wait_to_be_clickable())