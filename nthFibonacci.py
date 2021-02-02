def nthFibonacci(nth):
    if(nth <= 2): return 1
    return nthFibonacci(nth-1)  + nthFibonacci(nth - 2)

print(nthFibonacci(6))
print(nthFibonacci(7))
print(nthFibonacci(8))