antecessor = 0
atual = 1
sucessor = antecessor + atual

sequencia=int(input("Digite um valor: "))


if sequencia == 0:
    print("Inválido")
elif sequencia == 1:
    print(antecessor)
elif sequencia == 2:
    print(f"{antecessor} --> {atual}")
else:
    print(f"{antecessor} --> {atual}",end=" ")
    sequencia = sequencia - 2


    while sequencia >= 1:
       sucessor = antecessor + atual
       print(f"--> {sucessor}", end=" ")
       antecessor = atual
       atual = sucessor
       sequencia -= 1
