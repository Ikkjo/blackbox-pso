import numpy as np
from particle import Particle
import math


def initiate_population(particle_num, dimension):
    population = []
    for i in range(particle_num):
        if i % 5 == 0:
            x0 = -1 * np.random.rand(dimension, 1)
        else:
            x0 = np.random.rand(dimension, 1)
        population.append(Particle(x0, dimension))
    return population


class PSO(object):
    def __init__(self, func, particle_num, max_iter, dimension, option):
        self.best_value = math.inf
        self.best_position = []
        population = initiate_population(particle_num, dimension)
        for i in range(max_iter):
            for j in range(particle_num):
                population[j].enumerate(func)
                if population[j].value < self.best_value:
                    self.best_position = population[j].position
                    self.best_value = population[j].value
            for j in range(particle_num):
                population[j].new_speed(self.best_position, i, max_iter, option)
                population[j].change_position()
