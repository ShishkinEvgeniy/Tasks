import numpy as np


def game_core_v3(number):
    '''Поиск позиции числа в сортированном списке'''
    num_list = [i for i in range (1, 101)] # Создание списка на 100 элементов
    less = num_list[0] 
    more = num_list[99] 
    i = 0 
    while less<=more: # Итерация до совпадения меньшего и большего
        i += 1 
        midst = (less + more)//2 
        if midst > number:
            more = midst - 1 # Больший элемент списка становится средним
        elif midst<number:
            less = midst + 1  # Меньший элемент списка становится средним
        else:
            break 
    return(i)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
score_game(game_core_v3)