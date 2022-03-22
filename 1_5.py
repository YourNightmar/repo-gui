#создаю запрос выручки и убытков от пользователя
revenue = int(input('Enter your revenue: '))
costs = int(input('Enter your costs: '))
#производим расчеты
if revenue > costs:
    result = revenue - costs
    print('You have profit: ' + str(result))
#расчет рентабельности выручки
    result_1 = (revenue / costs) * 100
    print('Your profitability of revenue:' + str(result_1) + '%')
#расчет прибыли на одного сотрудника
    workers = int(input('Enter the number of employees: '))
    result_2 = result / workers
    print("The company's profit per employee: " + str(result_2))
elif revenue < costs:
    result = revenue - costs
    print('You have loss:' + str(result))
else:
    revenue == costs
    print('You are at the break-even point')