numeros= []

contador=0

for c in range(0,10):
    numero=int(input(f"Insira o {c+1}º número "))
    if numero not in numeros:
        numeros.append(numero)
        contador += 1
    else:
        print(f"O valor {numero} já se encontra na lista")

numeros.sort(reverse=True)
for numero in numeros:
    print(f"{numero}-->" , end="")
