numeros= []

for c in range(0,5):
    numero=int(input(f"Insira o {c+1}º número "))

    if c==0:
        numeros.append(numero)
        print("Primeiro valor inserido com sucesso")
        continue

    if numero > numeros[-1]:
        numeros.append(numero)
        print("Valor inserido na última posição")
    else:
        indice=0
        while indice < len(numeros):
            if numero <= numeros[indice]:
                numeros.insert(indice,numero)
                print(f"Valor inserido na posição {indice+1}")
                break
            indice+=1

print(numeros)