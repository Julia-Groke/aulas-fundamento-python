import time
print("---Boas vindas!---")
time.sleep(1)
print("Faça o seu registro!")
username_in=input("Username:").strip()

email_in=input("Email:").strip()
if email_in.count("@")==0 and email_in.count(".")==0:
    print("Email inválido, insira novamente" )
    email_in = input("Email:").strip()

password_in=input("Password:").strip()
if username_in == password_in:
    print("Password inválida, igual ao username, insira novamente")
    password_in = input("Password:").strip()

time.sleep(0.5)
print("Criando o seu perfil")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print("Registro efetuado com sucesso, vamos reencaminhar para o login")

print("---MENU---")
print("[1]-Login")
print("[2]-Sair")
opcao= input("-->").strip().lower()

if opcao == "login" or opcao == "1":
    username = input("Username: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    if username == username_in and email == email_in and password == password_in:
        print("Login efetuado com sucesso!")
    else:
        print("Username, password ou email errado, tente novamente")
        username = input("Username: ").strip()
        email = input("Email: ").strip()
        password = input("Password: ").strip()

        if username == username_in and email == email_in and password == password_in:
            print("Login efetuado com sucesso!")
        else:
            print("Username, password ou email errado novamente, conta bloqueada")

elif opcao == "sair" or opcao == "2":
    print("Obrigado por utilizar o nosso programa, tenha um bom dia")
else:
    print("Opção invalida")


