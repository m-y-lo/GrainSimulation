import random

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

    def animate(self):
        # Creates an animation
        # fig, ax = plt.subplots()
        fig = plt.figure()
        ax = plt.axes(xlim=(0, 200), ylim=(0, 200))
        patches = []
        for ball in self.objects:
            patches.append(Circle((ball.pos[0], ball.pos[1]), ball.radius))

        def init():
            for p in patches:
                ax.add_patch(p)
            return patches

        def run(frame):
            nparts = len(self.objects)
            for i in range(nparts):
                self.objects[i].euler_step()
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

        


if __name__ == '__main__':
    # balls = [Grain([0, 10], [100, 100], 10, 1),
    #          Grain([0, 10], [100, 150], 10, 1),
    #          Grain([10000, 10000], [100, 1000], 10000, 1),
    #          Grain([0, 500], [100, 700], 1, 1),
    #          Grain([0, 1000], [100, 1000], 1, 1)]
    # balls = [Grain([500, 500], [0, 0], 10, 1),
    #         Grain([600, 500], [0, 0], 20, 1)]

    # two ball horizontally bounce each other
    # balls = [Grain([90, 2], [0, 0], 2, 1),
    #         Grain([100, 2], [-5, 0], 2, 1)]

    # one ball bounce between walls
    # balls = [Grain([100, 10], [-5, 0], 10, 1)]

    # one ball free ball
    # balls = [Grain([100, 100], [0, 0], 2, 1)]

    # overlapping balls
    # balls = [Grain([100, 10], [0, 0], 10, 1),
    #          Grain([105, 10], [0, 0], 10, 1)]

    # balls of variant sizes poured into container
    # balls = []
    # for i in range(200):
    #     balls.append(
    #         Grain([random.randint(95, 105), (200 + 11 * i)], [0, 0], 2, 0.2, [70, 10, 130]))

    # balls = [Grain([100, 100], [0, 0], 2, 1.0, [70, 10, 130])]

    balls = []
    for i in range(15):
        for j in range(15):
            balls.append(
                Grain([i * 5 , j * 5], [0, 0], 2, 0.5, [0, 0, 120])
            )

    world = World()
    for ball in balls:
        world.add_object(ball)
    world.animate()
