import random

NEGATIVE_QUERIES = ["нет", "Нет", "НЕТ", "no", "No", "NO", "not", "Not", "NOT"]
POSITIVE_QUERIES = ["да", "Да", "ДА", "yes", "Yes", "YES"]
CONGRATULATIONS = ["Very Good!!!"]

def printing_title():
    title = " блиц-викторина "
    title = (title.upper()).center(len(title)+60, "*")
    return title

def open_quest_file():
    with open("quests.txt", encoding="utf-8") as all_quests:
        quests = [line.rstrip('\n') for line in all_quests]
    return quests      

def open_answer_file():
    with open("answers.txt", encoding="utf-8") as all_answers:
        answers = [line.rstrip('\n') for line in all_answers]
    return answers
    
def input_name():
    username = input('Введите Ваше имя, чтобы начать играть: ')
    return username

quests = open_quest_file()
answers = open_answer_file()
AMOUNT_QUESTS = len(quests)
AMOUNT_ANSWERS = len(answers)            

def connected_pairs(quest, answer, counter_index=0, end=AMOUNT_QUESTS):
    connected_couples = {}
    while counter_index < end:
        connected_couples[quest[counter_index]] = answer[counter_index]
        counter_index += 1
        
    return connected_couples


def randomize_and_testing(library, counter_corrects=0, counter_answer=0, 
                          counter_omission=0, counter_wrong=0, 
                          stopping=False):
    keys = list(library)
    random.shuffle(keys)

    for quest in keys:
        counter_answer += 1
        answer_for_question, responce = (input(f'{counter_answer}) {quest} '), 
        input("Нажмите 'Enter', чтобы продолжить или введите " 
              "('Нет'/'No'/'Not') для приостановки тестирования: "))
        print()

        if answer_for_question == library[quest]:
            counter_corrects += 1
        elif answer_for_question == '':
            counter_omission += 1
            counter_wrong += 1
        elif answer_for_question != library[quest]:
            counter_wrong += 1

        if responce in NEGATIVE_QUERIES:
            stopping = True
            print("Тестирование завершено. Спасибо за участие!")
            break
        else:
            continue

    COMPLETE_QUESTS = counter_corrects + counter_wrong
    CORRECT_ANSWERS = counter_corrects
    UNCORRECT_ANSWERS = counter_wrong
    MISSED_ANSWERS = counter_omission 
    INCOMPLETE_ANSWERS = AMOUNT_QUESTS - counter_answer 
            
    return (COMPLETE_QUESTS, CORRECT_ANSWERS, UNCORRECT_ANSWERS, 
            MISSED_ANSWERS, INCOMPLETE_ANSWERS, stopping)
            
def decl_responce(missings):
    ending_number = missings % 10
    if ending_number == 1:
        declination = 'пропущенный'
    else:
        declination = 'пропущенных'
        
    return declination


def printing_and_recording(username, complete_quests, correct_answers, 
                           uncorrect_answers, missed_answers, incomplete_answers, 
                           decl, total_quests=AMOUNT_QUESTS):

    TERMS = {'terrible': missed_answers == AMOUNT_ANSWERS,
             'all_bad': uncorrect_answers and incomplete_answers
                        and missed_answers,
             'between-between': uncorrect_answers and incomplete_answers
                                and not missed_answers,
             'more or less': uncorrect_answers and not incomplete_answers 
                             and not missed_answers,
             'almost_good': not uncorrect_answers and not incomplete_answers
                            and missed_answers,
             'all_good': not uncorrect_answers and incomplete_answers,
             'everything is great': not uncorrect_answers and not 
                                    incomplete_answers,}


    if TERMS['terrible']:
        note_print = (f'\nВы не ответили ни на один вопрос: попробуйте начать '
                      'тестирование ещё раз.\n')

    elif TERMS["all_bad"]:
        note_print = (f'\nВсего пройдено: {complete_quests} из {total_quests} '
                       'вопросов.'
                      f'\nВерных ответов: {correct_answers}'
                      f'\nНеверных ответов: {uncorrect_answers}, из которых '
                      f'{missed_answers} {decl}.'
                      f'\nПовторите теорию и приходите на тестирование снова.\n')

    elif TERMS['more or less']:
        note_print = (f'\nВы ответили на все тестовые вопросы!'
                      f'\nВерных ответов: {correct_answers}'
                      f'\nНеверных ответов: {uncorrect_answers}'
                      f'\nПри этом, Вы не пропустили ни одного вопроса! '
                       'Это уже говорит про Вашу заинтересованность!\n')

    elif TERMS['between-between']:
        note_print = (f'\nВсего пройдено: {complete_quests} из {total_quests} ' 
                       'вопросов.'
                      f'\nВерных ответов: {correct_answers}'
                      f'\nНеверных ответов: {uncorrect_answers}'
                      f'\nПри этом, Вы сумели ответить на все заданные вопросы '
                       'без пропусков! Это уже говорит о Вашей смелости.\n')

    elif TERMS['almost_good']:
        note_print = (f'\nВы полностью ответили на заданную часть тестовых '
                       'вопросов!'
                      f'\nВерных ответов: {correct_answers}'
                      f'\nНеверных ответов: {correct_answers}, из которых ' 
                      f'{missed_answers} {decl}.\n')

    elif TERMS['all_good']:
        note_print = (f'\nВы полностью верно ответили на заданную часть тестовых вопросов!'
                      f'\nВсего пройдено: {complete_quests} из {total_quests} вопросов.'
                      f'\nПопробуйте в следующий раз пройти тестирование полностью.\n')

    elif TERMS['everything is great']:
        note_print = (f'\n{CONGRATULATIONS[0].upper().center(len(CONGRATULATIONS[0])+10, "*")}'
                      f'\nВы ответили верно на абсолютно все ({total_quests}) ' 
                       'тестовые вопросы!'    
                      f'\nУ вас уже есть все базовые знания языка Python! '
                       'Так держать!\n')

    note_record = (f'{username}:'
                    f'\n\tВсего пройдено: {complete_quests}/{total_quests}'
                    f'\n\tВерных ответов: {correct_answers}'
                    f'\n\tНеверных ответов: {uncorrect_answers}'
                    f'\n\tПропущено ответов: {missed_answers}\n\n')
    
    with open("users.txt", "a+", encoding="utf-8") as results:
        results.write(f'{note_record}')
        
    return print(note_print)


print()
print(printing_title())
print()
username = input_name()
print()
library = connected_pairs(quests, answers)
connected_pairs(quests, answers)
testing = randomize_and_testing(library)
declination = decl_responce(testing[3])
printing_and_recording(username, testing[0], testing[1], testing[2], testing[3], testing[4], declination)

input("Нажите клавишу 'Enter' для выхода из приложения тестирования:")