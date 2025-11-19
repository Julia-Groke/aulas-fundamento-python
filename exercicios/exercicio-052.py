times=("Real Madrid","Barcelona","Villarreal","Real Betis",
       "Athletic Bilbao","Atlético de Madrid","Elche","Sevilla",
       "Espanyol","Alavés","Getafe","Osasuna","Levante","Rayo Vallecano",
       "Valencia","Celta de Vigo","Real Oviedo","Girona","Real Sociedad","Mallorca",)


print("Os primeiros 5 classificados:")
for indice, time in enumerate(times):
    if indice == 5:
        break
    else:
        print(f"\t{indice + 1}º-->{time}")
print("------------------------------------------")

print("Os últimos 4 classificados:")
TAM=len(times)
for indice, time in enumerate(times):
    if indice >= TAM -4:
        print(f"\t{indice + 1}º-->{time}")
    else:
        continue
print("------------------------------------------")

print(f"Lista dos times por ordem alfabetica:")
for time in sorted(times):
    print("\t",time)
print("------------------------------------------")

print("Posição da equipa Las Palmas:")
esta_la=False
indice_las_palmas=""
for indice, time in enumerate(times):
    if time == "Las Palmas":
        esta_la = True
        indice_las_palmas = indice
if indice_las_palmas == True:
    print(f"Las Palmas--> {indice_las_palmas + 1}º lugar")
else:
    print("Las Palmas não está classificado")
















