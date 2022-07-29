from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings as s



def test_show_my_pets(driver):
    driver.set_window_size(1024, 768)
    driver.get(s.url + 'login')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    driver.find_element_by_id('email').send_keys(s.valid_email)
    driver.find_element_by_id('pass').send_keys(s.valid_password)
    driver.find_element_by_css_selector(s.pets_submit).click()
    driver.find_element_by_xpath(s.navbar_my_pets).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'all_my_pets')))

    pet_images = driver.find_elements_by_css_selector(s.pets_images)
    pet_names = driver.find_elements_by_css_selector(s.pets_names)
    pet_types = driver.find_elements_by_css_selector(s.pets_types)
    pet_ages = driver.find_elements_by_css_selector(s.pets_ages)
    pet_numbers = driver.find_elements_by_css_selector(s.pets_stat)[0].text.split('\n')[1].split(' ')[1]

    assert int(pet_numbers) == len(pet_names)

    pet_this_photo = 0
    list_pet_names = []
    for i in range(len(pet_names)):
        pet_this_photo += 0 if pet_images[i].get_attribute('src') == "" else 1

        assert pet_names[i].text != ''
        assert pet_types[i].text != ''
        assert pet_ages[i].text != ''

        if pet_names[i].text not in list_pet_names:
            list_pet_names.append(pet_names[i].text)

        assert pet_this_photo >= (int(pet_numbers) + 1) // 2

        assert len(list_pet_names) == int(pet_numbers)