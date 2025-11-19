maior25=0
mulheres=0
homens_menos17=0
menor_idade=0

while True:
    idade=int(input("Qual a idade? "))
    genero=input("Qual o género? ").upper()
    if genero != "F" and genero != "M":
        print("Resposta inválida, responda com F ou M")
        genero = input("Qual o género? ").upper()
    continuar =input("Deseja continuar? ").lower()
    if "ã" in continuar:
        continuar= continuar.replace("ã","a")

    if genero == "F":
        mulheres += 1
    elif genero == "M" and idade < 17:
        homens_menos17 += 1
    if idade > 25:
        maior25 += 1
    elif idade < 18:
        menor_idade += 1
    if continuar != "sim" and continuar != "nao":
        print("Resposta inválida, responda com sim ou não")
        continuar = input("Deseja continuar? ").lower()
    elif continuar == "sim":
        print("Registre outra pessoa:")
    elif continuar == "nao":
        break


print(f"{maior25} pessoas têm mais de 25 anos")
print(f"{homens_menos17} homens com menos 17 anos foram registrados")
print(f"{mulheres} mulheres foram registradas")
print(f"{menor_idade} menores de idade foram registrados")



