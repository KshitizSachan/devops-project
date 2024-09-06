
# 1. Hello, World!
print("Hello, World!")

# 2. Sum of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum is:", sum)

# 3. Check if a Number is Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# 4. Find the Factorial of a Number
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")

# 5. Check if a Number is Prime
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# 6. Fibonacci Series up to n terms
n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence up to 1 term:", a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a)
        nth = a + b
        a = b
        b = nth
        count += 1

# 7. Reverse a String
string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

# 8. Find Largest of Three Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(f"The largest number is: {largest}")
