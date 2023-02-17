#Let's Go
# Fruits = ["apple","lemon","Banana"]
# # FOR LOOP
# for fruits in Fruits:
#     print(fruits + " Pie")
#---------------------------------------------
#average heights
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#WE CAN USE SUM() AND LEN() FUCTION FOR MORE EASIER WAY
# student_list = 0
# for i in range(0,len(student_heights)):
#     student_list += student_heights[i]
# average_height = round(student_list/len(student_heights))
# print(average_height)
# print(student_heights[-1]/len(student_heights))
#----------------------------------------------
#Higest Number without using Max() and Min() function

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# for i in range(0,len(student_scores)):
#     if student_scores[i] > minimum:
#      minimum = student_scores[i]
# print(f"The highest score in the class is: {minimum}")
# _________________________________________________________
#Print sum of all numbers from 1 to 100
# even = 0
# for i in range(2,101,2):
#     even += i
# print(even)
# #Printing number of odd numbers from 1to 100
# odd = 0
# for i in range(1,101,2):
#     odd+=i
# print(odd)
#Printing number of prime numbers from 1 to 100
# prime=0
# count =0
# print('2\n3\n5\n7\n')
# for i in range(2,101):
#    if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 !=0:
#       print(i)
#       prime+=i
# value = prime+2+3+5+7
# print(value)
#------------------------------------------------------
# for i in range(1, 101):
#     if (i % 3 == 0) and (i % 5 == 0):
#         i = "FizzBuzz"
#     elif i % 3 == 0:
#         i = "Fizz"
#     elif i % 5 == 0:
#         i = "Buzz"
#     print(i)
#----------------------------------------------



#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# #Eazy Level - Order not randomised:
# # #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#_----------"USE RANDOM.CHOICE(LIST)-->FOR SELECTING RANDOM CHARCTERS FROM LIST"----------
# # password = ""
# # for n in range(1,nr_letters+1):
# #    password += random.choice(letters)
# # for n in range(1,nr_symbols+1):
# #    password += random.choice(symbols)
# # for n in range(1,nr_numbers+1):
# #    password += random.choice(numbers)
# # print(password)
# ///--------------------------------///
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#---------"USE RANDOM.SHUFFLE() [DOESNOT RESTURN VALUE SO DONOT ASSIGN ] FOR REORDERING THE LIST"---------
# password = ""
# for n in range(1,nr_letters+1):
#    password += random.choice(letters)
# for n in range(1,nr_symbols+1):
#    password += random.choice(symbols)
# for n in range(1,nr_numbers+1):
#    password += random.choice(numbers)
# print(password)
# password_list = (" ".join(password).split())
# # print(password_list)
# random.shuffle(password_list)
# # print(password_list)
# # password="".join(password)
#////--------FOR CONVERTING STRING TO LIST OR VIVE OR VERSA USE FOR LOOP BY
# CONCATENATION OR SLIPT() AND JOIN() FUNCTION------//////
# new_password=""
# for char in password_list:
#    new_password += char
# print(new_password)
