"""
broj = 10 # int (integer)
ime = "Pero" # string
znak = 'a' # float (decimalni broj)
cijena = 10.5 false # boolean (boolean)
istina = True # Bool (Boolean)

if broj > 5:
    print("Broj je veći od 5.")
elif broj == 5:
    print("Broj je jednak 5.")
else:
    print("Broj nije veći od 5.")

if istina:
    print("True.")
else:
    print("False.")
"""
#Zadatak 2
"""
print("Unesi temperaturu:")
temperatura = input()
"""
"""
temperatura = int(input("Unesi temperaturu:"))
if temperatura <= 0:
    print("ledenica")
elif temperatura > 0 and temperatura <= 15:
    print("hladno")
elif temperatura > 15 and temperatura <= 25:
    print("ugodno") 
else:
    print("vruće")
"""

#petlje 
"""
for i in range(10):
    print(i)

for slovo in "Bok":
    print(slovo)

brojac = 0
while brojac < 11:
    print(brojac)
    brojac += 1
"""
#Zadatak 3: Napišite program koji ispisuje sve parne brojeve od 1 do 20.
for broj in range(2,21):
    if broj % 2 == 0:
        print(broj)
    else:
        continue

    for broj in range(2,21,2):
        print(broj)
    else:
        continue

    broj = 2
    while broj <= 20:
        print(broj)
        broj += 2