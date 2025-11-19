numeros= []



for c in range(0,5):
    numero=int(input(f"Insira o {c+1}º número "))
    numeros.append(numero)

maior= max(numeros)
menor= min(numeros)

pos_maior= numeros.index(maior)
pos_menor= numeros.index(menor)




print(f"O maior número foi o {maior} na posição {pos_maior} ")
print(f"O menor número foi o {menor} na posição {pos_menor} ")

