tickets = int(input("Введите количество билетов:"))
price_1 = 1390
price_2 = 990
s = 0.9
for i in range(1, tickets + 1):
    age = int(input("Введите возраст:"))
    if age < 18:
        print("Проход бесплатный")
    if 18 <= age < 25:
        if tickets >= 3:
            print("Итого со скидкой =", (tickets * price_2) * s, "руб.")
        else:
            print("Итого =", tickets * price_2, "руб.")
    if age >= 25:
        if tickets >= 3:
            print("Итого со скидкой =", (price_1 * tickets) * s, "руб.")
        else:
            print("Итого =", price_1 * tickets, "руб.")