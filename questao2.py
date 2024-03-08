def sequencia(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def is_in_fibonacci(num):
    fib = sequencia(num)
    if num in fib:
        return True
    else:
        return False

# Verificacao
number = int(input("Informe um numero: "))

if is_in_fibonacci(number):
    print(f"O numero {number} pertence à sequência de Fibonacci.")
else:
    print(f"O numero {number} não pertence à sequência de Fibonacci.")
