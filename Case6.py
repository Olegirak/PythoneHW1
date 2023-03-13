# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no
n = int(input("Введите 6-значный номер билета "))
if n//1000000 >=1:
    print("Ошибка ввода")
else:
    d1 = n//1000
    d2 = n%1000
    if (d1//100+d1%10+d1%100//10)==(d2//100+d2%10+d2%100//10):
        print("Билет счастливый")
    else:
        print("Билет несчастливый")