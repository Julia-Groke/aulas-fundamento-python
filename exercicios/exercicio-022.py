
nome = input("Insira o seu nome:  ").strip().lower()
print(f"Olá {nome.title()}, o seu registo está completo.")


p_nome = nome[0]
indice_espaco = nome.find(" ") + 1
u_nome = nome[indice_espaco:]

email = f"{p_nome}.{u_nome}@empresa.pt"
print(f"O seu email é {email}")
