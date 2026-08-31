num = float(input("Digite de 0 a 100:"))
if (num >= 0) and (num <= 100):
    if num % 2 != 0:
        print(num, "é ímpar.")
    else:
        print(num, " é par")
   
else:
    while (num < 0) or (num > 100):
        print("Erro!",num,"não está no intervalo de 0 a 100")
        num = float(input("Digite um número entre 0 e 100:"))
        if num % 2 != 0:
            print(num, "é ímpar.")
    else:
        print(num, " é par")
        pass
