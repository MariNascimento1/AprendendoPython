nome = "Mariana"
idade = 22
profissao = "Programadora"
linguagem = "Python"
pessoa = {"nome": "Mariana", "idade": 22, "profissao": "Programadora", "linguagem": "Python"}

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculada no curso de %s." %
      (nome, idade, profissao, linguagem))

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculada no curso de {}." .format(
    nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculada no curso de {0}." .format(
    linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}." .format(
    nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa))


PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")

