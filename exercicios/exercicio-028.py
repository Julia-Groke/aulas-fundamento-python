
from random import randint

aleatorio = randint(0, 7)


print("JOGO DA ADIVINHA")



jogada = int(input("Escolha um número entre 0 e 7 "))


if jogada == aleatorio:
    print("GANHOU!!!")
    print(f"Eu pensei em {aleatorio} e você jogou {jogada}.")
else:
    print("PERDEU!!")
    print(f"Eu pensei em {aleatorio} e você jogou {jogada}.")