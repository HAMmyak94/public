"""Задание 25.3.1
Написать тест, который проверяет, что на странице со списком питомцев пользователя:

Присутствуют все питомцы.
Хотя бы у половины питомцев есть фото.
У всех питомцев есть имя, возраст и порода.
У всех питомцев разные имена.
В списке нет повторяющихся питомцев. (Сложное задание).
Подсказки для решения
Количество питомцев взято из статистики пользователя.

Количество питомцев с фото тоже можно посчитать, взяв статистику пользователя.
Необходимо собрать в массив имена питомцев.
Повторяющиеся питомцы — это питомцы, у которых одинаковое имя, порода и возраст.
Вопросы для самопроверки
Количество строк таблицы соответствует количеству питомцев в блоке статистики пользователя?
При изменении количества проверяемых строк таблицы тест из задания 1 падает?
Половина от чётного и нечётного количества фотографий выдаёт одинаковые результаты теста?
При добавлении питомца с повторяющимся именем все тесты проходят?
При добавлении питомца с повторяющимся именем, породой или возрастом все тесты проходят?

Задание 25.5.1.
В написанном тесте (проверка карточек питомцев) добавьте неявные ожидания всех элементов (фото, имя питомца, его возраст).
В написанном тесте (проверка таблицы питомцев) добавьте явные ожидания элементов страницы.
Чеклист для самопроверки:

 В тестах используется настройка implicitly-wait веб-драйвера.

 В тестах используются элементы класса WebDriverWait."""


"""
def test_petfriends(selenium):
    
    # Open PetFriends base page:
    selenium.get("https://petfriends1.herokuapp.com/")

    # Find the field for search text input:
    btn_newuser = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    btn_exist_acc = selenium.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    field_email = selenium.find_element_by_id("email")
    field_email.click()
    field_email.clear()
    field_email.send_keys("isaid.zx@gmail.com")

    field_pass = selenium.find_element_by_id("pass")
    field_pass.click()
    field_pass.clear()
    field_pass.send_keys("qwerty1234")

    btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    # Save cookies of the browser after the login
    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(selenium.get_cookies(), cookies)

    # Make the screenshot of browser window:
    selenium.save_screenshot('result_petfriends.png')"""

from selenium.webdriver.common.keys import Keys


def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open google search page:
    selenium.get('https://google.com')

    # Find the field for search text input:
    search_input = selenium.find_element_by_name('q')

    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test')

    # Click Search:
    selenium.find_element_by_name("q").send_keys(Keys.RETURN)

    # Make the screenshot of browser window:
    selenium.save_screenshot('result.png')


