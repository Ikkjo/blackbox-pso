import numpy as np
import random as random


class Particle(object):
    def __init__(self, x0, num_dimensions, options):
        self.positions = []  # particle position
        self.velocities = []  # particle velocity
        self.position_bests = []  # best position individual
        self.fitness_best_i = -1  # best fitness individual
        self.fitness_i = -1  # fitness individual
        self.num_dimensions = num_dimensions

        # Initial positions and velocities
        for i in range(0, num_dimensions):
            self.velocities.append((np.random.rand() - 0.5) * 2 * options.vspaninit)
            self.positions.append(x0[i][0])

    # calculate current fitness and calculating new individually best values
    def evaluate(self, cost_func):
        self.fitness_i = cost_func(self.positions)
        # upadete individual best -> check to see if the current position is better than an individual best
        if self.fitness_i < self.fitness_best_i or self.fitness_best_i == -1:
            self.position_bests = self.positions
            self.fitness_best_i = self.fitness_i

    def calculate_pso_params(self, xmax, xmin, tmax, tmin, t):
        x = xmin + ((xmax - xmin) / (tmax - tmin)) * (tmax - t)
        return x

    # update new particle velocity
    def update_velocity(self, pos_best_g, maxiter, iter, opt):

        # Calculating PSO parameters
        w = self.calculate_pso_params(opt.w_final, opt.w_init, maxiter, 0, iter)
        cp = self.calculate_pso_params(opt.cp_final, opt.cp_init, maxiter, 0, iter)
        cg = self.calculate_pso_params(opt.cg_final, opt.cg_init, maxiter, 0, iter)

        for i in range(0, self.num_dimensions):
            rp = random.random()
            rg = random.random()
            # Calculating speeds
            vel_cognitive = cp * rp * (self.position_bests[i] - self.positions[i])
            vel_social = cg * rg * (pos_best_g[i] - self.positions[i])
            self.velocities[i] = w * self.velocities[i] + vel_cognitive + vel_social

    # update the particle position based off new velocity updates->moving particle
    def update_position(self):
        for i in range(0, self.num_dimensions):
            self.positions[i] = self.positions[i] + self.velocities[i]

            # adjust maximum position if necessary
        #   if self.positions[i]>bounds[i][1]:
        #      self.positions[i]=bounds[i][1]

        # adjust minimum position if neseccary
        #   if self.positions[i] < bounds[i][0]:
        #       self.positions[i]=bounds[i][0]
