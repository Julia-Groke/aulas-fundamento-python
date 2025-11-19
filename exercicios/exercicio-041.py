resposta=""
print("O céu é azul?")
while resposta != "V" and resposta != "F":
    resposta=input("[ V / F ]").strip().upper()
    if resposta == "V":
        print("Acertou!! Vamos para a próxima")
    elif resposta == "F":
        print("Errou!")
    else:
        print("Resposta inválida")

resposta=""
print("A grama é rosa?")
while resposta != "V" and resposta != "F":
    resposta = input("[ V / F ]").strip().upper()
    if resposta == "F":
        print("Acertou!! Vamos para a próxima")
    elif resposta == "V":
        print("Errou!")
    else:
        print("Resposta inválida")


print("O formador é o Ricardo?")
while True:
    resposta = input("[ V / F ]").strip().upper()
    if resposta == "V":
        print("Acertou!! Fim!")
        break
    elif resposta == "F":
        print("Errou!")
        break
    else:
        print("Resposta inválida")

