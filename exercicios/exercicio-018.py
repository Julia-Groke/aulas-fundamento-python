custo_dia = 60
custo_km = 0.45

km_percorridos = float(input("Digite quandos kms percorreu.\n--> "))
dias = int(input("Digite quantos dias teve o carro.\n--> "))

total = custo_dia * dias + custo_km * km_percorridos



print('Total a pagar:', float(total), '€.')