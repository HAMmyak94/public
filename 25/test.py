import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings as s


def test_show_my_pets(selenium):
    # Переходим на страницу авторизации
    pytest.driver.get(s.url + 'login')

    # Устанавливаем явное ожидание появления поля 'email'
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))

    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys(s.valid_email)
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys(s.valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector(s.css_my_pets_submit).click()

    # Устанавливаем явное ожидание появления navbar
    WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.XPATH, s.xpath_navbar_my_pets)))

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
    # Нажимаем на кнопку "Мои питомцы"
    pytest.driver.find_element_by_xpath(s.xpath_navbar_my_pets).click()

    # Устанавливаем явное ожидание появления таблицы
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'all_my_pets')))

    pet_images = pytest.driver.find_elements_by_css_selector(s.css_my_pets_images)
    pet_names = pytest.driver.find_elements_by_css_selector(s.css_my_pets_names)
    pet_types = pytest.driver.find_elements_by_css_selector(s.css_my_pets_types)
    pet_ages = pytest.driver.find_elements_by_css_selector(s.css_my_pets_ages)
    pet_numbers = pytest.driver.find_elements_by_css_selector(s.css_my_pets_stat)[0].text.split('\n')[1].split(' ')[1]

    # Проверяем все-ли питомцы есть в таблице
    assert int(pet_numbers) == len(pet_names)

    pet_this_photo = 0
    list_pet_names = []
    list_pets = {}
    for i in range(len(pet_names)):
        # Считаем количество питомцев с фото
        pet_this_photo += 0 if pet_images[i].get_attribute('src') == "" else 1

        # Проверяем, что у всех питомцев есть имя, порода и возраст
        assert pet_names[i].text != ''
        assert pet_types[i].text != ''
        assert pet_ages[i].text != ''

        # Создаем список неповторяющихся имён питомцев
        if pet_names[i].text not in list_pet_names:
            list_pet_names.append(pet_names[i].text)

        # Создаем словарь неповторяющихся питомцев
        list_pets.update({pet_names[i].text + pet_types[i].text + pet_ages[i].text: (
            pet_names[i].text, pet_types[i].text, pet_ages[i].text)})

    # Проверяем, что питомцев с фото не меньше половины
    assert pet_this_photo >= (int(pet_numbers) + 1) // 2

    # Проверяем, что все имена питомцев различны (количество неповторяющихся имен = кол-ву питомцев)
    assert len(list_pet_names) == int(pet_numbers)

    # Проверяем, что в списке нет повторяющихся питомцев (кол-во в словаре = общему кол-ву питомцев)
    assert len(list_pets) == int(pet_numbers)
