from world import World
from Grain import Grain
import random


def run(case):
    if case == 1:
        # Balls horizontally collide
        balls = [Grain([90, 2], [0, 0], 2, 0.85, [50, 0, 150]),
                 Grain([100, 2], [-5, 0], 2, 0.85, [50, 0, 150])]
    elif case == 2:
        # Energy increasing demo
        balls = [Grain([100, 100], [0, 0], 2, 1.0, [70, 0, 130])]
    elif case == 3:
        # Particles being poured on the ground
        balls = []
        for i in range(100):
            balls.append(
                Grain([random.randint(95, 105), (200 + 11 * i)], [0, 0], 2, 0.2, [0, 10, 200]))
    elif case == 4:
        # Particles being poured into a container
        balls = []
        for i in range(100):
            balls.append(
                Grain([random.randint(95, 105), (200 + 11 * i)], [0, 0], 2, 0.2, [70, 20, 130]))
    elif case == 5:
        # Breaking dam demo
        balls = []
        for i in range(10):
            for j in range(10):
                balls.append(
                    Grain([i * 5, j * 5], [0, 0], 2, 0.5, [0, 0, 120])
                )

    world = World()
    for ball in balls:
        world.add_object(ball)
    world.animate()


run(5)
