class Hirsipuu:
    def __init__(self, sana: str):
        self.__sana = sana
        self.__arvauksia = 6

    # korvaa arvaamattomat kirjaimet viivoilla
    def sana_piilotus(self, sana: str, arvatut: list):
        piilotettu = ""
        for kirjain in sana:
            if kirjain in arvatut:
                piilotettu += kirjain
            else:
                piilotettu += "_"
        return piilotettu
    
    #Funktio joka piirtää hirsiukon arvausten määrän mukaan
    def piirra_ukko(self, arvaukset):
        if arvaukset == 0:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif arvaukset == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif arvaukset == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
        elif arvaukset == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif arvaukset == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif arvaukset == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")
        else:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|             ")
    
    # arvaa kirjaimia kunnes sana on arvattu tai arvaukset loppuvat
    def pelaa(self):
        arvaukset = 0
        kirjaimet = "abcdefghijklmnopqrstuvwxyzåäö"
        arvatut = []

        print("Syötä kirjaimia kunnes sana on arvattu, 0 lopettaa")
        while True:
            print(f"Arvauksia jäljellä: {self.__arvauksia}")
            print(self.sana_piilotus(self.__sana, arvatut))
            print("")
            arvaus = input("Syötä kirjain: ").lower()
            if arvaus == "0":
                break
            if len(arvaus) != 1 or arvaus not in kirjaimet:   # jos ei ole kirjain, arvaa uudestaan
                print("Ei ole kirjain")
                continue
            if arvaus in arvatut:   # jos kirjain on jo arvattu, arvaa uudestaan
                print("Arvattu jo")
                continue
            arvatut.append(arvaus)   # lisätään kirjain jo arvattuihin
            if arvaus in self.__sana:   # löytyykö kirjain arvattavasta sanasta
                print("Löytyy!")
                if self.sana_piilotus(self.__sana, arvatut) == self.__sana:
                    print(":)")   # voitto
                    break
            else:
                print("Ei löydy")
                self.__arvauksia -= 1
                arvaukset += 1
                self.piirra_ukko(arvaukset)
                if self.__arvauksia == 0:
                    print(":(")   # häviö
                    break


