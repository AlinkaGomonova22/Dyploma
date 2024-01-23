import requests
import allure
import pytest_check as check
import time
import json

@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Пишем тесты для метода Post")
@allure.tag("API", "GET")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "alina gomonova")
@allure.link("https://dev.example.com/", name="Website_1")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_api_1():

    url = "https://restful-booker.herokuapp.com/auth"

    payload = json.dumps({
        "username": "admin",
        "password": "password123"
    })

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.text)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200)

    with allure.step('Проверка что значение параметра token не пустое'):
        response_token = response.json()
        if 'token' in response_token:
            print(response_token['token'])
            check.is_not_none(response_token['token'])
        else :
            print('Ошибка')


@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Пишем тесты для метода GET")
@allure.tag("API", "GET")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "alina gomonova")
@allure.link("https://dev.example.com/", name="Website_1")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_api_2():
    url = "https://restful-booker.herokuapp.com/booking"

    payload = {}
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200)

    with allure.step('Проверка метода'):
        check.equal(response.request.method, 'GET')

    with allure.step('Проверка что bookingid не пустой'):
        response_bookingid_one = response.json()[0]
        if 'bookingid' in response_bookingid_one:
            print(response_bookingid_one['bookingid'])
            check.is_not_none(response_bookingid_one['bookingid'])
        else:
            print('Ошибка')

    with allure.step('Проверка что bookingid не пустой'):
        response_bookingid = response.json()
        for book in response_bookingid:
            if 'bookingid' in book == 1172:
                pass
            else:
                print("такой книги нет ")

@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Пишем тесты для метода GET")
@allure.tag("API", "GET")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "alina gomonova")
@allure.link("https://dev.example.com/", name="Website_1")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_api_3():
    url = "https://restful-booker.herokuapp.com/ping"

    payload = {}
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 201)

    # with allure.step('Проверка что bookingid не пустой'):
    #     response_bookingid_one = response.json()[0]
    #     if 'bookingid' in response_bookingid_one:
    #         print(response_bookingid_one['bookingid'])
    #         check.is_not_none(response_bookingid_one['bookingid'])
    #     else:
    #         print('Ошибка')
    #
    # with allure.step('Проверка что bookingid не пустой'):
    #     response_bookingid = response.json()
    #     for book in response_bookingid:
    #         if 'bookingid' in book == 1172:
    #             pass
    #         else:
    #             print("такой книги нет ")

    with allure.step('Добавить результат в отчет Allure'):
         allure.attach(str(response.status_code), name ='статус код')
         allure.attach(str(response.headers), name='headers')





