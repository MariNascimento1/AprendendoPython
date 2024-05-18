senha_correta = "123456"

tentativas = [3]

for tentativa in tentativas:
    senha_digitada = input("Digite sua senha: ")

    if senha_digitada == senha_correta:
        print("Bem-vindo.")
        break  
    else:
        tentativa -= 1
        print(f"Senha incorreta. Você tem {tentativa} tentativas até o bloqueio.")

if tentativa == 0:
    print("O telefone foi bloqueado após 3 tentativas de senha incorreta.")
