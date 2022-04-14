per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите желаемую сумму вклада:"))
TKB = int((money / 100) * per_cent["ТКБ"])
SKB = int((money / 100) * per_cent["СКБ"])
VTB = int((money / 100) * per_cent["ВТБ"])
SBER = int((money / 100) * per_cent["СБЕР"])
profit = [TKB, SKB, VTB, SBER]
per_cent_max = max(per_cent.values())
profit_max = max(profit)
deposit = money + profit_max
print("Вы вносите", money, "руб.", "\nДоход составит:", profit, "руб.", "\nЧерез месяц вы получите", deposit, "руб., если выберете ставку", per_cent_max)