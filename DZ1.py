#1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

 N = int(input('Введите цифру '))
 if N > 5:
     print('да')
 else:
     print('нет') 
 
#_____________________________________________________________________________________________________________________________    

#2.Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

 for X in range (0,2):
     for Y in range (0,2):
         for Z in range (0,2):
             print(f'{X},{Y},{Z}')
 print(f'{(not (X or Y or Z)) == (not X and not Y and not Z)}')

#______________________________________________________________________________________________________________________________


#3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

 X = int(input('Введите X '))
 Y = int(input('Введите Y '))
 X != 0
 Y != 0
 if X>0 and Y>0:
     print('1')
 if X<0 and Y>0:
     print('2')    
 if X<0 and Y<0:
     print('3')
 if X>0 and Y<0:
     print('4')

#______________________________________________________________________________________________________________________________

#4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

 N = int(input('Введите номер четверти '))
 if N == 1:
     print('x>0 и y>0')
 elif N == 2:
     print('x<0 и y>0')
 elif N == 3:
     print('x<0 и y<0')
 elif N == 4:
     print('x>0 и y<0')

#______________________________________________________________________________________________________________________________
 
#5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21   

import math
X1 = int(input('Введите коррдинаты точки X1 '))
Y1 = int(input('Введите коррдинаты точки Y1 '))
X2 = int(input('Введите коррдинаты точки X2 '))
Y2 = int(input('Введите коррдинаты точки Y2 '))
R= math.sqrt((X1*Y1)**2 + (X1*Y1)**2)
print(f'{ R = :.2f}')