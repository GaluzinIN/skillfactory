# определяет для крестика или нолика победу, возращает True в случае выигрошной комбинации
def Check_win (Symb, Pole_check):
    
    Win = None
    Str = Pole_check[1][1] + Pole_check[1][2] + Pole_check[1][3]
    if Symb*3 == Str:
        Win = True
        Str = ''
    Str = Pole_check[2][1] + Pole_check[2][2] + Pole_check[2][3]
    if Symb*3 == Str:
        Win = True
        Str = ''
    Str = Pole_check[3][1] + Pole_check[3][2] + Pole_check[3][3]
    if Symb*3 == Str:
        Win = True
        Str = ''
    Str = Pole_check[1][1] + Pole_check[2][1] + Pole_check[3][1]
    if Symb*3 == Str:
        Win = True
        Str = ''
    Str = Pole_check[1][2] + Pole_check[2][2] + Pole_check[3][2]
    if Symb*3 == Str:
        Win = True
        Str = ''
    Str = Pole_check[1][3] + Pole_check[2][3] + Pole_check[3][3]
    if Symb*3 == Str:
        Win = True
        Str = ''
    Str = Pole_check[1][1] + Pole_check[2][2] + Pole_check[3][3]
    if Symb*3 == Str:
        Win = True
        Str = ''
    Str = Pole_check[3][1] + Pole_check[2][2] + Pole_check[1][3]
    if Symb*3 == Str:
        Win = True
        Str = ''
            
    return Win

Pole = [[' ','0', '1','2'], ['0','-', '-', '-'],['1', '-', '-', '-'],['2', '-', '-', '-']]
for i in range(9):
    i +=1
    if i % 2 != 0:
        print('Ход крестиков')
        x = int(input('введите номер строки:'))
        y = int(input('введите номер позиции:'))
        # Проверка на правильный диапазон ячейки
        while x > 2 or y > 2:
            print('Указанная ячейка вне поля,введите значения от 0 до 2')
            x = int(input('введите номер строки:'))
            y = int(input('введите номер позиции:'))
        # Проверка на занятость ячейки
        while (Pole[x+1][y+1] == 'X') or (Pole[x+1][y+1] == 'O'):
            print('Указанная ячейка, введите другие значения ')
            x = int(input('введите номер строки:'))
            y = int(input('введите номер позиции:'))
        Pole[x+1][y+1] = 'X'
        print(" ".join(Pole[0]))
        print(" ".join(Pole[1]))
        print(" ".join(Pole[2]))
        print(" ".join(Pole[3]))
    else:    
        print('Ход ноликов')
        x = int(input('введите номер строки:'))
        y = int(input('введите номер позиции:'))
        # Проверка на правильный диапазон ячейки
        while x > 2 or y > 2:
            print('Указанная ячейка вне поля,введите значения от 0 до 2')
            x = int(input('введите номер строки:'))
            y = int(input('введите номер позиции:'))
        # Проверка на занятость ячейки
        while (Pole[x+1][y+1] == 'X') or (Pole[x+1][y+1] == 'O'):
            print('Указанная ячейка уже занята,введите другие значения')
            x = int(input('введите номер строки:'))
            y = int(input('введите номер позиции:'))
        Pole[x+1][y+1] = 'O'
        print(" ".join(Pole[0]))
        print(" ".join(Pole[1]))
        print(" ".join(Pole[2]))
        print(" ".join(Pole[3]))
    if Check_win ('X', Pole):
        print('Выиграли крестики')
        break
    if Check_win ('O', Pole):
        print('Выиграли нолики')
        break