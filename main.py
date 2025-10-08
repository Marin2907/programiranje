#funkcija za učitavanje teksta iz datoteke
def ucitaj_tekst(filepath):
    try:
        # kod za otvaranje datoteke ide ovdje
        with open(filepath, 'r', encoding='utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f"Greška: Datoteka na putanji '{filepath}' nije pronađena.")
        return None # Vratit ćemo 'ništa' ako datoteka ne postoji

# Funkcija pročišćavanje teksta
def ocisti_tekst(tekst):
     #kod za pročišćavanje teksta ide ovdje
    tekst = tekst.lower()
    
    interpunkcija=[`.`,`,`,`!`,`"`,`;`,`:`,"`",`(`,`)`]
    for znak in interpunkcija:
        tekst = tekst.replace(znak,``)
    lista_rijeci = tekst.split()
    return lista_rijeci

def broji_rijeci(lista_rijeci):
        #rječnik u koji ćemo spremiti svaku riječ i koliko se puta ta riječ ponovila
        brojac_riječi = {}
        for riječ in lista_rijeci:
            if riječ in brojac_riječi:
                brojac_riječi[riječ] += 1
            else:
                brojac_riječi[riječ] = 1
        return brojac_riječi


if __name__ == "__main__":
    filepath = "tekst.txt"
    print(f"učitavam tekst iz datoteke: {filepath}")
    ucitani_tekst = ucitaj_tekst(filepath)
    if ucitani_tekst:
       print("učitani tekst je:")
       print(ucitani_tekst)
    else:
       print("greška pri učitavanju datoteke.")

    ucitani_tekst = ocisti_tekst(ucitani_tekst)     

    if ucitani_tekst:
       print("ucitani tekst je:")
       print(ucitani_tekst)
       #brojanje riječi i ispis rječnika
       brojac_riječi = broji_rijeci(ucitani_tekst)
       print("brojac riječi je:")
       print(brojac_riječi)
    else:
       print("greška pri učitavanju teksta.")


