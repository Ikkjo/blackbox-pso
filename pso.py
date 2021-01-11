# Load basic numeric packages
from particle import Particle
import numpy as np


class Error(Exception):
    def __init__(self, message):
        self.message = message


class PSO(object):
    def __init__(self, cost_func, num_dimensions, options):

        fitness_best_global = -1  # best fitness in population
        best_positions_global = []  # best position in population

        maxiter = options.num_iters
        num_particles = options.num_particles
        population = []
        if (~np.isnan(options.initpopulation)).all():
            b = np.shape(options.initpopulation)
            if np.size(b) == 1:
                pno = b[0]
                pdim = 1
            if (pno != options.num_particles) or (pdim != options.nvar):
                raise Error("The format of initial population is inconsistent with desired population")
            population = options.initpopulation
        else:
            for i in range(0, num_particles):
                x0 = (np.random.rand(num_dimensions, 1) - 0.5) * 2 * options.initspan + options.initoffset
                population.append(Particle(x0, num_dimensions, options))

        #################################
        # The main loop  ###############
        #################################
        # Begin optimization loop
        i = 0
        while i < maxiter:
            # print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0, num_particles):
                population[j].evaluate(cost_func)

                # Calculating new globally best values (globally)
                if population[j].fitness_i < fitness_best_global or fitness_best_global == -1:
                    best_positions_global = list(population[j].positions)
                    fitness_best_global = float(population[j].fitness_i)

            # Population is moving-> cycle through population and update velocities and position
            for j in range(0, num_particles):
                population[j].update_velocity(best_positions_global, maxiter, i, options)
                population[j].update_position()
            i += 1

        # print final results
        print('Optimal point:')
        print(best_positions_global)
        print('Optimal value:')
        print(fitness_best_global)
