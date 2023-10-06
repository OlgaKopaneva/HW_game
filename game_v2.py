"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Угадываем число бинарным поиском 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    #options = [i for i in range(1, 101)]  # список возможных вариантов, не сортируем, т.к. он создастся отсортированным
    mid = 50 # середина списка возможных вариантов (общее мн-во вариантов от 1 до 100)
    low = 1
    high = 100 # границы списка возможных вариантов - это константы 1 и 100
    
    while mid != number:  # пока не угадаем число (пока искомое число не окажется в центре сужающегося списка) -> 
        if number > mid:  #сравниваем искомое с центром списка, если больше, то сдвигаем нижнюю границу на +1 к центру
            low = mid + 1
        else:               # если меньше - сдвигаем верхнюю границу на -1 от центра
            high = mid - 1 
        mid = (low+high)//2   # перерасчитываем центр 
        count += 1

    return count


def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
