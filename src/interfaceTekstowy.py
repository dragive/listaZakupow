from src.komunikaty import menuGlownePL as menuGlowne
from src.komunikaty import interfaceTekstowyPL as interfaceTekstowy
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
    def menuGlowne(self):
        print(menuGlowne.menuGlowneKomunikat)

