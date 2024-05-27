def factorial(x):
    f = 1
    if x == 0:
        return 1
    else:
        while x > 0:
            f = f*x
            x -= 1
    return f
while True:
    number = int(input("input a number to calculate its factorial:"))
    print("the factorial of",number," is", factorial(number))
    y = ("do you want to continue, yes or no").upper()
    if y =="NO":
        break
