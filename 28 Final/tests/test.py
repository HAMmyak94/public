import time
from selenium.webdriver.common.keys import Keys
import settings as s
from selenium.webdriver import ActionChains
from pages.main_page import MainPage


# тестируем хэдер
# тест на авторизацию по связке логин-пароль
def test_successful_auth(web_browser):
    page = MainPage(web_browser)
    web_browser.implicitly_wait(3)
    page.login.click()
    page.email.send_keys(s.email)
    web_browser.find_element_by_id("g-recap-0-btn").click()
    page.passw.send_keys(s.passw)
    web_browser.find_elements_by_xpath('//input[contains(@value, "Проверить код и войти")]')[2].click()
    web_browser.find_element_by_xpath('//form[@id="auth-success-login"]/input[2]').click()
    page.login.click()
    assert page.get_current_url() == "https://www.labirint.ru/cabinet/"


# тест на авторизацию по коду скидки
def test_successful_auth_with_code(web_browser):
    page = MainPage(web_browser)
    web_browser.implicitly_wait(3)
    page.login.click()
    page.email.send_keys(s.passw)
    web_browser.find_element_by_id("g-recap-0-btn").click()
    web_browser.find_element_by_xpath('//form[@id="auth-success-login"]/input[2]').click()
    page.login.click()
    assert page.get_current_url() == "https://www.labirint.ru/cabinet/"


# негативный тест на авторизацию
def test_unsuccessful_auth(web_browser):
    page = MainPage(web_browser)
    web_browser.implicitly_wait(3)
    page.login.click()
    page.email.send_keys("SomeStrangeWords")
    web_browser.find_element_by_id("g-recap-0-btn").click()
    web_browser.find_element_by_xpath("//*[contains(text(),'Введенного кода не существует')]").is_displayed()


# тест перехода на главную страницу
def test_logo_click(web_browser):
    page = MainPage(web_browser)
    page.logo.click()
    assert page.get_current_url() == 'https://www.labirint.ru/'


# тест перехода в сообщения
def test_messages_click(web_browser):
    page = MainPage(web_browser)
    page.messages.click()
    assert web_browser.find_element_by_xpath('//*[@id="auth-by-code"]').is_displayed()


# тест перехода в Мой Лаб
def test_mylab_click(web_browser):
    page = MainPage(web_browser)
    page.mylab.click()
    assert page.login


# тест перехода в Отложено
def test_postponed_click(web_browser):
    page = MainPage(web_browser)
    page.putorder.click()
    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


# тест перехода в Корзина
def test_cart_click(web_browser):
    page = MainPage(web_browser)
    page.cart.click()
    assert page.get_current_url() == 'https://www.labirint.ru/cart/'


# тест перехода в Доставка и оплата
def test_help_click(web_browser):
    page = MainPage(web_browser)
    page.help.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/'


# тест перехода в Сертификаты
def test_certificates_click(web_browser):
    page = MainPage(web_browser)
    page.certificates.click()
    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'


# тест перехода в Рейтинги
def test_rating_click(web_browser):
    page = MainPage(web_browser)
    page.rating.click()
    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'


# тест перехода в Новинки
def test_novelty_click(web_browser):
    page = MainPage(web_browser)
    page.novelty.click()
    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'


# тест перехода в Скидки
def test_sale_click(web_browser):
    page = MainPage(web_browser)
    page.sale.click()
    assert page.get_current_url() == 'https://www.labirint.ru/search/' \
                                     '?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'


# тест перехода в Контакты
def test_contact_click(web_browser):
    page = MainPage(web_browser)
    page.contact.click()
    assert page.get_current_url() == 'https://www.labirint.ru/contact/'


# тест перехода в Поддержка
def test_support_click(web_browser):
    page = MainPage(web_browser)
    page.support.click()
    assert page.get_current_url() == 'https://www.labirint.ru/support/'


# тест перехода в Пункты самовывоза
def test_maps_click(web_browser):
    page = MainPage(web_browser)
    page.maps.click()
    assert page.get_current_url() == 'https://www.labirint.ru/maps/'


# тестируем поиск
# тестируем поиск по одному слову на английском
def test_one_eng_word_search(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys("london")
    page.search_run_button.click()
    title = page.page_title.get_text()
    assert title == 'Все, что мы нашли в Лабиринте по запросу «london»'


# тестируем поиск по одному слову на русском
def test_one_rus_word_search(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys("брэдбери")
    page.search_run_button.click()
    title = page.page_title.get_text()
    assert title == 'Все, что мы нашли в Лабиринте по запросу «брэдбери»'


# тестируем поиск по нескольким словам
def test_search_few_words(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys("ричард длинные руки")
    page.search_run_button.click()
    title = page.page_title.get_text()
    assert title == 'Все, что мы нашли в Лабиринте по запросу «ричард длинные руки»'


# тестируем поиск с цифрами
def test_search_with_numbers(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys("3 билборда")
    page.search_run_button.click()
    title = page.page_title.get_text()
    assert title == 'Все, что мы нашли в Лабиринте по запросу «3 билборда»'


# тестируем поиск с символами    
def test_search_with_symbols(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys("&#@!$%")
    page.search_run_button.click()
    title = page.page_title.get_text()
    assert title == 'Мы ничего не нашли по вашему запросу! Что делать?'


# тестируем поиск с ошибкой
def test_search_with_mistake(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys("wondows")
    page.search_run_button.click()
    title = page.page_title.get_text()
    assert title == 'Все, что мы нашли в Лабиринте по запросу «windows»'


# тестируем поиск с несуществующим словом
def test_search_with_wrong_word(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys("sfsdgsdag")
    page.search_run_button.click()
    title = page.page_title.get_text()
    assert title == 'Мы ничего не нашли по вашему запросу! Что делать?'


# тестируем Корзину и Отложенное
# проверка, что корзина пуста
def test_empty_cart(web_browser):
    page = MainPage(web_browser)
    count = web_browser.find_element_by_xpath('//span[@class="b-header-b-personal-e-icon-count-m-cart '
                                              'basket-in-cart-a"]').text
    assert int(count) == 0


# проверка, что Отложенное пусто
def test_empty_putorder(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_xpath('//span[@class="b-header-b-personal-e-icon-count-m-putorder '
                                      'basket-in-dreambox-a hidden-force"]').is_enabled()


# тест добавления в корзину
def test_add_book_in_cart(web_browser):
    page = MainPage(web_browser)
    web_browser.implicitly_wait(3)
    page.search.send_keys("брэдбери")
    page.search_run_button.click()
    count = web_browser.find_element_by_xpath('//span[@class="b-header-b-personal-e-icon-count-m-cart '
                                              'basket-in-cart-a"]').text
    assert int(count) == 0
    page.add_book.click()
    # вынужден добавить таймслип, так как ожидания не отрабатывают изменения текста
    time.sleep(0.5)
    count = web_browser.find_element_by_xpath('//span[@class="b-header-b-personal-e-icon-count-m-cart '
                                              'basket-in-cart-a"]').text
    assert int(count) == 1


# тест оформления заказа
def test_checkout(web_browser):
    page = MainPage(web_browser)
    web_browser.implicitly_wait(3)
    test_add_book_in_cart(web_browser)
    web_browser.find_element_by_xpath('//a[@class ="b-basket-popinfo-close"]').click()
    web_browser.find_element_by_tag_name('html').send_keys(Keys.HOME)
    hoverable = web_browser.find_element_by_xpath('//*[@data-event-type="16"]')
    ActionChains(web_browser).move_to_element(hoverable).perform()
    page.buy.click()
    page.cookie_button.click()
    page.checkout_button.click()


# тест добавления в Отложенное
def test_add_book_in_putorder(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys("лондон")
    page.search_run_button.click()
    web_browser.find_element_by_xpath('//span[@class="b-header-b-personal-e-icon-count-m-putorder '
                                      'basket-in-dreambox-a hidden-force"]').is_enabled()
    page.add_putorder.click()
    time.sleep(0.5)
    count = web_browser.find_element_by_xpath('//span[@class="b-header-b-personal-e-icon-count-m-putorder '
                                              'basket-in-dreambox-a"]').text
    assert int(count) == 1


# тест функции Написать рецензию
def test_add_review(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys("лондон")
    page.search_run_button.click()
    page.else_button.click()
    page.review_button.click()
    web_browser.find_element_by_xpath('//h1[contains(text(), "Написать рецензию")]').is_displayed()


# тест удаления товара из Корзины
def test_delete_book_from_cart(web_browser):
    page = MainPage(web_browser)
    page.cookie_button.click()
    test_add_book_in_cart(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.HOME)
    page.cart.click()
    time.sleep(0.5)
    count = web_browser.find_element_by_xpath('//*[@id="ui-id-4"]/b').text
    assert int(count) == 1
    web_browser.find_element_by_xpath('//*[@class ="b-link-popup"]').click()
    web_browser.find_element_by_xpath('//span[@class="g-alttext-small g-alttext-grey g-alttext-head"]').is_displayed()


# тест удаления товара из Отложенного
def test_delete_book_from_putorder(web_browser):
    page = MainPage(web_browser)
    page.cookie_button.click()
    test_add_book_in_putorder(web_browser)
    page.putorder.click()
    count = web_browser.find_element_by_xpath('//span[@class ="cabinet-menu__counter"]').text
    assert int(count) == 1
    web_browser.find_element_by_xpath('//span[@class="checkbox-ui-e-bg b-checkbox-e-bg-m-white '
                                      'b-checkbox-m-radius"]').click()

    web_browser.find_element_by_xpath('//a[@class="btn btn-small btn-invert btn-pad-10 js-ap-btn-remove"]').click()
    web_browser.switch_to.alert.accept()
    web_browser.refresh()
    web_browser.find_element_by_xpath('//span[@style="color: #1a1a1a;font: 16px/22px PTSans,Tahoma,'
                                      'sans-serif;opacity: 0.66;"]').is_displayed()


def test_add_another_one_book(web_browser):
    page = MainPage(web_browser)
    test_add_book_in_cart(web_browser)
    page.cart.click()
    page.add_another_book.click()
    time.sleep(3)
    count = web_browser.find_element_by_xpath('//span[@class="b-header-b-personal-e-icon-count-m-cart '
                                              'basket-in-cart-a"]').text
    assert int(count) == 2


# тестируем футер
# тест перехода в AppStore
def test_app_store_click(web_browser):
    page = MainPage(web_browser)
    # скролл страницы до футера, обсуловлен нажатием по ссылке, которую в данный момент перекрывает другой видимый
    # объект. в результате выполнения клика по локатору xpath, происходит переход на совершенно другую страницу.
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.app_store.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    # здесь сравнение url работает некорректно, подошел иным способом
    web_browser.find_element_by_xpath('//span[@class="we-localnav__title__qualifier"]').is_displayed()


# тест перехода в GooglePlay
def test_google_play_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.google_play.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == "https://play.google.com/store/apps/details?id=ru.labirint.android"


# тест перехода в AppGallery
def test_app_gallery_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.app_gallery.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == "https://appgallery.huawei.com/app/C101184737?appId=C101184737&source=appshare" \
                                     "&subsource=C101184737"


# тест перехода в Вконтакте
def test_vk_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.vk.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://vk.com/labirintru'


# тест перехода в Вконтакте.Дети
def test_vk_kids_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.vk_kids.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://vk.com/labirintdeti'


# тест перехода в Ютьюб
def test_youtube_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.youtube.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'


# тест перехода в Одноклассники
def test_ok_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.ok.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://ok.ru/labirintru'


# тест перехода в Дзен
def test_dzen_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.dzen.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'


# тест перехода в Телеграм
def test_telegram_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.telegram.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://t.me/labirintru'


# тест перехода в Все книги
def test_all_books_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.all_books.click()
    assert page.get_current_url() == 'https://www.labirint.ru/books/'


# тест перехода в Школа
def test_school_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.school.click()
    assert page.get_current_url() == 'https://www.labirint.ru/school/'


# тест перехода в Журналы
def test_magazines_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.magazines.click()
    assert page.get_current_url() == 'https://www.labirint.ru/journals/'


# тест перехода в Игрушки
def test_games_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.games.click()
    assert page.get_current_url() == 'https://www.labirint.ru/games/'


# тест перехода в Канцтовары
def test_office_supplies_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.office_supplies.click()
    assert page.get_current_url() == 'https://www.labirint.ru/office/'


# тест перехода в CD/DVD
def test_cd_dvd_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.disks.click()
    assert page.get_current_url() == 'https://www.labirint.ru/multimedia/'


# тест перехода в Сувениры
def test_souvenirs_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.souvenirs.click()
    assert page.get_current_url() == 'https://www.labirint.ru/souvenir/'


# тест перехода в Товары для дома
def test_household_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.household.click()
    assert page.get_current_url() == 'https://www.labirint.ru/household/'


# тест перехода в Партнерам
def test_partner_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.partners.click()
    assert page.get_current_url() == 'https://partner.labirint.ru/login'


# тест перехода в Наши вакансии
def test_job_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.job.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://www.labirint.org/vakansii?tab=5'


# тест перехода в Как сделать заказ
def test_order_help_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.order_help.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/order/'


# тест перехода в Оплата
def test_payment_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.payment.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/?clause=132'


# тест перехода в Курьерская доставка
def test_delivery_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.delivery.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/?clause=9'


# тест перехода в Поддержка
def test_support_f_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.support_f.click()
    assert page.get_current_url() == 'https://www.labirint.ru/support/'


# тест перехода в Вся помощь
def test_help_f_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.help_f.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/'


# тест перехода в Пользовательское соглашение
def test_agreement_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.agreement.click()
    assert page.get_current_url() == 'https://www.labirint.ru/agreement/'


# тест перехода в Вы смотрели
def test_visited_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.visited.click()
    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/?vybor=visited'


# тест перехода в Кабинет
def test_cabinet_click(web_browser):
    page = MainPage(web_browser)
    web_browser.find_element_by_tag_name('html').send_keys(Keys.END)
    page.cabinet.click()
    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/'
