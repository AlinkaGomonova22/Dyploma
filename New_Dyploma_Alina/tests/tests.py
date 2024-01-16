import time

import pytest_check as check
import allure

from maksim_tsybulko.class_work.example.diplom.pages.locators.futer_page_locators import FuterBtn
from maksim_tsybulko.class_work.example.diplom.conftest import web_browser

@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопок футера')
def test_click_futer_btn(web_browser):
    """ Убеждаемся, что ссылки/кнопки футера
        кликабельные и переход на страницу корректный. """

    page = FuterBtn(web_browser)

    with allure.step("Проверка кнопки 'О компании'"):
        if check.equal(page.btn_futer_about.get_text(), 'О компании'):
            check.equal(page.btn_futer_about.get_attribute('href'), 'https://blog.onliner.by/about')
            page1 = page.get_current_url()
            page.btn_futer_about.click(1)
            check.equal(page1, page.get_current_url())
            check.is_true(page.btn_futer_about.wait_for_visibility())
            check.is_true(page.btn_futer_about.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Контакты редакции'"):
        if check.equal(page.btn_futer_contacts.get_text(), 'Контакты редакции'):
            check.equal(page.btn_futer_contacts.get_attribute('href'), 'https://people.onliner.by/contacts')
            page1 = page.get_current_url()
            page.btn_futer_contacts.click(1)
            check.equal(page1, page.get_current_url())
            check.is_true(page.btn_futer_contacts.wait_for_visibility())
            check.is_true(page.btn_futer_contacts.wait_to_be_clickable())