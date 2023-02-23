#FUNCTIONS WITH OUTPUTS
# def format_name():
#     f_name ="Hitesh"
#     l_name = "N"
#     return f_name,l_name
# result={"Name":[format_name()]}
# print(result)
#--------------------------------
# def format_name(f_name,l_name):
#     f_name=f_name.title()
#     l_name=l_name.title()
#     return f_name,l_name
# f_name =input("Fisrt Name:").lower()
# l_name =input("lower case:").lower()
# result={"Name":[format_name(f_name,l_name)]}
# print(result)
#-----------------------------------
# def format_name(f_name,l_name):
#     if f_name=='' or l_name=='':
#         return "Provide Valid inputs"
#     else:
#         f_name =f_name.title()
#         l_name = l_name.title()
#         return f'Resule:{f_name} {l_name}'
# print(format_name(input("Enter Firstname:").lower(),input("Enter Lastname:").lower()))
#-----------------------------------------------------------------------------
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         # print("Leap year.")
#         return True
#       else:
#         # print("Not leap year.")
#         return False
#     else:
#     #   print("Leap year.")
#       return True
#   else:
#     # print("Not leap year.")
#     return False
#
# def days_in_month(year,month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if year== False:
#      return month_days[month-1]
#   elif year== True:
#       if month==2:
#           return month_days[month-1]+1
#       else:
#           return month_days[month-1]
# days = days_in_month(is_leap(int(input("Enter a year: "))),int(input("Enter a month: ")))
# print(days)
#----------------------------------------------------------
#calculator
from Calculator_art import logo
def add(n1,n2):
  '''Adds two Numbers'''
  return n1+n2
def sub(n1,n2):
  '''Subtracts Two numbers'''
  return n1-n2
def mul(n1,n2):
  '''Multiplies two numbers'''
  return n1*n2
def divide(n1,n2):
  '''Divide two numbers'''
  return round((n1/n2),4)


operations ={
"+":add,
"-":sub,
"*":mul,
"/":divide
}
def Calculator():
    '''This fuction will calculate the values for the set of
    operations the user enter and user can also wish to continue
    by:yes or no or refresh  accordingly'''
    print(logo)
    n1 = float(input("Enter the First Number:"))
    to_continue = "yes"
    while to_continue=='yes':
      for operator in operations:
        print(operator)
      chosen_operator = input("Enter the operator:")
      operation_func = operations[chosen_operator]
      n2 = float(input("Enter the Second Number:"))
      answer = operation_func(n1,n2)
      print(f"{n1}{chosen_operator}{n2} = {answer}")
      to_continue = input("Do you wish to continue?Type 'yes','no''refresh':").lower()
      n1 = answer
    if to_continue=="no":
      print("Good Bye!")
    elif to_continue=='refresh':
      Calculator()
Calculator()