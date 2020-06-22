from src.komunikaty import menuGlownePL as menuGlowne
from src.komunikaty import interfaceTekstowyPL as interfaceTekstowy
import src.Dane;
def wczytanieInta():
    ok = True
    while(True):
        ok=True
        print(end=interfaceTekstowy.pobranieIntakomunikat)
        i=input()
        try:
            i=int(i)
        except Exception as e:
            ok=False
        if ok == True:
            break
    return i

class interface:
    def __init__(self):
        self.menuGlowne()
        self.db={}
        self.wczytajDane()
        self.plik= src.Plik("data.txt")
    def menuGlowne(self):
        print(menuGlowne.menuGlowneKomunikat)
    def wczytajDane(self):
        try:
            self.db=self.plik.wczytajJson()
        except Exception as ex:
            print(ex)
            exit(2139)

'''
version: 1.0
listy_zakupów:
    Lista sporzywacza:
        kto co kupił gdziek keidy za ile
    Lista paliwowa:
        ----||----
settings:
    wartość_defaultowa_kto_kupuje: 
    wartość_defaultowa_kiedy_kupuje: 
    ostatnio_edytowana_lista: 
    szerokosc_podstawowa: 
'''