#Раздел иморта модулей
import random
#раздел созданных функций

def displayBoard(board):

    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    

def inputPlayerLeter():
    letter = ''
    while not(letter =='X' or letter=='O'):
        print('Введите X или O')

        letter =input ().upper()

    if letter =='X':
        return ['X','O']
    else:    
        return ['O','X']

def whoGoesFirst():
    a = random.randint(1,2)
    if a == 1 :
        return 'Человек'
    else:
        return 'Комьютер'    








#Основное тело программы 
print(whoGoesFirst())