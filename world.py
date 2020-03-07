import random

import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from Grain import Grain


class World:
    def __init__(self):
        self.objects = []

    def add_object(self, object):
        self.objects.append(object)

    def plot(self):
        x = 0
        for i in self.objects:
            x += 1
            i.plot("Ball" + str(x))

        plt.legend()
        plt.show()

    def animate(self, graph=True):
        # Creates an animation
        # fig, ax = plt.subplots()
        fig = plt.figure()
        ax = plt.axes(xlim=(0, 200), ylim=(0, 200))
        patches = []
        KE = []
        PE = []
        total = []

        for ball in self.objects:
            patches.append(Circle((ball.pos[0], ball.pos[1]), ball.radius))

        def init():
            for p in patches:
                ax.add_patch(p)
            return patches

        def run(frame):
            nparts = len(self.objects)
            for i in range(nparts):
                self.objects[i].exact_solution()
                KE.append(self.objects[i].kinetic())
                PE.append(self.objects[i].potential())
                total.append(self.objects[i].total_energy())
                for j in range(i + 1, nparts):
                    self.objects[i].pair_collision1(self.objects[j])
                self.objects[i].wall_collision()

                patches[i].center = (self.objects[i].pos[0],
                                     self.objects[i].pos[1])
                patches[i].radius = self.objects[i].radius

            return patches

        ani = animation.FuncAnimation(fig, run, frames=2000, blit=False,
                                      interval=30,
                                      repeat=False, init_func=init)
        plt.show()

        if graph == True:
            x = np.arange(0, len(total))
            fig, ax1 = plt.subplots()
            plt.xlabel("Time")
            plt.ylabel("Total Energy")
            ax1.plot(x, total)
            plt.show()

            x = np.arange(0, len(KE))
            fig, ax1 = plt.subplots()
            plt.xlabel("Time")
            plt.ylabel("Kinetic Energy")
            ax1.plot(x, KE)
            plt.show()

            x = np.arange(0, len(PE))
            fig, ax1 = plt.subplots()
            plt.xlabel("Time")
            plt.ylabel("Potential Energy")
            ax1.plot(x, PE)
            plt.show()


if __name__ == '__main__':
    # Balls horizontally collide
    balls = [Grain([90, 2], [0, 0], 2, 0.85, [50, 0, 150]),
            Grain([100, 2], [-5, 0], 2, 0.85, [50, 0, 150])]

    # Energy increasing demo
    # balls = [Grain([100, 100], [0, 0], 2, 1.0, [70, 0, 130])]

    # Particles being poured on the ground
    # balls = []
    # for i in range(100):
    #     balls.append(
    #         Grain([random.randint(95, 105), (200 + 11 * i)], [0, 0], 2, 0.2, [0, 10, 200]))

    # Particles being poured into a container
    # balls = []
    # for i in range(100):
    #     balls.append(
    #         Grain([random.randint(95, 105), (200 + 11 * i)], [0, 0], 2, 0.2, [70, 20, 130]))

    # Breaking dam demo
    # balls = []
    # for i in range(10):
    #     for j in range(10):
    #         balls.append(
    #             Grain([i * 5 , j * 5], [0, 0], 2, 0.5, [0, 0, 120])
    #         )

    world = World()
    for ball in balls:
        world.add_object(ball)
    world.animate()
