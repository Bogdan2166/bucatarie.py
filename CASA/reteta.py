from CASA.bucatarie import scoatem
from CASA.bucatarie import adaugam



class Bucatarie:
    def __init__(self):
        self.retete = {}

    def adauga_reteta(self, nume_reteta, ingrediente):
        self.retete[nume_reteta] = ingrediente

    def afiseaza_retete(self):
        print("Retete disponibile: ")
        for nume, ingrediente in self.retete.items():
            print(nume + ":")
            for ingredient, cantitate in ingrediente.items():
                print("- " + ingredient + "(" + str(cantitate) + ")")
