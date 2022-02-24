import numpy as np

def game_core_v3(number):
    '''Решаем методом дихотомии. Ищем середину нашего диапазона и определяем в какую половину попало искомое число. 
       Вторую половину отбрасываем и дальнейший поиск ведем аналогичным образом во второй половине'''
    '''Для того чтобы при загаданном числе равном в 100 цикл не зацикливался присваиваем значение 100,
       как решить эту проблемму по другому не знаю '''
    predict = 100 
    count = 1
    a_start = 0
    b_end = 100
    while number != predict:
        count += 1
        predict = a_start + (b_end - a_start)//2
        if number > predict: 
            a_start = predict
        elif number < predict: 
            b_end = predict
    return(count) # выход из цикла, если угадали
        
        
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