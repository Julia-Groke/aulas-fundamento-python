valores=(int(input("Insira um valor ")),int(input("Insira um valor ")),
         int(input("Insira um valor ")),int(input("Insira um valor ")))

numero7=0
numero5=False
indice_5=""
pares=0


for c in range(0,4):
    if valores[c] == 7:
        numero7 += 1
    if valores[c] == 5:
        if not numero5:
            indice_5=c
            numero5=True




if numero7 > 0:
    print(f"O número 7 aparece {numero7} vezes")
else:
    print("Não foi encontrado o número 7")

if indice_5:
    print(f"O número 5 foi digitado na posição {indice_5 + 1} ")
else:
    print("Não foi encontrado o número 5")










