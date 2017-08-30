def mod(a,b):
    if a<b:
        return a
    else:
        return mod(a-b,b)

print("Ingrese un numero")
a=int(input())
print("Ingrese un numero")
b=int(input())
print(mod(a,b))

