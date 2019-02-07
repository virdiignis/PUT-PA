import numpy as np
from scipy.interpolate import lagrange


class OgniwoPeltiera:
    interpolation_dt = np.array((0, 10, 20, 30, 40, 50, 60))

    interpolation_data = {
        0:  lambda x: x,
        2:  lagrange(interpolation_dt, (33.15, 11.67, 0, 0, 0, 0, 0)),
        4:  lagrange(interpolation_dt, (61.53, 40.58, 20.42, 0, 0, 0, 0)),
        6:  lagrange(interpolation_dt, (85.67, 65.5, 44.5, 25, 3.72, 0, 0)),
        8:  lagrange(interpolation_dt, (105, 85.7, 65, 44.56, 25, 3.72, 0)),
        10: lagrange(interpolation_dt, (120.7, 100, 80.1, 60.5, 40.3, 20.15, 0)),
        12: lagrange(interpolation_dt, (131.3, 111.14, 91.5, 71.6, 51.2, 30.76, 10.6)),
        14: lagrange(interpolation_dt, (138, 118.5, 98.4, 78.5, 58.35, 37.66, 17.5)),
        16: lagrange(interpolation_dt, (139.8, 120.15, 100, 80.6, 60.74, 40, 19.62))
    }

    @staticmethod
    def Qc(dt, v):
        dt = dt if dt >= 0 else 0
        assert abs(v) <= 16, "Napięcie poza dopuszczalnymi granicami"
        sign = v/abs(v)
        v = abs(v)
        x = tuple(OgniwoPeltiera.interpolation_data.keys())
        y = [f(dt) for f in OgniwoPeltiera.interpolation_data.values()]
        f = lagrange(x, y)
        return sign * f(v)

    @staticmethod
    def dt(t):
        return 27-t
