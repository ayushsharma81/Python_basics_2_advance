"""
Q1: Take two numbers as input from the user. Print their sum, difference,
product, and remainder.
"""

num1=int(input("Enter a number= "))
num2=int(input("Enter second number= "))
sum=num1+num2
diff=(num1-num2)
mul=num2*num1
rem=num1%num2

print(f"sum={sum}\ndifference={diff}\nmultipy={mul}\nremainder={rem}")