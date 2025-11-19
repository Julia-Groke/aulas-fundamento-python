maior=0
menor=0
soma=0
contagem=0
while True:
    nota=float(input(f"Insira a {contagem+1}ª nota [0 para parar]: "))
    if nota == 0:
        break

    if contagem == 0:
        maior = menor = nota
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota


    contagem += 1
    soma += nota

media= soma/contagem

print(f"Inseriu {contagem} notas")
print(f"A média é: {media:.2f}")
print(f"A maior nota inserida é: {maior}")
print(f"A menor nota inserida é: {menor }")


