# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8



def stepen(a,b,res=1):
    if b==0:
         return res 
    return stepen(a,b-1,res*a)
     
        

number_A=int(input("Введите число, которое необходимо возвести в степень: "))
number_B=int(input("Введите степень числа: "))
print(stepen(number_A,number_B))