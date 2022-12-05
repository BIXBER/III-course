title = " РАЗМЕН ДЕНЕЖНОЙ СУММЫ В РОССИЙСКОМ НОМИНАЛЕ КУПЮР "
title = (title.upper()).center(len(title)+20, "*")
print(title)


def declination_count_times(times, declination=''):
    if 2 <= times <= 4:
        declination = 'раза'
    else:
        declination = 'раз'
        
    return declination

def declination_monetary_unit(denomination, declination=''):
    if denomination == 1:
        declination = 'рублю'
    elif 2 <= denomination <= 4:
        declination = 'рубля'
    else:
        declination = 'рублей'
        
    return declination

sum = 0
while type(sum) == int:
    
    try:
        sum = int(input("\nВведите сумму денег: "))

        while sum == 0 or sum < 0:
            if sum == 0:
                print("\nВаша сумма равна 0 и её нельзя ни на что разменять...\nВведите повторно другое значение.\n")
                sum = int(input("Введите сумму денег: "))
            elif sum < 0:
                print("\nВы ввели отрицательное значение суммы и её нельзя разменять...\nВведите повторно положительное значение.\n")
                sum = int(input("Введите сумму денег: "))
                
        if sum >= 10:       
            print("\nВашу сумму денег можно разменять на купюры:")
            
            for i in 5000, 2000, 1000, 500, 200, 100, 50, 10:
                count_divisions = sum // i
                sum_remaininig_after_divide = sum % i
                sum = sum % i
                
                if count_divisions == 0:
                    continue
                else:
                    decl_times = declination_count_times(count_divisions)
                    print(f'По {i} рублей - {count_divisions} {decl_times}')
                    
            if sum == 0:
                print("\n--- Без остатка ---")
            else:
                print(f"\nОстаток: {sum}")
                print("\nОстаток можно разменять на монеты:")
                for i in 5, 2, 1:
                    count_divisions = sum // i
                    sum_remaininig_after_divide = sum % i
                    sum = sum % i
                    
                    if count_divisions == 0:
                        continue
                    else:
                        decl_times = declination_count_times(count_divisions)
                        decl_rubles = declination_monetary_unit(i)
                        print(f'По {i} {decl_rubles} - {count_divisions} {decl_times}')
        else:
            print("\nВашу сумму денег разменять на монеты:")
            for i in 5, 2, 1:
                count_divisions = sum // i
                sum_remaininig_after_divide = sum % i
                sum = sum % i
                
                if count_divisions == 0:
                    continue
                else:
                    decl_times = declination_count_times(count_divisions)
                    decl_rubles = declination_monetary_unit(i)
                    print(f'По {i} {decl_rubles} - {count_divisions} {decl_times}')       
        print()
                    
        break   # You can comment this line for programm is do not stopping
        
    except:
        print("\nВы ввели не числовое значение...\nВведите повторно корректное значение.")
        