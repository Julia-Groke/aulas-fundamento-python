from random import randint

aleatorio= randint (0, 10)

print("--- JOGO DA ADIVINHA ---")


tentativas=0

while True:
    tentativas +=1
    jogada=int(input("Escolha um número de 1 á 10 "))
    if jogada != aleatorio:
        print("Errou! Tente novamente")
    elif jogada == aleatorio:
        print("Acertou!!!")
        break
print(f"{tentativas} tentativas")
