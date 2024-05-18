#Peça a idade do usuário com base na idade fornecida, o programa deve classificar a pessoa em uma das seguintes categorias:
#Se a idade for menor que 12 anos, imprimir "Criança". Se a idade estiver entre 12 e 17 anos (inclusive), imprimir "Adolescente".
#Se a idade estiver entre 18 e 59 anos (inclusive), imprimir "Adulto". Se a idade for igual ou superior a 60 anos, imprimir "Idoso".

idade = int(input("Quantos anos você tem? "))

if idade < 12:
    print("Você é uma criança")
elif 12 <= idade <= 17:
    print("Você é um Adolescente")
elif 18 <= idade <= 59:
     print("Você vai sofrer para aposentar, ou seja, você é um Adulto") 
else:
    print("Você logo mais vai morrer, ou seja, você é um Idoso")






