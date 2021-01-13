import random
import math


def scale_factor(final_value, initial_value, max_iter, it):
    return initial_value + ((final_value - initial_value) / max_iter * (max_iter - it))


class Particle(object):
    def __init__(self, x0, dimension):
        self.position = []
        self.speed = []
        self.best_position = []
        self.best_value = math.inf
        self.value = math.inf
        self.dimension = dimension

        for i in range(0, dimension):
            if i % 2 == 0:
                self.speed.append(-1 * random.random())
            else:
                self.speed.append(random.random())
            self.position.append(x0[i][0])

    def enumerate(self, func):
        self.value = func(self.position)
        if self.value < self.best_value:
            self.best_value = self.value
            self.best_position = self.position

    def change_position(self):
        for i in range(0, self.dimension):
            self.position[i] = self.position[i] + self.speed[i]

    def new_speed(self, global_best, it, max_iter, option):
        cp = scale_factor(option.cp_final, option.cp_init, max_iter, it)
        w = scale_factor(option.w_final, option.w_init, max_iter, it)
        cg = scale_factor(option.cg_final, option.cg_init, max_iter, it)
        for i in range(0, self.dimension):
            rp = random.random()
            rg = random.random()
            self.speed[i] = w * self.speed[i] + rp * cp * (self.best_position[i] - self.position[i]) + rg * cg * (global_best[i] - self.position[i])

