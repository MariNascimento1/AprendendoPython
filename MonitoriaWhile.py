import random

senha_correta = random.randint(1, 20)
#senha_correta = "123456"

tentativas = 3

while tentativas > 0:
    senha_digitada = input("Digite a senha: ")
    
    if senha_digitada == senha_correta:
        print("Bem-vindo.")
        break  
    else:
        tentativas -= 1
        print(f"Senha incorreta. Você tem {tentativas} tentativas até o bloqueio.")
        
if tentativas == 0:
    print(senha_correta)
    print(f"O telefone foi bloqueado após 3 tentativas de senha incorreta.")
