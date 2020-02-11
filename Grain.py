import matplotlib.animation as animation
import matplotlib.pyplot as plt

from Vector2D import Vector2D

acceleration = -9.81  # m/s/s
deltaT = 0.1  # s

class Grain:
    def __init__(self, position, velocity, radius, elasticity, wallboundaries):
        # Initialize all variables
        self.pos = Vector2D(position)
        self.velocity = Vector2D(velocity)
        self.elasticity = elasticity
        self.radius = radius
        self.mass = 1
        self.wallboundary = wallboundaries


    def __str__(self):
        kinetic = 0.5 * self.mass * self.velocity.dot_product(self.velocity)
        potential = -self.mass * acceleration * self.pos[1]
        total = kinetic + potential
        return "Position: " + str(self.pos) + \
               ", Velocity: " + str(self.velocity) + \
               ", Total Energy: " + str(total)
        # ", Kinetic Energy: " + str(kinetic) + \
        # ", Potential Energy: " + str(potential) + \
        # ", Total Energy: " + str(total)

    def pair_collision1(self, other):
        # dP = P1 - P0, displacement from this particle to the other
        dP = other.pos - self.pos
        norm = dP.norm() + 0.01

        if dP.norm() < self.radius + other.radius:
            # two particle collided when there distance is less than
            # the sum of their radius, Calculate new velocity for them.
            # unit vector along the direction P0 -> P1
            normalized = dP * (1 / norm)

            # Projection and rejection of V0 on D
            v0_proj = self.velocity.projection(normalized)
            v0_rej = self.velocity.rejection(normalized)

            # Project and rejection of V1 on D
            v1_proj = other.velocity.projection(normalized)
            v1_rej = other.velocity.rejection(normalized)

            # particles keep their v_rej and exchange their v_proj
            self.velocity = v0_rej + v1_proj * self.elasticity
            other.velocity = v1_rej + v0_proj * self.elasticity

            # move particles back so they don't overlap
            overlap = 0.5 * (self.radius + other.radius - norm)
            self.pos = self.pos - normalized * overlap
            other.pos = other.pos + normalized * overlap

    def euler_step(self):
        self.pos = self.pos + self.velocity * deltaT
        self.velocity[1] = self.velocity[1] + acceleration * deltaT

    def wall_collision(self):
        if self.pos[0] < self.wallboundary[0] + self.radius:
            # hit left wall
            self.pos[0] = self.wallboundary[0] + self.radius
            self.velocity[0] = -self.elasticity * self.velocity[0]
        if self.pos[1] < self.wallboundary[1] + self.radius:
            # hit bottom
            self.pos[1] = self.wallboundary[1] + self.radius
            self.velocity[1] = -self.elasticity * self.velocity[1]
        if self.pos[0] > self.wallboundary[2] - self.radius:
            # hit right wall
            self.pos[0] = self.wallboundary[2] - self.radius
            self.velocity[0] = -self.elasticity * self.velocity[0]