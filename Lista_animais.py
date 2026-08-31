lista_animais = ["patos", "girafa", "cachorro", "papagaio"]


lista_animais.append('onça')
lista_animais.append('macaco')
lista_animais.append('pavão')
lista_animais.remove("patos")
#lista_animais = [2:]
# for x in lista_animais
sub_lista = lista_animais[::2]
for x in sub_lista:
    print (x, len(x))

