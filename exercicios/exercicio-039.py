maior_idade=0
menor_idade=0


for c in range(0,7):
    idade=int(input(f"Qual a idade da {c+1}ª pessoa? "))
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print(f"{maior_idade} pessoas são maiores de idade e {menor_idade} pessoas são menores de idade")


#from datetime import datetime
# maior_idade=0
# menor_idade=0
# ano_atual = datetime.now().year
#for c in range(0,7):
    # ano_nascimento=int(input(f"Digite o ano de nascimento da {c+1}ª pessoa"))
    #idade = ano_atual - ano_nascimento
    #if idade >= 18:
         #maior_idade += 1
    #else:
        #menor_idade += 1
#print(f"{maior_idade} pessoas são maiores de idade e {menor_idade} pessoas são menores de idade")