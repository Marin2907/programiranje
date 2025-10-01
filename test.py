#Rjecnik (dictionary)
kosarica = {}

print(f"Prazna kosarica: {kosarica}")
print(f"Tip: {typa(kosarica)}")

#dodavanje elementa u rjecnik
kosarica['jabuka'] = 15
kosarica['kreke'] = 23
kosarica['mandarine'] = 3

#ispis rjecnika
print(f"Napunjena kosarica:{kosarica}")

kosarica['jabuka']=kosarica['jabuka']+5
print(f"Azuriraj kosarica:{kosarica}")

broj_mandarina = kosarica['mandarine']
print(f"Broj mandarina:{broj:mandarina}")

try:
    broj_krusaka = kosarica['kruska']
    print(f"Broj krusaka: {broj_krusaka}")
    except Exeption 
