from random import randint
aleatorio=randint(0,10)
print("--- PAR ou ÍMPAR ---")
vitorias=0
while True:

    numero = int(input("Escolha um número de 0 a 10 "))
    if  numero > 10 or numero < 0:
        print("Valor inválido, escolha um número de 0 a 10")
        continue

    while True:
       opcao = input("Par ou Ímpar? ").lower()
       if opcao == "par" or opcao == "impar":
          break
       else:
          print("Opção inválida, escolha par ou impar")





    if opcao == "par":
        if (aleatorio + numero) % 2 == 0:
            print(f"{aleatorio + numero} é par")
            vitorias += 1
            print("Ganhou!!")
        else:
            print(f"{aleatorio + numero} é ímpar")
            print("Perdeu!!")
            break
    elif opcao == "impar":
        if (aleatorio + numero) % 2 == 0:
            print(f"{aleatorio + numero} é par")
            print("Perdeu!!")
            break
        else:
            print(f"{aleatorio + numero} é ímpar")
            vitorias += 1
            print("Ganhou!!")


print(f"{vitorias} vitórias consecutivas")
