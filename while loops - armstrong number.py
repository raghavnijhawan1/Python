a = int(input("enter num: "))
b = a
s = 0
while b > 0:
    c = b % 10
    s = s + c ** 3
    b = b//10
if s == a:
    print("Armstrong number")
else:
    print("Not armstrong number")
