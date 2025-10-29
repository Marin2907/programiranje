"""
prvi_element = moja_lista[0]

print (prvi_element)

moja_lista.append(40)

print (moja_lista)

dio_liste = moja_lista[1;3]

print (dio_liste)
"""
"""
#Zadatak 1:

voce = ["jabuka","banana","kruska"]
prvi_element = voce[0]
print(prvi_element)
voce.append("naranca")
print(voce)
"""

#2D liste
ormar = [
    ['majica','kapa','sal'],  #0. redak (polica)
    ['hlace','carape','remen'], #1. redak
    ['jakna','cipele','cizme'], #2. redak
]
"""
print ( ormar[1][0])
print (ormar[1][1])
print (ormar[2][1])
"""

"""for odjeca in ormar:

    print(odjeca[1])

for redak in ormar:
    print(f"Sadržaj retka:{redak}")

    for element in redak:
        print (f"Element: {element}")"""

def pronadji_broj (lista,broj):
    print(f"Tražim broj {broj} u listi {lista}")
    prekidac = False

    for element in lista:
        if element == trazeni_broj:
            prekidac = True
            break
        else:
            prekidac = False

    if prekidac:
        print (f"Broj {trazeni_broj} je na listi")
    else:
        print (f"Broj {trazeni_broj} nije na listi")


lista = [10, 20, 30, 40, 50]
trazeni_broj = 30
pronadji_broj (lista, trazeni_broj)
