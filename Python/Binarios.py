"""
Método que conviete un número a binarios 
"""
def binario(n):
    if n/2 == 0:
        return n
    else:
        return (n%2) + 10 * binario(n//2)


print("Ingrese un número decimal")
print(binario(int(input())))


