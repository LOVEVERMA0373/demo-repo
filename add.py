def fibonacci_iterative(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Generate the first 10 terms
print(fibonacci_iterative(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
