from matplotlib import pyplot as pl
from matplotlib import gridspec as gs

from Symulacja import Symulacja


if __name__ == "__main__":
    time = 5000

    s = Symulacja(30)
    t_zadane = 0
    run = s.run(time, t_zadane)
    fig = pl.figure(figsize=(16,9))

    grid = gs.GridSpec(2, 2)
    ax = fig.add_subplot(grid[0, 0])
    bx = fig.add_subplot(grid[1, 0])
    cx = fig.add_subplot(grid[1, 1])
    dx = fig.add_subplot(grid[0, 1])

    ax.plot(range(time), s.dane_t, 'r')
    ax.set_title("Zmiana temperatury w czasie, T zadane: " + str(t_zadane) + "st C")
    ax.set_ylabel("Temperatura [C]")
    ax.set_xlabel("Czas[s]")

    bx.plot(range(time), s.dane_Qc, 'b')
    bx.set_title("Chwilowa moc cieplna ogniwa")
    bx.set_ylabel("Moc[W]")
    bx.set_xlabel("Czas[s]")

    cx.plot(range(time), s.dane_dt, 'g')
    cx.set_title("Chwilowy uchyb regulacji w czasie")
    cx.set_ylabel("dt [C]")
    cx.set_xlabel("Czas[s]")

    dx.plot(range(time), s.dane_v, 'g')
    dx.set_title("Napięcie na ogniwie w czasie")
    dx.set_ylabel("Napięcie [V]")
    dx.set_xlabel("Czas[s]")

    fig.tight_layout()
    pl.show()
