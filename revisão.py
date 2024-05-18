idade = int(input("Quantos anos você tem? "))

if idade < 12:
    print("Você é uma criança")
elif 12 <= idade <= 17:
    print("Você é um Adolescente")
elif 18 <= idade <= 59:
     print("Você vai sofre para aposentar, ou seja, você é um Adulto") 
else:
    print("Você logo mais vai morrer, ou seja, você é um Idoso")