from random import randint
from sanat import Sanalista
from hangman import Hirsipuu

class Main:
    def suorita(self):
        while True:
            print("1: Pelaa")
            print("2: Lisää sana")
            print("3: Poistu")
            syote = input("Valitse toiminto: ")
            if syote == "1":
                sanat = Sanalista.hae_sanalista()
                luku = randint(0, len(sanat)-1)
                sana = sanat[luku]
                peli = Hirsipuu(sana)
                peli.pelaa()
            elif syote == "2":
                Sanalista.lisaa_sana()
            elif syote == "3":
                break


main = Main()
main.suorita()