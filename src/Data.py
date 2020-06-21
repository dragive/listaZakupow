class Data:

    def __init__(self,dzien,miesiac,rok):
        self.dzien=dzien
        self.miesiac=miesiac
        self.rok=rok
    def nrDniaTygodniaZDaty(self):
        dzien = self.dzien
        miesiac = self.miesiac
        rok=self.rok
        C=rok//100
        Y=rok%100
        if(miesiac==1 or miesiac ==2):
                miesiac-=1
        return (dzien+( int ((2.6*(((miesiac-3+12)%12)+1))-0.2) ) -2*C+Y+ Y/4 + C/4+6)%7+1


