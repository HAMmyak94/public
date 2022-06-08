from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_with_invalid_email(email='WrongWay@mail.ru', password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    print("\nНеверный логин\пароль")


def test_get_api_key_with_invalid_password(email=valid_email, password="invalid_password"):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    print("\nНеверный логин\пароль")


def test_add_new_pet_with_empty_name(name='', animal_type='Cat', age='3',
                                      pet_photo='images/P1040103.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    print("\nВводятся неверные данные")


def test_add_new_pet_with_invalid_age(name='Boris', animal_type='Cat', age='текствместосимвола',
                                      pet_photo='images/P1040103.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    print("\nВводятся неверные данные")


def test_add_new_pet_with_long_age(name='Boris', animal_type='Cat', age='7777777', pet_photo='images/P1040103.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    print("\nВводятся неверные данные")


def test_update_pet_info_with_empty_name(name='', animal_type='mouse', age=2):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] != name
        print("\nИмя питомца не изменено")


def test_update_pet_info_without_photo(pet_photo='images/несуществующеефото.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        print("\nДанные изменены")


def test_update_pet_info_with_numeric_animal_type(name='Larry', animal_type='41241', age=2):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
        print("\nДанные изменены")


def test_update_pet_info_with_long_name(name='Larry was a wild hog', animal_type='', age=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
        print("\nДанные изменены")


def test_update_pet_info_with_long_animal_type(name='', animal_type='who have a twenty-five years old motorcycle', age=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        print("\nДанные изменены")


def test_update_pet_info_with_long_text_age(name='', animal_type='', age='and "Want to break free!" (пропеть как Queen)'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        print("\nДанные изменены")
