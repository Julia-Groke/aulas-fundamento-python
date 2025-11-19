maior = menor = 0


for c in range(0,10):

    idade=int(input(f"Qual a idade da {c+1}ª pessoa? "))
    if c == 0:
        maior = idade
        menor = idade
    else:
        if idade > maior :
           maior = idade
        if idade < menor:
           menor = idade





print(f"A maior idade foi {maior} e a menor idade foi {menor}")

