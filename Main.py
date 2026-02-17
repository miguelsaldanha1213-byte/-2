#calculator
num1=float(input("digit the first number."))
num2=float(input("digit the second number."))
op=input("does your sentence has a third number?")
if op == "yes":
  num3=float(input("digit the third number"))
  else:
  print("Error...")
operation=input("choose 1 for adition, 2 for multiplication and 3 for subtraction")
if operation == "1":
  print(num1+num2+num3)
elif operation == "2":
  print(num1*num2*num3)
elif operation == "3":
  print(num1-num2-num3)
else:
  print("error...")

