def fib_non_recursive(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

n = int(input("Enter n: "))
print("1. Recursive\n2. Non-Recursive")
ch = int(input("Enter choice: "))

if ch == 1:
    for i in range(n):
        print(fib_recursive(i), end=" ")
elif ch == 2:
    fib_non_recursive(n)
else:
    print("Invalid choice")