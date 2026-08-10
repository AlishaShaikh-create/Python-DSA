def FibonacciSeries(n):
    if n == 0:
        return 0
    if n ==1:
        return 1
    return FibonacciSeries(n-1)+FibonacciSeries(n-2)

print(FibonacciSeries(3))