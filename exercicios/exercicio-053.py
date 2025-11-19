from random import randint

numeros=(randint(0,10),
         randint(0,10),
         randint(0,10),
         randint(0,10),
         randint(0,10))

maior=0 #max
menor=0 #min

print("Números gerados:")
for numero in numeros:
    print(f"\t{numero}",end=" ")

    if numero == numeros[0]:
        menor=numero
        maior=numero
    else:
        if numero > maior:
            maior=numero
        if numero < menor:
            menor=numero


print()
print(f"O maior número encontrado é: {maior}")
print(f"O menor número encontrado é: {menor}")
