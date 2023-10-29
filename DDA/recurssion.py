# recurssive implimentation of fibonacci series
print("Fibonacci Series")
def fibonacci(num):
    if num < 1:
        return None
    elif num < 3:
        return 1
    elem1 = elem2 = 1
    # sum
    sum = 0
    for i in range(3, num + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum

    return sum

for i in range(1, 10):
    print(f"{i} => {fibonacci(i)}", end='\n')


# Recurssive implimentation of factorial
print("\n\nFactorial")

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

for i in range(1, 10):
    print(f"{i} => {factorial(i)}", end='\n')

