
# input_1 = int(input("Enter the height in cm: "))
# if input_1 > 120:
#     print("Can ride")
#     age = int(input("Enter the age: "))
#     if age < 12:
#         bill = 5
#         print("Pay $5")
#     elif (age <= 18):
#         bill = 7
#         print("pay $7")
#     else:
#         bill = 12
#         print('pay $12')
#     photo = input("Want a photo copy Y or N?\n")
#     if photo == 'Y':
#         #Add $3 to the Bill
#         bill += 3
#         print(f"Your total bill amount: {bill}")
#     else:
#         print(f"Your total bill amount: {bill}")
# else:
#     print("Can't ride")
#
# #---------------------------------
# # number = int(input("Which number do you want to check? "))
# # if number % 2 == 0:
# #     print("This is an even number.")
# # else:
# #     print('This is an odd number.')
#
# #__________________________________
#
# # height = float(input("enter your height in m: "))
# # weight = float(input("enter your weight in kg: "))
# # bmi = round(weight/height**2)
# # if bmi < 18.5:
# #     print(f"Your BMI is {bmi}, you are underweight.")
# # elif (bmi > 18.5) & (bmi < 25):
# #      print(f"Your BMI is {bmi}, you have a normal weight.")
# # elif (bmi > 25) & (bmi < 30):
# #      print(f"Your BMI is {bmi}, you are slightly overweight.")
# # elif (bmi > 30) & (bmi < 35):
# #      print(f"Your BMI is {bmi}, you are obese.")
# # else:
# #      print(f"Your BMI is {bmi}, you are clinically obese.")
#
# #------------------------------------------------------------
# # LEAP YEAR
# #------------------#
# # year = int(input("Enter the year: "))
# # if year % 4 == 0:
# #     if year % 100 == 0:
# #         if year % 400 == 0:
# #             print("Leap year. ")
# #         else:
# #             print("Not leap year")
# #     else:
# #         print("Leap year.")
# # else:
# #     print("Not leap year")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L?")
# add_pepperoni = input("Do you want pepperoni? Y or N? ")
# extra_cheese = input("Do you want extra cheese? Y or N?")
# if size == 'S':
#     bill = 15
#     if add_pepperoni == 'Y':
#         bill += 2
#     elif extra_cheese == 'Y':
#         bill += 1
#     print(f"Your final bill is: ${bill}.")
# elif size == 'M':
#     bill = 20
#     if add_pepperoni == 'Y':
#         bill += 3
#     elif extra_cheese == 'Y':
#         bill += 1
#     print(f"Your final bill is: ${bill}.")
# elif size == 'L':
#     bill = 25
#     if add_pepperoni == 'Y':
#         bill += 3
#     elif extra_cheese == 'Y':
#         bill += 1
#     print(f"Your final bill is: ${bill}.")

#_________________________________________
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
# upper_case = name1.upper() + name2.upper()
# name_true = upper_case.count("T") + upper_case.count("R") + upper_case.count("U")+ upper_case.count("E")
# name_love = upper_case.count("L") + upper_case.count("O") + upper_case.count("V")+ upper_case.count("E")
# love_score = int(str(name_true) + str(name_love))
# if love_score<10 or love_score>90:
#     print(f"Your score is{love_score}, you go together like coke and mentos.")
# elif love_score>=40 and love_score<=50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}")
#__________________________________________________

# input_1 = input("Where do you want to go L or R?")
# input_2 = input("What do you want to do swim or wait?")
# input_3 = input("which door R,B or Y?")
# if input_1 == 'L':
#     if input_2 == 'wait':
#         if input_3 == 'R':
#             print("Game Over!!")
#         elif input_3 == "B":
#             print("Game Over!!")
#         else:
#             print("You Win!!")
#     else:
#         print("Game over!!")
# else:
#     print("Game Over!!")

