# Solicitando a entrada do usuário para três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Usando a instrução match para determinar o maior e o menor número
match num1, num2, num3:
    case num1, num2, num3 if num1 >= num2 and num1 >= num3:
        maior_numero = num1
        menor_numero = num2 if num2 < num3 else num3
    case num1, num2, num3 if num2 >= num1 and num2 >= num3:
        maior_numero = num2
        menor_numero = num1 if num1 < num3 else num3
    case num1, num2, num3 if num3 >= num1 and num3 >= num2:
        maior_numero = num3
        menor_numero = num1 if num1 < num2 else num2
    case _:
        print("Erro ao determinar o maior e o menor número.")
        maior_numero = None
        menor_numero = None

# Imprimindo o maior e o menor número
if maior_numero is not None and menor_numero is not None:
    print("O maior número é:", maior_numero)
    print("O menor número é:", menor_numero)
else:
    print("Não foi possível determinar o maior e o menor número.")