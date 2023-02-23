# num_char = str(len(input("what is your name?\n")))
# print('your name has '+num_char+' characters.')
# print(70+float(100))

# num1 = str(input("a : "))
# num2 = str(input("b : "))
# num3 = num1
# num1 = num2
# num2 = num3
# print("a: "+num1+"\nb: "+num2)

# height = float(input("enter your height in m: "))
# weight = int(input("enter your weight in kg: "))
# bmi = weight/(height**2)
# print(int(bmi))

# a=19
# b=1.23
# c=True
# print(round(a/b,2))
# print(f"your score {a},value of b {b}, value of c {c}")

print("Welcome to the tip calculator")
print("--------------------------------")
bill_amt = float(input("Enter the total bill amount?$"))
tip = int(input("what percentage tip would you like to give?\n10,12,or15?\n"))
bill_amt += bill_amt*(tip/100)
split = int(input("enter the no. of person?"))
total_amt = round(float(bill_amt)/split,2)
print(f"Each person should pay:$ {total_amt}")
