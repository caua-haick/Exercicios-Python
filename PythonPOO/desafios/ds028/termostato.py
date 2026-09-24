class Termostato():
    def __init__(self):
        self.__temperatura = 24
        self.ftemperatura= f'{self.__temperatura}ºC'
    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,temp ):
        if temp <16:
            self.__temperatura = 16
        elif temp>30:
            self.__temperatura = 30
        else:
            if temp%0.5==0:
                self.__temperatura = temp
            else:
                temp = int(temp)
                self.__temperatura = temp
        self.ftemperatura = f'{self.__temperatura}ºC'
