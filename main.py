num = int(input("Enter a number"))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("Factorial is", factorial)
