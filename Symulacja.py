from PojemnikCieczy import PojemnikCieczy
from OgniwoPeltiera import OgniwoPeltiera


class Symulacja:
    def __init__(self, temp_pocz):
        self.ogniwo = OgniwoPeltiera()
        self.pojemnik = PojemnikCieczy(temp_pocz)
        self.dane_t = []
        self.dane_dt = []
        self.dane_v = []
        self.dane_Qc = []
        self.Ti = 75
        self.Td = 100
        self.kp = 1

    def regulator(self, dt):
        r = self.kp*(dt + sum(self.dane_dt)/self.Ti + self.Td * (dt - self.dane_dt[-1]))
        r = r if abs(r) <= 16 else 16*r/abs(r)
        return r

    def run(self, czas, temperatura_docelowa):
        for i in range(czas):
            self.dane_t.append(self.pojemnik.temp)
            self.dane_dt.append(temperatura_docelowa - self.pojemnik.temp)

            v = self.regulator(temperatura_docelowa - self.pojemnik.temp)
            self.dane_v.append(v)

            Qc = self.ogniwo.Qc(self.ogniwo.dt(self.pojemnik.temp), v)
            self.dane_Qc.append(Qc)
            self.pojemnik += Qc


