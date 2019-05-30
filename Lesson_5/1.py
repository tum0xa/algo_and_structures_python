"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple


def average_profit(list_profits):
    """

    :param list_profits: The list of profit values
    :return: Average value of the profit
    """
    profit_total = 0
    for profit in list_profits:
        profit_total += profit
    return profit_total / len(list_profits)


num_of_companies = input("Enter the number of companies: ")

if num_of_companies.isdecimal():
    num_of_companies = int(num_of_companies)
else:
    print("Invalid input! Restart the program.")
    quit(0)

companies = []
Company = namedtuple('Company', 'name profit_year average_profit')
for i in range(0, num_of_companies):
    profit_year = []
    name_of_company = input(f"Type the name of {i + 1} company: ")
    for quarter in range(1, 5):
        profit_quarter = input(f"Type the profit of the company for the {quarter} quarter: ")
        if profit_quarter.isnumeric():
            profit_year.append(float(profit_quarter))
        else:
            profit_year.append(0.0)
            print(f"Invalid input! Presume the profit for the {quarter} quarter is 0.")
    company = Company(
        name=name_of_company,
        profit_year=profit_year,
        average_profit=average_profit(profit_year)
    )
    companies.append(company)
# print(companies)

statistic_profit_total = 0
for company in companies:
    statistic_profit_total += company.average_profit
statistic_average_profit = statistic_profit_total / num_of_companies

# print(statistic_average_profit)

print(f"The list of the companies that the year profit GREATER than a statistic average profit "
      f"({statistic_average_profit}):")
for company in companies:
    if company.average_profit > statistic_average_profit:
        print(company.name)

print(f"The list of the companies that the year profit LESS than a statistic average profit "
      f"({statistic_average_profit}):")
for company in companies:
    if company.average_profit < statistic_average_profit:
        print(company.name)
