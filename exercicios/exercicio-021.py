frase = "A minha prima falou com o António".upper()

A = frase.count('A')
print(f"O A aparece {A} vezes.")

primeira_posicao = frase.find('A')
print(f"Aparece pela primeira vez na posição {primeira_posicao + 1}.")

ultima_posicao = frase.rfind('A')
print(f"Aparece pela última vez na posição {ultima_posicao + 1}.")