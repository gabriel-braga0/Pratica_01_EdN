idade = int(input("Digite sua idade: "))

if (idade >= 0 and idade <= 12):
    print("O usuário é Criança.")
elif (idade >= 0 and idade <= 17):
    print("O usuário é Adolescente.")
elif (idade >= 0 and idade <= 59):
    print("O usuário é Adulto.")
elif (idade >= 0 and idade >= 60):
    print("O usuário é Idoso.")
else:
    print("Idade inválida")
