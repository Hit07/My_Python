#Let's Go
#DICTIONARIES AND NESTING LIST

# Vehicles={
# "Bus":"Toyato",
# "Car":"Lambo",
# "Lorry":123
# }
# # #Retreiving elements from Dictionary
# # print(Vehicles["Lorry"])
# # #Adding Key-Value pair to the dictionary
# # Vehicles["Helicopter"]=345
# # print(Vehicles)
# #Create an empty dictionary
# # new_dictionary ={}
# # new_list=[]
# # print(new_list,new_dictionary)
# #looping through dictionary
# # for key in Vehicles:
# #     print(key)
# #     print(Vehicles[key])
# new_dictionary = Vehicles.copy()
# print(new_dictionary)
#--------------------------------------
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# student_grades = student_scores.copy()
# for key in student_grades:
#     if student_grades[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif student_grades[key] > 80:
#         student_grades[key] = "Exceeds Expectation"
#     elif student_grades[key] > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
# print(student_grades)
#----------------------------------------------------
#Nesting a list in a Dictionary

# travel_log={
# 'Karnataka':['Bengaluru','Mysore','Mahalakshmilayout'],
# 'Pune':'Mumbai',
# 'Tmail_Nadu':'Chennai',
# }
# print(travel_log["Karnataka"])

#Nesting a dictionary inside a Dictionary
# travel_log={
# 'Karnataka':{'Bengaluru':['Mahalakshmilayout','BullTemple'],'Mysore':'Palace',},
# 'Pune':'Mumbai',
# 'Tmail_Nadu':'Chennai',
# }
# print()
# print(travel_log["Karnataka"]["Bengaluru"])

#Nesting Dictionary in list
#
# travel_log=[
#     { 'Karnataka':'Bellary',
#       'Bengaluru':'Orion Mall'},
#     {'Mahalakshmilayout':'BullTemple'},
#     {'Pune':'Mumbai',
#      'Tmail_Nadu':'Chennai',
#     }
# ]
# print(travel_log[0]['Karnataka'])
#---------------------------------------------
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# def add_new_country(Country_name,No_visits,City):
#   last_element = {
# "Country":Country_name,
# "visits":No_visits,
# "cities":City
# }
#   travel_log.append(last_element)
#
#
# add_new_country(Country_name="Russia", No_visits=2, City=["Moscow", "Saint Petersburg"])
# print(travel_log)
# #---------------------------------------------------------------------------------------------
#BIDING THE HIGHEST AMOUNT
from replit import clear
import art

# HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("-------------------------------------------------------------")

name = input("What is your name?")
bid = int(input("What is your bid?$"))
to_continue = input("Are there any other bidder?Type 'Y'or'N:")
log = {}
log[name] = bid
while to_continue == 'Y':
    clear()
    name = input("What is your name?")
    bid = int(input("What is your bid?$"))
    to_continue = input("Are there any other bidder?Type 'Y'or'N':")
    log[name] = bid
if to_continue == 'N':
    print(log)
    # print(max(log))
    a = 0
    b = ''
    for key in log:
        if log[key] > a:
            a = log[key]
            b = key
print(f"The winner is {b} with bid of {a}")
