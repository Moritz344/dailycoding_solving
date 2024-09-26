def is_fibo(a,b,f):
    # 0 1 1 2 3 5 8 13
    
    if f == b or f == a:
        return True

    while b < f:
        # Berechne die nächste fib zahl
        a,b = b,a + b

        return True 

    return False


print(is_fibo(0,1,2))

