#FUNCTION: PARAMETERS AND ARGUMENTS


# # Review:
# # Create a function called greet().
# def greet(name,location):
#     # Write 3 print statements inside the function.
#     print(f"Hello {name},{location}")
#     # print(f"Hi {name}")
#     # print(f"Have a good day {name}")
# # Call the greet() function and run your code.
# greet("Hitesh","Bengaluru")
#----------------------------------------------

# #Functions with more than one inputs
# def greet(name,state,location):
#     print(f"Hello {name} from :{location},{state}")
# #Positional Arguments passed to the parameters
# greet("hitesh","pune","Sarojini Nagar")
# #To miss out order of any arguments we can assign parameter while calling
# #the fuction
# greet(name="Hitesh",location="Bengaluru",state="Karnataka")
#----------------------------------------------------------------

# def paint_calc(height,width,cover):
#     cans = (height*width)/cover
#     print(f"You'll need {cans} cans of paint")
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
#
# paint_calc(height=test_h, width=test_w, cover=coverage)
# ---------------------------------------------------------------
#PRIME NUMBER
# def prime_checker(number):
#     count = 0
#     if number > 1:
#         for i in range(2, int(number / 2) + 1):
#             if (number % i) == 0:
#                 count += 1
#         if count > 0:
#             print("It's not a prime number.")
#         else:
#             print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
# n = int(input("Check this number: "))
# prime_checker(number=n)
# -----------------------------------------------------------
# import math
#The way to approximate the value to highest and lowest
# # number = math.ceil(5.4)
# # number = math.floor(5.4)
# print(number)
#------------------------------------------

