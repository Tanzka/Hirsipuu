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
            tiedosto = open("words.txt", "a")
        except FileNotFoundError:
            print("Tiedostoa ei löytynyt..")
            SystemExit 
        sana = input("Syötä sana: ")
        tiedosto.write("\n"+sana.lower())
        tiedosto.close()
        print("Sana lisätty!")
    



        