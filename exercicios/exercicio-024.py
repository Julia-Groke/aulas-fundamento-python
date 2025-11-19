print("--- RADAR DE VELOCIDADE ---")

limite = 80
velocidade = int(input("Insira a velocidade "))

multa = 100 + 7 * (velocidade - limite)

if velocidade > limite:
    print("-> MULTADO <-")
    print(f"MULTA: {multa:.2f}€ ")
else:
    print("Não multado! Boa Viagem!")