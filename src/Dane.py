import src.Exceptions as Exceptions
import json
import src.komunikaty.DanePL as DK


class Plik:
    def __int__(self, nazwaPliku):
        if len(nazwaPliku) == 0:
            raise Exceptions.zaKrotkiString()
        self.nazwaPliku = nazwaPliku

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
            wejscie = json.loads(wejscie)
        except json.JSONDecodeError as ex:
            print(ex)
            exit(2138)

    def zapiszSurowo(self, wartosc):
        if (not wartosc is str) or len(wartosc) == 0:
            raise Exceptions.zaKrotkiString
        with open(self.nazwaPliku) as p:
            p.write(wartosc)
        return True

    def zapiszJson(self, strukturaDanych):
        s = json.dumps(strukturaDanych)
        self.zapiszSurowo(s)

    def getNazwaPliku(self):
        return self.nazwaPliku


class BazaDanych1_0Exception(Exception):
    def __init__(self, msg=None):
        if msg is None:
            self.msg = DK.BazaDanychExceptionKomunikat
        else:
            self.msg = msg
    def __str__(self):
        return self.msg


class BazaDanych1_0():
    def __init__(self):
        self.magazyn = dict()

    def setMagazyn(self, strukturaDanych):
        if not strukturaDanych is dict:
            raise None


