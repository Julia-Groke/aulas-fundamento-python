while True:
    numero=int(input("Insira um número"))

    if numero <= 0:
        break


    for c in range(0,10):
        print(f"{numero} x {c+1} = {numero * (c+1)}")




