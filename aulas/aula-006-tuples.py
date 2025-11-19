"""estante="Playstation", "Xbox", "Gameboy", "Nintendo"

print(estante[0])"""


nomes=("Nádia","Julia","Alexandra","Telmo",
       "Victor","Rafael","Daniel", "Leticia",
       "Roman", "Pedro", "Francisca","Inês")

"""for c in range(0,len(nomes)):
    print(f"{c}--> {nomes[c]}")

for nome in nomes:
    print(nome)"""


for indice,nome in enumerate(nomes):
    print(f"No indice {indice} o valor é {nome}")


print(sorted(nomes))

print(type(nomes))