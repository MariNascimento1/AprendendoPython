# Faça um Programa que peça as 4 notas bimestrais e mostre a média

nota1 = float(input("Digite sua nota na primeira prova: "))
nota2 = float(input("Digite sua nota na segunda prova: "))
nota3 = float(input("Digite sua nota na terceira prova: "))
nota4 = float(input("Digite sua nota no projeto: "))

notafinal = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Sua média é: {notafinal}")

# --------------------------------------------------------------------------------------------------------------

nota1 = float(input("Digite sua nota na primeira prova: "))
nota2 = float(input("Digite sua nota na segunda prova: "))
nota3 = float(input("Digite sua nota na terceira prova: "))
nota4 = float(input("Digite sua nota no projeto: "))

notafinal = (nota1 + nota2 + nota3 + nota4) / 4

if notafinal >= 60:
    print(f"Sua média é: {notafinal}")
    print("Aprovado, Parabéns! Não fez mais que sua obrigação :)")
else:
    print(f"Sua média é: {notafinal}")
    print("Reprovado! faz de novo e faz direito Ò.Ó")
