import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
from selenium.webdriver.common.by import By


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        super().__init__(web_driver, url)

    # кнопка авторизации
    login = WebElement(xpath='//*[@id="minwidth"]/div[4]/div/div[1]/div[2]/div/ul/li[4]/a/span[1]/span[1]/span')
    # электронная почта
    email = WebElement(xpath='//*[@name="code"]')
    # пароль (код скидки)
    passw = WebElement(xpath='//*[@class="full-input__input formvalidate-error"]')

    # кнопка на логотипе-названии
    logo = WebElement(xpath='//*[@class="b-header-b-logo-e-logo-wrap"]')
    # кнопка сообщения
    messages = WebElement(xpath='//*[@class="b-header-b-personal-e-link top-link-main have-dropdown-touchlink '
                                'top-link-main_notification"]')
    # кнопка Мой Лаб
    mylab = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/div/ul/li[4]/a')
    # кнопка Отложено
    putorder = WebElement(xpath='//*[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    # кнопка Корзина
    cart = WebElement(xpath='//*[@data-event-type="16"]')
    # кнопка Доставка и оплата
    help = WebElement(xpath='//*[@class="b-header-b-sec-menu-e-link" and contains (text(),"Доставка и оплата")]')
    # кнопка Сертификаты
    certificates = WebElement(xpath='//*[@class="b-header-b-sec-menu-e-link" and contains (text(),"Сертификаты")]')
    # кнопка Рейтинги
    rating = WebElement(xpath='//a[@href="/rating/?id_genre=-1&nrd=1"]')
    # кнопка Новинки
    novelty = WebElement(xpath='//*[@class="b-header-b-sec-menu-e-link" and contains (text(),"Новинки")]')
    # кнопка Скидки
    sale = WebElement(xpath='//a[@href="/sale/"]')
    # кнопка Контакты
    contact = WebElement(xpath='//*[@data-event-content="Контакты"]')
    # кнопка Поддержка
    support = WebElement(xpath='//*[@class="b-header-b-sec-menu-e-link" and contains (text(),"Поддержка")]')
    # кнопка Пункты самовывоза
    maps = WebElement(xpath='//*[@class="b-header-b-sec-menu-e-link" and @href="/maps/"]')

    # поле поиска
    search = WebElement(id='search-field')
    # кнопка  поиска
    search_run_button = WebElement(xpath='//button[@class="b-header-b-search-e-btn" and @type="submit"]')
    # результаты поиска
    products_titles = ManyWebElements(xpath='//a[@class="product-title-link"]')
    # заголовок страницы
    page_title = WebElement(xpath='//h1')

    # кнопка В корзину
    add_book = WebElement(xpath='//a[@data-position="1"]')
    # кнопка Добавить книгу
    add_another_book = WebElement(xpath='//span[@class="btn btn-increase btn-increase-cart"]')
    # кол-во книг в корзине
    added_books = WebElement(xpath='//span[@class="b-header-b-personal-e-icon-count-m-cart '
                                              'basket-in-cart-a"]')
    # кнопка Отложить
    add_putorder = WebElement(xpath='//a[@data-hasqtip="2"]')
    # кнопка Другие действия
    else_button = WebElement(xpath='//a[@data-hasqtip="1"]')
    # кнопка Написать рецензию
    review_button = WebElement(xpath='//a[@class="b-list-item-hover js-card-block-actions-review"]')
    # кнопка Оформить в Корзине
    buy = WebElement(xpath='//a[@data-event-type="24"]')
    # кнопка Принять куки
    cookie_button = WebElement(xpath='//button[@class="cookie-policy__button js-cookie-policy-agree"]')
    # кнопка Оформить заказ в Корзине
    checkout_button = WebElement(xpath='//button[@class ="btn btn-primary btn-large fright start-checkout-js"]')



    # кнопка AppStore
    app_store = WebElement(xpath='//a[@data-event-content="App Store"]')
    # кнопка GooglePlay
    google_play = WebElement(xpath='//a[@data-event-content="Google Play"]')
    # кнопка AppGallery
    app_gallery = WebElement(xpath='//a[@data-event-content="App Gallery"]')
    # кнопка Вконтакте
    vk = WebElement(xpath='//a[@data-event-content="ВКонтакте"]')
    # кнопка Вконтакте. Дети
    vk_kids = WebElement(xpath='//a[@data-event-content="ВКонтакте. Дети"]')
    # кнопка Ютьуб
    youtube = WebElement(xpath='//a[@data-event-content="Ютьюб"]')
    # кнопка Одноклассники
    ok = WebElement(xpath='//a[@data-event-content="Одноклассники"]')
    # кнопка Яндекс.Дзен
    dzen = WebElement(xpath='//a[@data-event-content="Дзен"]')
    # кнопка Телеграм
    telegram = WebElement(xpath='//a[@data-event-content="Телеграм"]')
    # кнопка Все книги
    all_books = WebElement(xpath='//a[@data-event-content="Все книги"]')
    # кнопка Школа
    school = WebElement(xpath='//a[@data-event-content="Школа"]')
    # кнопка Журналы
    magazines = WebElement(xpath='//a[@data-event-content="Журналы"]')
    # кнопка Игрушки
    games = WebElement(xpath='//a[@data-event-content="Игрушки"]')
    # кнопка Канцтовары
    office_supplies = WebElement(xpath='//a[@data-event-content="Канцтовары"]')
    # кнопка CD/DVD
    disks = WebElement(xpath='//a[@data-event-content="CD/DVD"]')
    # кнопка Сувениры
    souvenirs = WebElement(xpath='//a[@data-event-content="Сувениры"]')
    # кнопка Товары для дома
    household = WebElement(xpath='//a[@class="b-rfooter-e-item-link" and contains(text(),"Товары для дома")]')
    # кнопка Партнерам
    partners = WebElement(xpath='//a[@data-event-content="Партнерам"]')
    # кнопка Наши вакансии
    job = WebElement(xpath='//a[@data-event-content="Наши вакансии"]')
    # кнопка Как сделать заказ
    order_help = WebElement(xpath='//a[@data-event-content="Как сделать заказ"]')
    # кнопка Оплата
    payment = WebElement(xpath='//a[@data-event-content="Оплата"]')
    # кнопка Курьерская доставка
    delivery = WebElement(xpath='//a[@data-event-content="Курьерская доставка"]')
    # кнопка Поддержка
    support_f = WebElement(xpath='//a[@data-event-content="Поддержка"]')
    # кнопка Напишите нам
    mailto = WebElement(xpath='//a[@data-event-content="Напишите нам"]')
    # кнопка Вся помощь
    help_f = WebElement(xpath='//a[@data-event-content="Вся помощь"]')
    # кнопка Пользовательское соглашение
    agreement = WebElement(xpath='//a[@data-event-content="Пользовательское соглашение"]')
    # кнопка Вы смотрели
    visited = WebElement(xpath='//a[@data-event-content="Вы смотрели"]')
    # кнопка Кабинет
    cabinet = WebElement(xpath='//a[@data-event-content="Кабинет"]')



    '''header'''

    """# окно авторизации
    login = WebElement(xpath='//*[@class="b-header-b-personal-e-list-item_cabinet"]')
    # кнопка на логотипе-названии
    logo = WebElement(xpath='//*[@class="b-header-b-logo-e-logo-wrap"]')
    # кнопка сообщения
    messages = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div/ul/li[3]/a/span[1]/span')
    # кнопка Мой Лаб
    my_lab = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[2]/div/ul/li[4]/a/span[2]')
    # кнопка Отложено
    postponed = WebElement(xpath='//*[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    # кнопка Корзина
    cart = WebElement(xpath='//*[@class="b-header-b-personal-e-list-item have-dropdown  last-child"]')
    # кнопка 18+
    agreement = WebElement(
        xpath='//*[@class="b-header-e-icon-adult b-header-e-icon-adult-m-big b-header-e-sprite-background"]')
    # кнопка Что читать? Рекомендуем
    now = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[1]/div/a[2]/span[2]/span/span')
    # кнопка Книги
    books = WebElement(xpath='//*[@id="minwidth"]/div[4]/div/div[1]/div[4]/div/div[1]/ul/li[1]/span/a')
    # кнопка Главное 2022
    best = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[2]/span/a')
    # кнопка Школа
    school = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[3]/span/a')
    # кнопка Игрушки
    games = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[4]/span/a')
    # кнопка Канцтовары
    stationery = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[5]/span/a')
    # кнопка Клуб
    club = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[11]/span/a')
   

    '''body'''

    # кнопка "Что почитать: выбор редакции"
    what_to_read_button = WebElement(xpath='//*[@id="right-inner"]/div[1]/div[1]/a')
    # названия книг на странице "Что почитать: выбор редакции"
    products_titles_large = ManyWebElements(xpath='//span[@class="product-title large-name"]')
    # заголовок страницы
    page_title = WebElement(xpath='//h1')
    # кнопка "Лучшая покупка дня"
    best_buy_button = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div/div[1]/div[2]/div/h2/a')
    # карточка книг на странице
    products_carts = ManyWebElements(xpath='//div[@class="product need-watch watched"]')
    # кнопка "Больше книг со скидками"
    discounts_button = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div/div[1]/div[2]/a')
    # описание скидки на книгу в результатах поиска
    discounts_books = ManyWebElements(xpath='//a[contains(@class, "card-label_profit")]')
    # кнопка "Читатели выбирают сегодня"
    today_button = WebElement(xpath='//*[@id="bottom"]/div[1]/div[1]/a')
    # карточки книг в результатах поиска Читатели выбирают сегодня
    products_books_now = ManyWebElements(
        xpath='//div[contains(@class, "jcarousel-item book-item need-watch swiper-slide-active watched")]')
    # карточки книг в результатах поиска Лидеры продаж
    products_books_leaders = ManyWebElements(xpath='//div[contains(@class, "product need-watch watched")]')
    # карточки книг в результатах поиска Новинки 2022
    products_books_new = ManyWebElements(
        xpath='//div[contains(@class, "product need-watch watched")]')
    # карточки обзоров в результатах поиска
    products_reviews = ManyWebElements(xpath='//div[contains(@class, "news-item need-watch watched")]')
    # кнопка "Лабиринт. Сейчас"
    now_button = WebElement(xpath='//*[@id="bottom"]/div[2]/div[1]/noindex/a')
    # активный пункт горизонтального меню, который соответсвует содержанию открывшейся страницы
    active_menu_item = WebElement(xpath='//a[@class="mm-link mm-link-big mm-link-big-m-sub active"]')
    # кнопка "Детский навигатор — что читать детям и с детьми"
    kids_button = WebElement(xpath='//*[@id="bottom"]/div[3]/div[1]/noindex/a')
    # кнопка "Книжные лидеры продаж"
    leaders_button = WebElement(xpath='//*[@id="bottom"]/div[7]/div[1]/a')
    # кнопка "Книги: новинки 2022"
    novelties_books_button = WebElement(xpath='//*[@id="bottom"]/div[9]/div[1]/a')
    # кнопка "Книжные обзоры и рецензии"
    reviews_button = WebElement(xpath='//*[@id="bottom"]/div[12]/a')
    # заголовок на открывшейся странице "Книжные обзоры и рецензии"
    heading_reviews = WebElement(xpath='//div[@class="ratingh h1"]')
    # кнопка "Правила" в разделе "Вам подарок!"
    regulations_button = WebElement(xpath='//*[@id="left"]/div[1]/form/div[1]/p/a')

    '''footer'''

   
     # кнопка Акции
    sales = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Акции")]')
    # кнопка Главные книги
    main_books = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Главные книги")]')
    # кнопка Бонус за рецензию
    bonus = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Бонус за рецензию")]')
    # кнопка Сертификаты
    certificates = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Сертификаты")]')
    # кнопка Только у нас
    exclusive = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Только у нас")]')
    # кнопка Предзаказы
    pre_order = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Предзаказы")]')
    # кнопка Лабиринт.Сейчас
    lab_now = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Лабиринт. Сейчас")]')
    # кнопка Детский навигатор
    child_now = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Детский навигатор")]')
    # кнопка Рецензии читателей
    reviews = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Рецензии читателей")]')
    # кнопка Книжные обзоры
    book_reviews = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Книжные обзоры")]')
    # кнопка Подборки читателей
    recommendations = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Подборки читателей")]')
    # кнопка Тесты
    lit_tests = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Тесты")]')
    # кнопка Новости Л.
    news = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Новости Л.")]')
    # кнопка Конкурсы
    contests = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Конкурсы")]')
    # кнопка Спепцпроекты
    club = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Спецпроекты")]')

    # кнопка Войти по коду скидки или через соцсеть
    login_1 = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" '
              'and contains(text(),"Войти по коду скидки или через соцсеть")]')
    # кнопка Вход и регистрация
    login_2 = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Вход и регистрация")]')
    # кнопка Вы смотрели
    visited = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Вы смотрели")]')
    # кнопка Кабинет
    cabinet = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Кабинет")]')
    # окно авторизации
    login = WebElement(
        xpath='//a[@id="g-recap-0-btn"]')

    # кнопка СтопКовид
    stop_covid = WebElement(
        xpath='//a[@class="sprite_kovid kov_desc"]')
    # кнопка Акит
    akit = WebElement(
        xpath='//a[@class="logo_akit_grey kov_desc"]')
    # кнопка Холдинг «Лабиринт»
    lab_hold = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link b-rfooter-e-item-link-m-small analytics-click-js" '
              'and contains(text(),"© Холдинг «Лабиринт»")]')
    # кнопка 8 800 600-95-25
    contacts = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link b-rfooter-e-item-link-m-small analytics-click-js" '
              'and contains(text(),"8 800 600-95-25")]')
"""
