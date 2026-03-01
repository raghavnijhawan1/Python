
base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (n): "))

result = 1
for i in range(exponent):
    result = result * base
print(f"The result of {base} to the power of {exponent} is: {result}")
