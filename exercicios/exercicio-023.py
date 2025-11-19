palavra = input("Digite uma palavra de 6 letras: ").strip()


for c in range(0,6):

    if len(palavra) == 6:
        print(palavra[::-1])
        break
    else:
        print("Palavra inválida")
        palavra = input("Digite uma palavra de 6 letras: ").strip()
