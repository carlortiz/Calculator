first_number = float(input("Enter First Number: "))
operator = input("The operators are '+', '-', '*', and '/'. \nEnter Operator: ")
second_number = float(input("Enter Second Number: "))
answer = 0.0

if operator == "+":
   answer = first_number + second_number
elif operator == "-":
   answer = first_number - second_number
elif operator == "*":
   answer = first_number * second_number
elif operator == "/":
   answer = first_number / second_number
else:
   print("You have failed to put an operator.")
   str(answer)
   answer = "N/A"

print("Answer: " + str(answer))
