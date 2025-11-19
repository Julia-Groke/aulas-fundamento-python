from random import randint

print("--- Pedra, Papel, Tesoura ---")

print("[1] - Pedra")
print("[2] - Papel")
print("[3] - Tesoura")

jogador = int(input('---> '))
aleatorio = randint(1, 3)

if jogador == 1:
    if aleatorio == 1:
        print("Empate")
        print(f"Computador: {aleatorio}")
        print(f"Jogador: {jogador}")
    elif aleatorio == 2:
        print("Computador ganhou")
        print(f"Computador: {aleatorio}")
        print(f"Jogador: {jogador}")
    elif aleatorio == 3:
        print('Jogador ganhou')
        print(f"Computador: {aleatorio}")
        print(f"Jogador: {jogador}")

elif jogador == 2:
    if aleatorio == 1:
        print("Jogador ganhou")
        print(f"Computador: {aleatorio}")
        print(f"Jogador: {jogador}")
    elif aleatorio == 2:
        print("Empate")
        print(f"Computador: {aleatorio}")
        print(f"Jogador: {jogador}")
    elif aleatorio == 3:
        print("Computador ganhou")
        print(f"Computador: {aleatorio}")
        print(f"Jogador: {jogador}")

elif jogador == 3:
    if aleatorio == 1:
        print("Computador ganhou")
        print(f"Computador: {aleatorio}")
        print(f"Jogador: {jogador}")
    elif aleatorio == 2:
        print("Jogador ganhou")
        print(f"Computador: {aleatorio}")
        print(f"Jogador: {jogador}")
    elif aleatorio == 3:
        print("Empate")
        print(f"Computador: {aleatorio}")
        print(f"Jogador: {jogador}")

else:
    print("Jogada invalida.")