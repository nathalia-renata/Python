minha_lista = ['Pera', 'Kiwi', 'Amora']
elemento = minha_lista[0]
elemento1 = minha_lista[1]
elemento2 = minha_lista[2]
print("         Jogo: Adivinhe a Fruta          ")
resposta = str(input("Fruta que começa com a letra P:"))
if (resposta != elemento):
    print("Você errou!!")

resposta = str(input("Fruta é verde e formato oval:"))
if (resposta != elemento1):
    print("Você errou!!")

resposta = str(input("O nome da fruta lembra 'amor'"))
if (resposta != elemento2):
    print("Você errou!!")


if (resposta == elemento) or (resposta == elemento1) or (resposta == elemento2):
    print(" Parabéns!! Você acertou as três frutas.")
    pass
else:
    print("Você não acertou as frutas. Iremos te dá mais uma chance.")
    print = ("Tente de novo:")
    resposta = str(input("Fruta que começa com a letra P:"))
if (resposta != elemento):
    print("Você errou!!")

resposta = str(input("Fruta é verde e formato oval:"))
if (resposta != elemento1):
    print("Você errou!!")

resposta = str(input("O nome da fruta lembra 'amor':"))
if (resposta != elemento2):
    print("Você errou!!")


if (resposta == elemento) or (resposta == elemento1) or (resposta == elemento2):
    print(" Parabéns!! Você acertou as três frutas.")

    pass
