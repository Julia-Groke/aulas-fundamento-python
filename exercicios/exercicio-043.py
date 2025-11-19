valor1=int(input("Insira o 1º valor "))
valor2=int(input("Insira o 2º valor "))
valor3=int(input("Insira o 3º valor "))
soma = 0
multiplicacao=0
maior=0
while True:
    print("--- MENU ---")
    print("[1] SOMAR")
    print("[2] MULTIPLICAR")
    print("[3] MAIOR")
    print("[4] NOVOS NÚMEROS")
    print("[5] SAIR DO PROGRAMA")
    opcao=int(input("---> "))
    if opcao == 1:
        soma += (valor1+valor2+valor3)
        print(f"A soma dos valores é: {soma}")
    elif opcao == 2:
        multiplicacao += (valor1*valor2*valor3)
        print(f"A multiplicação dos valores é: {multiplicacao}")
    elif opcao == 3:
        if valor1 > maior:
            maior = valor1
            if valor2 > maior:
                maior = valor2
                if valor3 > maior:
                    maior = valor3
        print(f"O maior valor é: {maior}")
    elif opcao == 4:
        print("Insira novos valores: ")
        valor1 = int(input("Insira o 1º valor "))
        valor2 = int(input("Insira o 2º valor "))
        valor3 = int(input("Insira o 3º valor "))
    elif opcao == 5:
        print("A sair...")
        break
    else:
        print("Opção inválida")






