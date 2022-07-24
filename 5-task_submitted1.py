#Задача 1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# import re
# def join_punctuation(seq, characters='.,;?!'):
#     characters = set(characters)
#     seq = iter(seq)
#     current = next(seq)
#     for i in seq:
#         if i in characters:
#             current += i
#         else:
#             yield current #как удаляет точку из списка?
#             current = i
#     yield current

# text1 = "абв это первые три буквы абвалфавита. С этой строчки начинается название передачи абвгдейка. \
# Много лишних абвслов встречается в абвфразах."
# text3 = re.findall(r"[\w']+|[.,!?;]", text1)
# text3 = [x for x in text3 if not 'абв' in x]
# text3 = ' '.join(join_punctuation(text3))
# print(text3)    


#-------------------------------------------
#Задача 2
#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

# import random
# def current_gamer(whose_turn):
#     if (whose_turn): return 1
#     else: return 2
# def honesty_check(amount):
#     if (amount>28 or amount<1): return False
#     else: return True
# def check_gamers_qty(amount):
#     if amount>2 or amount<1: return False
#     else: return True    
# def bots_answer(x):
#     if (x==0): str1= bots_phrases[random.randint(0,len(bots_phrases)-1)]
#     elif (x<15): str1= bots_phrases1[random.randint(0,len(bots_phrases1)-1)]
#     else: str1= bots_phrases2[random.randint(0,len(bots_phrases2)-1)]
#     return str1

# candies_amount = 181
# candies_limit = 28
# candies_taken = 0
# gamer = 'игрок '
# id=1
# exit_mark=True
# bots_phrases = ['дорогу молодым уступаешь? ', 'ок. первый ход за мной, страдай! ', 'лузер, я первым хожу! ']
# bots_phrases1 = ['чё так мало взял? ', 'боишься что-ли брать больше? ', 'с козырей пошел? ']
# bots_phrases2 = ['все равно ошибёшься! ', 'Всё, считай, ты уже проиграл!' , 'русьський, здавайся, сдесь нэ пройти! ', 'ну-ну, попробуй. ']
# if (random.randint(0,1)): whose_turn=True
# else: whose_turn=False 

# gamers_qty_check = False
# while (not gamers_qty_check):
#     gamers_qty = int(input("введите количество игроков 1 или 2: "))
#     gamers_qty_check = check_gamers_qty(gamers_qty)
# if gamers_qty==2:    
#     while(exit_mark):
#         if ((candies_amount)<=candies_limit):
#             id = current_gamer(whose_turn)
#             print('на столе осталось {} конфет.'.format(candies_amount))
#             print('выиграл:', gamer, id)
#             exit_mark=False
#         else:
#             id = current_gamer(whose_turn)
#             print('Игрок {}, введите сколько конфет вы берете (сейчас на столе {} конфет): '.format(id, candies_amount), end=' ')
#             candies_taken=int(input())
#             while (not honesty_check(candies_taken)): 
#                 print('низя стока брать')
#                 print('Игрок {}, введите сколько конфет вы берете (сейчас на столе {} конфет): '.format(id, candies_amount), end=' ')
#                 candies_taken=int(input())
#             candies_amount-=candies_taken
#             if (whose_turn): whose_turn=False
#             else: whose_turn=True
# else:
#     print("вы играете с ботом")
#     first_turn = current_gamer(whose_turn)
#     while(exit_mark):
#         if (candies_amount<=candies_limit):
#             id = current_gamer(whose_turn)
#             print('на столе осталось {} конфет и я их все забираю'.format(candies_amount))
#             if(id==1): print('выиграл Игрок')
#             else: print('выиграл Бот')
#             exit_mark=False
#         else:
#             if (whose_turn):
#                 print('Игрок, введите сколько конфет вы берете (сейчас на столе {} конфет): '.format(candies_amount), end=' ')
#                 candies_taken=int(input())
#                 while (not honesty_check(candies_taken)): 
#                     print('низя стока брать')
#                     print('Игрок, введите сколько конфет вы берете (сейчас на столе {} конфет): '.format(candies_amount), end=' ')
#                     candies_taken=int(input())
#                 candies_amount-=candies_taken
#                 whose_turn=False
#             else:
#                 if (candies_amount<(candies_limit+1+candies_limit)): 
#                     print(bots_answer(candies_taken), end=' '); candies_taken=candies_amount-(candies_limit+1)
#                 elif ((candies_amount//candies_limit)%2==0) and ((candies_amount%candies_limit)>0) and (first_turn==2):
#                 # если целое от взятого - четное и при этом остаток >0 и я первый, то я выигрываю, можно брать максимум
#                     print(bots_answer(candies_taken), end=' '); candies_taken=28
#                 elif ((candies_amount//candies_limit)%2==1) and ((candies_amount%candies_limit)>0) and (first_turn==1):
#                 # если целое от взятого - НЕчетное и при этом остаток >0 и я второй, то я выигрываю, можно брать максимум
#                     print(bots_answer(candies_taken), end=' '); candies_taken=28
#                 elif ((candies_amount//candies_limit)%2==0) and ((candies_amount%candies_limit)==0) and (first_turn==2): 
#                 # если целое от взятого - четное и при этом остаток =0 и я первый, то делитель на 1 больше
#                     print(bots_answer(candies_taken), end=' '); candies_taken=(candies_amount//((candies_amount//candies_limit)+1))+1
#                 elif ((candies_amount//candies_limit)%2==1) and ((candies_amount%candies_limit)==0) and (first_turn==1): 
#                 # если целое от взятого - четное и при этом остаток =0 и я первый, то делитель на 1 больше
#                     print(bots_answer(candies_taken), end=' '); candies_taken=(candies_amount//((candies_amount//candies_limit)+1))+1
#                 elif ((candies_amount//candies_limit)%2==1) and ((candies_amount%candies_limit)>0) and (first_turn==2):
#                 # если целое от взятого - НЕчетное и при этом остаток >0 и я первый, то я проигрываю
#                     print(bots_answer(candies_taken), end=' '); candies_taken=(candies_amount//((candies_amount/candies_limit)+1))
#                 else:
#                     print(bots_answer(candies_taken), end=' '); candies_taken=(candies_amount//((candies_amount/candies_limit)+1))
#                 print('Бот взял {} конфет'.format(candies_taken))
#                 candies_amount-=candies_taken
#                 whose_turn=True



#-------------------------------------------
#Задача 3
# Создайте программу для игры в ""Крестики-нолики"".

# def print_matrix(lines):
#     for line in lines:
#         for i in range(len(line)):
#             print(line[i], end='')
#             if ((i*10)%2==0) and (i<2): print('|', end='')
#         print('')        
# def check_correct_input(str1):
#     coordinates = str1.split()   
#     if len(coordinates)!=2: print('Данные введены неверно. Нужно ввести 2 цифры через пробел.'); return False
#     for x in range(2):
#         if int(coordinates[x])<1 or int(coordinates[x])>3: print('Данные введены неверно. Числа должны бвть <=3 и >=1.'); return False
#     #проверяем занято ли поле
#     line1 = coordinates_matrix[int(coordinates[0])-1]
#     symbol1 = line1[int(coordinates[1])-1]
#     if (symbol1!='_') and (symbol1!=' '): print('клетка уже занята. '); return False
#     return True   
# def check_for_win (position):
#     line1 = coordinates_matrix[int(position[0])-1]
#     symbol1 = line1[int(position[1])-1]
#     if coordinates1[0]==symbol1 and coordinates1[1]==symbol1 and coordinates1[2]==symbol1: return True
#     if coordinates2[0]==symbol1 and coordinates2[1]==symbol1 and coordinates2[2]==symbol1: return True
#     if coordinates3[0]==symbol1 and coordinates3[1]==symbol1 and coordinates3[2]==symbol1: return True
#     if coordinates1[0]==symbol1 and coordinates2[0]==symbol1 and coordinates3[0]==symbol1: return True
#     if coordinates1[1]==symbol1 and coordinates2[1]==symbol1 and coordinates3[1]==symbol1: return True
#     if coordinates1[2]==symbol1 and coordinates2[2]==symbol1 and coordinates3[2]==symbol1: return True
#     if coordinates1[0]==symbol1 and coordinates2[1]==symbol1 and coordinates3[2]==symbol1: return True
#     if coordinates1[2]==symbol1 and coordinates2[1]==symbol1 and coordinates3[0]==symbol1: return True
#     return False

# input_str=''
# whose_turn=True
# steps=0
# coordinates1 = ['_','_','_',]
# coordinates2 = ['_','_','_',]
# coordinates3 = [' ',' ',' ',]
# coordinates_matrix = []; coordinates_matrix.append(coordinates1); coordinates_matrix.append(coordinates2); coordinates_matrix.append(coordinates3);
# print_matrix(coordinates_matrix)
# while (steps<9):
#     if (whose_turn):
#         input_str = input('Ставим крестик. Введите номер строки и номер столбца через пробел: ')
#         while (not check_correct_input(input_str)):
#             input_str = input('Ставим крестик. Введите номер строки и номер столбца через пробел: ')
#         coordinates = input_str.split() 
#         line = coordinates_matrix[int(coordinates[0])-1]
#         line[int(coordinates[1])-1]='X'
#         print_matrix(coordinates_matrix)
#         if (check_for_win(coordinates)): print("Игра закончена"); exit()
#         whose_turn=False; steps+=1
#     else:
#         input_str = input('Ставим нолик. Введите номер строки и номер столбца через пробел: ')
#         while (not check_correct_input(input_str)):
#             input_str = input('Ставим нолик. Введите номер строки и номер столбца через пробел: ')
#         coordinates = input_str.split() 
#         coordinates = input_str.split() 
#         line = coordinates_matrix[int(coordinates[0])-1]
#         line[int(coordinates[1])-1]='O'
#         print_matrix(coordinates_matrix)
#         if (check_for_win(coordinates)): print("Игра закончена"); exit()
#         whose_turn=True; steps+=1



#-------------------------------------------
#Задача 4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.      
     
# def rle_coding(data): 
#     encoding = ''; prev_char = ''; count = 1 
#     if not data: return '' 
#     for char in data: 
#         if char != prev_char: # если этот и пердыдущий не совпадают
#             if prev_char: #если не пустой
#                 encoding += str(count) + prev_char 
#             count = 1 
#             prev_char = char 
#         else: # счетчик увеличиваем, если совпадают
#             count += 1 
#     # завершаем encoding, когда строка закончилась 
#     encoding += str(count) + prev_char
#     return encoding
# def rle_decode(data): #декодирование
#     decode = '' 
#     count = '' 
#     for char in data:
#        if char.isdigit():
#           count += char 
#        else:  
#             decode += char * int(count) 
#             count = '' 
#     return decode
# decoded_val = rle_decode('6A1F2D7C1A17E') 
# print(decoded_val)
# regular_value = rle_coding('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE') 
# print(regular_value)



