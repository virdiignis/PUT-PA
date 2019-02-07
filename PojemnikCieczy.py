class PojemnikCieczy:
    cieplowlasciwe = 4190 #J/(kg*K)

    def __init__(self, temp, masa=0.5):
        self.masa = masa  # dla wody w uproszczeniu 1l=1kg
        self.temp = temp

    def __iadd__(self, cieplo):
        self.temp += cieplo/(PojemnikCieczy.cieplowlasciwe * self.masa)
        return self

    def __isub__(self, cieplo):
        self.temp -= cieplo/(PojemnikCieczy.cieplowlasciwe * self.masa)
        return self


