minha_lista = ['Maçã', 'Manga' , 'Melão']
elemento0 = minha_lista[0]
elemento1 = minha_lista[1]
elemento2 = minha_lista[2]
tentativas = 0


print("*****Jogo de adivinhação de nomes de frutas*****")
resposta = str(input("Frutas que começam com letra M:"))

if (resposta ==elemento0) or (resposta == elemento1) or (resposta == elemento2):
    print("Parabéns! Você acertou!")

else:
    print("Você errou.")
    n = str(input("Tente de novo:"))
pass
