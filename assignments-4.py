Assignment - 4 (Is it a Prime Number?)

Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.

The examples of the desired output are as follows :

input →  19 ⇉ output : 19 is a prime number
input →  10 ⇉ output : 10 is not a prime number
Note that ⚠: This question is famous on the web, so to get more benefit from this assignment, try to complete this task on your own.


_____________________________________________________________________________________

number = int(input("Bir sayı giriniz: "))
liste = []

for i in range(1, number+1):
    if number % i == 0:
        liste.append(i)
if liste == [1, number]:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
