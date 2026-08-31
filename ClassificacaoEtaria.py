# criança = 0 <= 11
# adolescente = 12 <= 18
# jovem = 19 <= 30
# adulto = 31 <= 60
# idoso = > 61 

idade = int(input("Digite sua idade:")) 
print ("    ") #para dá espaço
if (idade >= 0) and (idade <= 11): #limite de idade de 0 ate 11
    print ("Idade:", idade)
    print ("Classificação etária: Criança" )

elif (idade >= 12) and (idade <= 18): # elide = if + else (simplificar)
    print ("Idade:", idade)
    print ("Classificação etária: Adolescente" )

elif (idade >= 19) and (idade <= 30):
    print ("Idade:", idade)
    print ("Classificação etária: Jovem" )

elif (idade >= 31) and (idade <= 60):
    print ("Idade :", idade)
    print ("Classificação etária: Adulto")

elif (idade >=61):
    print ("Idade:", idade)
    print ("Classificação etária: Idoso")

elif (idade <= -1):
    print ("Ainda não nasceu")

