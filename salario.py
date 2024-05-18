#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês,sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
#5% para o sindicato, faça um programa que nos dê:
#Salário bruto
#Quanto pagou ao INSS.
#Quanto pagou ao sindicato.
#O salário líquido.
#Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#Salário Bruto : R$
#IR (11%) : R$
#INSS (8%) : R$
#Sindicato ( 5%) : R$
#Salário Liquido : R$

valor_hora = float(input("Digite quanto você ganha por hora: "))
hora_trabalhadas = float(input("Digite quantas horas você trabalha no mês: "))

salario_bruto = valor_hora * hora_trabalhadas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sidicato = salario_bruto * 0.05

salario_liquido = salario_bruto - ir - inss - sidicato

print(f"Seu salário bruto é: {salario_bruto : .2f}")
print(f"Desconto do IR (11%): {ir :.2f}")
print(f"Desconto do INSS (8%): {inss :.2f}")
print(f"Desconto do Sidicato (5%): {sidicato}")
print(f"Seu salário liquido: R$ {salario_liquido :.2f}")


