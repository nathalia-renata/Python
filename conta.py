nota1 = 50
nota2 = 10
nota3 = 1
divide = ''
divide1 = ''
divide2 = ''

valor = int(input("Digite o valor que você quer sacar:"))
input(nota1)
input(nota2)
input(nota3)
escolha = int(input("Escolha entre os três valores acima:"))
if escolha == 50 :
    divide = valor/50
    print("Você irá sacar ", divide , "notas")
elif escolha == 10 :
    divide1 = valor/10
    print("Você irá sacar ", divide1 , "notas")
elif escolha == 1 :
    divide2 = valor/1
    print("Você irá sacar ", divide2 , "notas")
pass
