#Faça um programa que leia 3 números e informe o maior número e o menor.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# maior = max(n1, n2, n3)
# menor = min(n1, n2, n3)
# print("O maior número é:", maior)
# print("O menor número é:", menor)

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n2 < n1  and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")