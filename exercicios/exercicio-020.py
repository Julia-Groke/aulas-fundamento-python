
nome = input("Digite o seu nome: ").strip()

print(f"Nome com todas as letras maiúsculas: {nome.upper()}")
print(f"Nome com todas as letras minúsculas: {nome.lower()}")
espacos = nome.count(' ')
print(f"Quantidade de letras sem espaços: {len(nome) - espacos}")
primeiro_espaco = nome.find(' ')
primeiro_nome=(nome[:primeiro_espaco])
print(f"Quantidade de letras do primeiro nome: {len(primeiro_nome)}")