# Program that asks for a input number and check if the number is
# a Prime number.

print ("To check if a number is prime.")
number = int(input("Enter the number you want to check: "))

x = number
y = 0

while x > 0:
    if (number % x) == 0:
       y += 1
    x -= 1
if y > 2 or y == 1:
    print ("The number is not prime")
else:
	print ("The number is prime")