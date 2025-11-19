numero=int(input("Insira um número de 0 a 20 "))


numero_extenso=("zero","um", "dois","três", "quatro", "cinco",
                "seis", "sete","oito","nove", "dez","onze", "doze",
                "treze","quatorze" , "quinze","dezesseis","dezessete",
                "dezoito","dezenove", "vinte")

for indice,nome in enumerate(numero_extenso):
    if numero < 0 or numero > 20:
        print("Número inválido")
        numero = int(input("Insira um número de 0 a 20 "))



"""elif numero == indice:
        print(f"{numero}->{numero_extenso[numero]}")"""


print(numero_extenso[numero])#muito mais simples