print("--- Calculadora ---")
print("[ 1 ] – Tabuada")
print("[ 2 ] – Calculadora")
print("[ 3 ] – Números Pares")
print("[ 4 ] – Sair")
opcao = int(input("---> "))

if opcao == 1:
    print("--- Tabuada ---")
    numero = int(input("Digite um número: "))


    print(f"{numero} x 1 = {numero * 1}")
    print(f"{numero} x 2 = {numero * 2}")
    print(f"{numero} x 3 = {numero * 3}")
    print(f"{numero} x 4 = {numero * 4}")
    print(f"{numero} x 5 = {numero * 5}")
    print(f"{numero} x 6 = {numero * 6}")
    print(f"{numero} x 7 = {numero * 7}")
    print(f"{numero} x 8 = {numero * 8}")
    print(f"{numero} x 9 = {numero * 9}")
    print(f"{numero} x 10 = {numero * 10}")

elif opcao == 2:
    print("--- Calculadora ---")

    calculo = input("Digite o cálculo: ")
    calculo = calculo.strip().replace(" ", "")

    if "+" in calculo:
        pos = calculo.find("+")
        num1 = int(calculo[:pos])
        num2 = int(calculo[pos+1:])
        print(f"{num1} + {num2} = {num1 + num2}")

    elif "-" in calculo:
        pos = calculo.find("-")
        num1 = int(calculo[:pos])
        num2 = int(calculo[pos + 1:])
        print(f"{num1} - {num2} = {num1 - num2}")

    elif "*" in calculo or "x" in calculo:
        if "x" in calculo:
            pos = calculo.find("x")
        else:
            pos = calculo.find("*")

        num1 = int(calculo[:pos])
        num2 = int(calculo[pos + 1:])
        print(f"{num1} x {num2} = {num1 * num2}")

    elif "/" in calculo:
        pos = calculo.find("/")
        num1 = int(calculo[:pos])
        num2 = int(calculo[pos + 1:])
        if num2 == 0:
            print("Não é possível dividir por zero")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")

elif opcao == 3:
    print("--- Números pares--- ")
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")

elif opcao == 4:
    print("Saindo...")
else:
    print("Opção inválida...")