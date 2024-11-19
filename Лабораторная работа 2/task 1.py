money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 1
while (spend <= money_capital):
    month += 1
    money_capital = (money_capital + salary) - spend
    spend += (spend * increase)

print("Количество месяцев, которое можно протянуть без долгов:", month)
