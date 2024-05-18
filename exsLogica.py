#1. Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n2 > n1:
    print(f"{n2} é maior que {n1}")
else:
    print("Os números são iguais")

#2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = float(input("Digite um número: "))

if n1 > 0:
    print("Esse número é positivo")
elif n1 == 0:
    print("É zero")
else:
    print("Esse número é negativo")

#3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
#F - Feminino,
#M - Masculino,
#Outra letra qualquer - Sexo Inválido.

letra = input("Digite uma letra (F para Femino, M para masculino): ")

if letra  == "F":
    print("Feminino")
elif letra == "M":
    print("Masculino")
else:
    print("Sexo inválido")

#4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra in ('aeiouAEIOU'):
    print("Vogal.")
elif letra.isnumeric():
    print("Número.")
else:
    print("Consoante.")

#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota = float(input("Insira sua nota: "))
nota2 = float(input("Insira sua segunda nota: "))

media = (nota + nota2)/2

if media < 6:
    print("Reprovado.")
    print(f"Sua nota foi: {media}.")
elif media == 10:
    print("Aprovado com Distinção. Parabéns!!")
    print(f"Sua nota foi: {media}.")
else:
    print("Aprovado.")
    print(f"Sua nota foi: {media}.")

#Faça um Programa que leia três números e mostre o maior deles.

num = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

match num, num2, num3:
  case num, num2, num3 if num > num2 and num > num3:
      print(f"O maior número é o primeiro número: {num}")
  case num, num2, num3 if num2 > num and num2 > num3:
      print(f"O maior número é o segundo número: {num2}")
  case num, num2, num3 if num3 > num and num3 > num2:
      print(f"O maior número é o terceiro número: {num3}")
  case _:
       print("Erro ao determinar o maior número.")

#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

match num1, num2, num3:
   case num1, num2, num3 if num1 >= num2 and num1 >= num3:
       maior = num1
       menor = num2 if num2 < num3 else num3
   case num1, num2, num3 if num2 >= num1 and num2 >= num3:
       maior = num2
       menor = num1 if num1 < num3 else num3
   case num1, num2, num3 if num3 >= num1 and num3 >= num2:
       maior = num3
       menor = num1 if num1 < num2 else num2
   case _:
       print("Erro ao determinar o maior e o menor número.")
       maior = None
       menor = None
    
if maior is not None and menor is not None:
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
else:
    print("Merda, deu ruim! Tente novamente.")



