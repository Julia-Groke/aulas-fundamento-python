altura=float(input("Qual a sua altura?"))
peso=float(input("Qual o seu peso?"))

imc = peso / (altura*altura)
print(f"O valor do IMC é {imc}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc >=18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >=25.0 and imc <= 29.9:
    print("Sobrepeso")
elif imc >=30.0 and imc <= 34.9:
    print("Obesidade grau 1")
elif imc >=35.0 and imc <= 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3 (obesidade mórbida)")

