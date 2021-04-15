# First few terms of Fib:
# 1, 1, 2, 3, 5, 8, 13, 21
# Each term is the sum of the previous 2 terms
# So a fib number of 10 would equal 13, why? idk

# Slow way
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))
for i in range(1, 20):
    print(i, ":", fibonacci(i))