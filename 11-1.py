def func(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)
    return fact
a = func(3)
for i in range( a, 0,-1 ):
    func(i)
