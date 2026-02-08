inp = input("Enter a string: ")
a = inp
b = ("")
for i in a:
    b = i + b
print(f"Normal string: {a}")
print(f"Reversed string: {b}")
