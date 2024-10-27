money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05 # Ежемесячный рост цен
budget=salary+money_capital-spend #after first month
k=0 #так как цикл добавит лишние
while budget>0:
    budget+=salary
    spend*=(1+increase)
    budget-=spend
    k+=1
print("Количество месяцев, которое можно протянуть без долгов:", k)
