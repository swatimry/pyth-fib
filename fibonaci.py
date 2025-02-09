def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter a number to find the Fibonacci sequence: "))


print(f"Fibonacci of {n} is {fibonacci(n)}")
print("Checking jenkins build  ")

