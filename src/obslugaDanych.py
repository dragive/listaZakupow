import src.Exceptions as Exceptions
import json;
class Plik:
    def __int__(self,nazwaPliku):
        if len(nazwaPliku)==0 :
            raise Exceptions.zaKrotkiString();
        self.nazwaPliku=nazwaPliku
    def wczytajSurowo(self):
        try:
            with open(self.nazwaPliku) as p:
                return p.read()
        except Exception as e:
            print(e)
            exit(2137)
    def wczytajJson(self):
        wejscie = self.wczytajSurowo()
        try:
            wejscie=json.loads(wejscie)
        except json.JSONDecodeError as ex:
            print(ex)
            exit(2138)
    def zapiszSurowo(self,wartosc):
        if  ( not wartosc is str) or len (wartosc) == 0 :
            raise Exceptions.zaKrotkiString
        with open(self.nazwaPliku) as p:
            p.write(wartosc)
        return True
    def zapiszJson(self,strukturaDanych):
        s=json.dumps(strukturaDanych)
        self.zapiszSurowo(s)
    def getNazwaPliku(self):
        return self.nazwaPliku;