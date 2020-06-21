import src.Exceptions as Exceptions
class Plik:
    def __int__(self,nazwaPliku):
        if(len(nazwaPliku)==0):
            raise Exceptions.zaKrotkiString();
        self.nazwaPliku=nazwaPliku
