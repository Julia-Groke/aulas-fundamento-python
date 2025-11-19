numeros=[]
pares=[]
impares=[]

for c in range(0,10):
    numero=int(input(f"Insira o {c+1}º número "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(numeros)
print(pares)
print(impares)