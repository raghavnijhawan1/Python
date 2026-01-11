x = 10
y = 10

if x is y:
    print("The values are the same")
    print(id(x), id(y))
else:
    print("The values are different")
    print(id(x), id(y))
