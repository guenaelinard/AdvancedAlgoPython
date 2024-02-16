
def factorial(n):
    if n == 0 :
        return 1
    else: F = 1
    for i in range(2, n+1) :
            F = F * i
            print(F, n, i)
    return F

# factorial(5)

def fibonacci(n) :
    if n == 0 or n == 1:
        return n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        print(fibonacci(n-1), fibonacci(n-2), result)
        return result

# fibonacci(8)

def syracuse(n) :
    while n != 1 :
        if n %2 == 0 :
            n = n//2
            print(n, end=" ")
        else :
            n =3 * n + 1
            print(n, end=" ")
    print(n)
    return n

# syracuse(15)

def pgcd(n,m) :
    if m == 0 :
        return n
    else :
        return pgcd(m, n % m)

# print(pgcd(21, 72))