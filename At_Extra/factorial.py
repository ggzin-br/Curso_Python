def factorial(num: int):
    if num == 0: return 1
    return num * factorial(num - 1)

print(factorial(int(input("$ "))))