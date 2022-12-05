# выбор_формата_ввода_даты:
input_date = int(input("""\n1 - стандартный формат - ДД.ММ.ГГГГ;
2 - стандартный формат (перевернутый) - ММ.ДД.ГГГГ);
3 - нестандартный формат - ГГГГ.ММ.ДД.

Введите значение: '1', '2' или '3' (в зависимости от Вашего выбора формата ввода даты): """))

# подготовка_формата_данных_(через_условия):
standart_dateformat = input_date == 1
standart_reverse_dateformat = input_date == 2
unstandart_dateformat = input_date == 3

if standart_dateformat:
    input_date = input("\nВведите дату в формате ДД.ММ.ГГГГ: ")
    str_date = input_date.split(".")
    date = []
    for i in str_date:
        date.append(int(i))
    day = date[0]
    month = date[1]
    year = date[2]
    
elif standart_reverse_dateformat:
    input_date = input("\nВведите дату в формате ММ.ДД.ГГГГ: ")
    str_date = input_date.split(".") 
    date = []
    for i in str_date:
        date.append(int(i))
    month = date[0]
    day = date[1]
    year = date[2]

elif unstandart_dateformat:
    input_date = input("\nВведите дату в формате ГГГГ.ММ.ДД: ")
    str_date = input_date.split(".")
    date = []
    for i in str_date:
        date.append(int(i))
    year = date[0]
    month = date[1]
    day = date[2]



# булевы_значения:
full_year = month == 12 and day == 31
leap_year = year % 4 == 0
month_30 = month % 2 == 1
month_31 = month % 2 == 0
full_month_30 = month != 2 and month_30 and day == 30 and not full_year
full_month_31 = month != 2 and month_31 and day == 31 and not full_year
full_month_in_leap_year = leap_year and month == 2 and day == 29
full_month_in_common_year = not leap_year and month == 2 and day == 28

# условия_следующего_дня:
if full_year:
    year += 1
    month = 1
    day = 1
elif (full_month_30 or full_month_31) or (full_month_in_leap_year or full_month_in_common_year):
    month += 1
    day = 1
else:
    day += 1

# преобразование_даты:
if day < 10:
    day = "0" + str(day)
elif day >= 10:
    day = str(day)
if month < 10:
    month = "0" + str(month)
elif month >= 10:
    month = str(month)

# словарь_месяцев:
MONTH = {
    "01": "Январь",
    "02": "Февраль",
    "03": "Март",
    "04": "Апрель",
    "05": "Май",
    "06": "Июнь",
    "07": "Июль",
    "08": "Август",
    "09": "Сентябрь",
    "10": "Октябрь",
    "11": "Ноябрь",
    "12": "Декабрь",
    "13": "None"
}

# склонение_месяцев_(через_словарь):
for i in MONTH.keys():
    MONTH[i] = MONTH[i].lower()
    if MONTH[i][-1] == "т":
        MONTH[i] = MONTH[i] + "а"
    else:
        MONTH[i] = MONTH[i].replace(MONTH[i][-1], "я")

# подготовка_вывода_результата:
if standart_dateformat:
    output_date = f"{day}.{month}.{year}"
elif standart_reverse_dateformat:
    output_date = f"{month}.{day}.{year}"
elif unstandart_dateformat:
    output_date = f"{year}.{month}.{day}"
if "0" in day:
    day = day[1]

output_date_informat = f"{day} {MONTH[month]} {year} года"



# вывод_результата:
print(f"\nСледующий день (дата): {output_date}")
print(f"Или же: {output_date_informat}")

input(f"\nНажмите 'Enter', чтобы выйти из программы:")