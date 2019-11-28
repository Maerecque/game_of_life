from Visualisation import *
from Simulator import *
import time

# Configuratie
VISUALISATION=True

if __name__ == "__main__":
    w = World(110)
    age = 6
    sim = Simulator(w,age)

    midX = w.width // 2
    midY = w.height // 2

    w.set(midX, midY, age)
    w.set(midX - 1, midY, age)
    w.set(midX + 1, midY, age)

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)