pares=0

for c in range(0,10):
    numeros = int(input(f"Digite o {c+1}º número"))
    if numeros % 2 == 0:
        pares += 1

print (f"Tem {pares} números pares")
