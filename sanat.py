CHARS = ["ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖ"]

class Sanalista():
    def hae_sanalista():
        try:
            tiedosto = open("words.txt","r")
        except FileNotFoundError:
            print("Tiedostoa ei löytynyt..")
            SystemExit
        lista = []
        for rivi in tiedosto:
            lista.append(rivi.strip())
        return lista 
    
    def lisaa_sana():
        try:
            tiedosto = open("words.txt", "r+")
        except FileNotFoundError:
            print("Tiedostoa ei löytynyt..")
            SystemExit 
        lista = []
        for rivi in tiedosto:
            lista.append(rivi.strip())
        sana = input("Syötä sana: ")
        if sana in lista:
            print("Sana on jo listassa")
            return
        tiedosto.write("\n" + sana.lower())
        tiedosto.close()
        print("Sana lisätty!")