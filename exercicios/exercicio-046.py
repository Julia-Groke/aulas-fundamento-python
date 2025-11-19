soma=0
contador=0
while True:
    numero=int(input("Insira um número "))
    if numero != 0:
        contador += 1
        soma += numero
    else:
        break
print(f"O utilizador inseriu {contador} números ")
print(f"A soma dos números é {soma}")
