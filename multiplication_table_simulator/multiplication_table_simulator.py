from random import choice as chc


title = " тренажер_таблицы_умножения.py "
title = (title.upper()).center(len(title)+26, "*")
print(title)

# создание_списков_значений_и_сложности_уровней: 
def difficult_level_of_value(level):
    values_list = []
    for i in range(level):
        values_list.append(i)
    return values_list

def difficult_level_of_multiplier(level):
    multiplier_list = []
    for i in range(level):
        multiplier_list.append(i)
    return multiplier_list

# выборка_значений:
def random_value(values):
    value = chc(values)
    return value

def random_multiplier(multipliers):
    multiplier = chc(multipliers)
    return multiplier



# цикл_обучения:
queries = ["да", "Да", "ДА", "нет", "Нет", "НЕТ", "yes", "Yes", "YES", "no", "No", "NO", "not", "Not", "NOT"]
queries_negative = ["нет", "Нет", "НЕТ", "no", "No", "NO", "not", "Not", "NOT"]
queries_positive = ["да", "Да", "ДА", "yes", "Yes", "YES"]
response = "\nТакого запроса не существует... Введите верный запрос!"

low_level = 10
medium_level = 50
hard_level = 100

query = ""
while query not in queries:
    query = input("""\nГотовы ли Вы начать обучаться? - (Да(Yes) / Нет(No, Not))
Ответ: """)

    if query in queries_negative:
        print(f"\nВы не решили ни одного уровня. Возвращайтесь снова!")
        break

    elif query in queries_positive:
        level = 0
        while level != range(1, 4):
            try:
                level = int(input("""\nВыберите доступный уровень сложности - (от 1 до 3 включительно)
Ответ: """))
                if level == 1:
                    level = low_level
                    break
                elif level == 2:
                    level = medium_level
                    break
                elif level == 3:
                    level = hard_level
                    break
                else:
                    print(f"\n{level} уровня не существует... Введите доступный уровень в числовом формате!")
            except:
                print(f"\nУровень введён некорректно! - Введите доступный уровень в числовом формате!")
                
        counter = 0     
        while query not in queries_negative:  
            value = random_value(difficult_level_of_value(level))
            multiplier = random_multiplier(difficult_level_of_multiplier(level))
            answer = value * multiplier

            try:
                question = int(input(f"""\nСколько будет {value}*{multiplier}?
Ответ: """))
                if question == answer:
                    counter += 1
                    print("\nПравильно!")

                    query = ""
                    while query not in queries:
                        query = input("""\nХотите ли вы продолжить? - (Да(Yes) / Нет(No, Not))                                              
Ответ: """)
                        if query in queries_negative:    
                            break

                        elif query in queries_positive:
                            continue

                        else:
                            print(response)

                elif question != answer:
                    print(f"\nНеправильно! - Верный ответ: {answer}")

                    query = ""
                    while query not in queries:
                        query = input("""\nХотите ли вы продолжить? - (Да(Yes) / Нет(No, Not))                                              
Ответ: """)     
                        if query in queries_negative:    
                            break
                        
                        elif query in queries_positive:
                            continue
                        
                        else:
                            print(response)           
            except:
                print(f"""\nВы ввели некорректный ответ! - Ответ должен быть в числовом формате. Введите верный ответ в следующем примере:""")


            # вывод_результата:
            counter_declination = counter % 10

            low = counter_declination == 0 and level == low_level 
            medium = counter_declination == 0 and level == medium_level
            hard = counter_declination == 0 and level == hard_level

            declination_zero = counter_declination == 0
            declination_one = counter_declination == 1
            declination_two = 2 <= counter_declination <= 4
            declination_three = (counter_declination >= 5 and counter_declination <= 9)

            if declination_zero:
               lvl_decl = "уровней." 
            elif declination_one:
                lvl_decl = "уровень."
            elif declination_two:
                lvl_decl = "уровня!"
            elif declination_three:
                lvl_decl = "уровней!!!"

            result = f"\nВы прошли {counter} {lvl_decl}"
            goodbye = "\nСпасибо за тренировку! Возвращайтесь снова!"

            if (query in queries_negative) and (declination_one or declination_two or declination_three):
                print(result, goodbye)
            elif (query in queries_negative) and low:
                print(result, "\nПостарайтесь не ошибаться и возвращайтесь снова!")
            elif (query in queries_negative) and medium:
                print(result, "\nПотренируйся достаточно на 1-ом уровне и возвращайтесь снова на 2-ой!")
            elif (query in queries_negative) and hard:
                print(result, "\nПотренируйтесь на более лёгких уровнях и возвращайтесь снова на 3-ий уровень!")

    else:
        print(response)
        
input("\nНажмите клавишу 'Enter', чтобы выйти: ")


    
        
    
