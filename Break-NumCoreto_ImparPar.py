# (num >= 0) and (num <= 25) 
num = float(input("Digite um número entre 0 e 25:"))
while (num <= -1) or (num >= 26) :  # while {condiçao} :
        print ("Erro!!")
        print ("........................................")
        print ("    ")
        print ("TENTE NOVAMENTE")
        num = float(input("Digite um número entre 0 e 25:")) # {código}
        break # para parar a execução do loop

if (num >= 0) and (num <= 25):
    if num %2 == 0:
            print ("Seu número é :", num, "e ele é par")
    
    else:
        print ("Seu número é :", num, "e ele é ímpar")
   

    #com o break o loop repete apenas uma vez(1 chance)