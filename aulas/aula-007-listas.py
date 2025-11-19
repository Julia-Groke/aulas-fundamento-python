"""from math import fsum

notas=list()

print(type(notas))

for c in range(0,5):
    nota=float(input(f"Insira a {c+1}ª nota "))
    notas.append(nota)

media= fsum(notas) / len(notas)

print(media)"""


"""nomes=["Nádia","Julia","Alexandra","Telmo",
       "Victor","Rafael","Daniel", "Leticia",
       "Roman", "Pedro", "Francisca","Inês"]

print(nomes)

nomes.append("João")
print(nomes)

nomes.insert(0,"Luanna")
print(nomes)"""


series=list()

print("Insere o seu top 5 de séries")
for c in range(0,5):
    serie=input("-->")
    series.append(serie)

print(series)

while True:
    print("1 - Inserir novo top 5")
    print("2 - Substituir serie")
    print("3 - Mostrar top 5")
    print("4 - Sair")
    opcao=int(input("-->"))


    match opcao:
        case 1:
            print("Insere o seu top 5 de séries")
            for c in range(0, 5):
                serie = input("-->")
                series.append(serie)

        case 2:
            nova_serie=input("Digite a nova série: ")
            serie_remover=input("Digite a série a remover: ")

            indice_serie_remover= series.index(serie_remover)

            series[indice_serie_remover] = nova_serie
            print("Série alterada com sucesso")

        case 3:
            for indice,serie in enumerate(series):
                print(f"{indice + 1}ª -> {serie}")

        case 4:
            print("A sair...")
            break

        case _:
            print("Opção inválida")

