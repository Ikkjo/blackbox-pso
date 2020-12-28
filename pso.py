# Load basic numeric packages
import numpy as np
import random as random
import math as math


# This class defines default values of the options within the options structure.
class MyOptions(object):
    def __init__(self):
        self.npart = 30  # The number of particles.
        self.niter = 100  # The number of iterations.
        self.cbi = 2.5  # Initial value of the individual-best acceleration factor.
        self.cbf = 0.5  # Final value of the individual-best acceleration factor.
        self.cgi = 0.5  # Initial value of the global-best acceleration factor.
        self.cgf = 2.5  # Final value of the global-best acceleration factor.
        self.wi = 0.9  # Initial value of the inertia factor.
        self.wf = 0.4  # Final value of the inertia factor.
        self.vmax = math.inf  # Absolute speed limit. It is the primary speed limit.
        self.vmaxscale = float('nan')  # Relative speed limit. Used only if absolute limit is unspecified.
        self.vspaninit = 1  # The initial velocity span. Initial velocities are initialized
        self.initpopulation = float('nan')
        self.initoffset = 0  # Offset of the initial population.
        self.initspan = 1  # Span of the initial population.
        self.trustoffset = 0  # If set to 1 (true) and offset is vector, than the offset is
        # believed to be a good solution candidate, so it is included in
        # the initial swarm.


class Error(Exception):
    def __init__(self, message):
        self.message = message


class Particle(object):
    def __init__(self, x0, num_dimensions, options):
        self.position_i = []  # particle position
        self.velocity_i = []  # particle velocity
        self.pos_best_i = []  # best position individual
        self.fitness_best_i = -1  # best fitness individual
        self.fitness_i = -1  # fitness individual
        self.num_dimensions = num_dimensions

        # Initial positions and velocities
        for i in range(0, num_dimensions):
            self.velocity_i.append((np.random.rand() - 0.5) * 2 * options.vspaninit)
            self.position_i.append(x0[i][0])

    # calculate current fitness and calculating new individually best values
    def evaluate(self, costFunc):
        self.fitness_i = costFunc(self.position_i)
        # upadete individual best -> check to see if the current position is better than an individual best
        if self.fitness_i < self.fitness_best_i or self.fitness_best_i == -1:
            self.pos_best_i = self.position_i
            self.fitness_best_i = self.fitness_i

    def linrate(self, xmax, xmin, tmax, tmin, t):
        x = xmin + ((xmax - xmin) / (tmax - tmin)) * (tmax - t)
        return x

    # update new particle velocity
    def update_velocity(self, pos_best_g, maxiter, iter, opt):

        # Calculating PSO parameters
        w = self.linrate(opt.wf, opt.wi, maxiter, 0, iter)
        cp = self.linrate(opt.cbf, opt.cbi, maxiter, 0, iter)
        cg = self.linrate(opt.cgf, opt.cgi, maxiter, 0, iter)

        for i in range(0, self.num_dimensions):
            r1 = random.random()
            r2 = random.random()
            # Calculating speeds
            vel_cognitive = cp * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = cg * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitive + vel_social

    # update the particle position based off new velocity updates->moving particle
    def update_position(self):
        for i in range(0, self.num_dimensions):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]

            # adjust maximum position if necessary
        #   if self.position_i[i]>bounds[i][1]:
        #      self.position_i[i]=bounds[i][1]

        # adjust minimum position if neseccary
        #   if self.position_i[i] < bounds[i][0]:
        #       self.position_i[i]=bounds[i][0]


class PSO(object):
    def __init__(self, costFunc, num_dimensions, options):

        fitness_best_g = -1  # best fitness in population
        pos_best_g = []  # best position in population

        maxiter = options.niter
        num_particles = options.npart
        population = []
        if (~np.isnan(options.initpopulation)).all():
            b = np.shape(options.initpopulation)
            if np.size(b) == 1:
                pno = b[0]
                pdim = 1
            if (pno != options.npart) or (pdim != options.nvar):
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
                population[j].evaluate(costFunc)

                # Calculating new globally best values (globally)
                if population[j].fitness_i < fitness_best_g or fitness_best_g == -1:
                    pos_best_g = list(population[j].position_i)
                    fitness_best_g = float(population[j].fitness_i)

            # Population is moving-> cycle through population and update velocities and position
            for j in range(0, num_particles):
                population[j].update_velocity(pos_best_g, maxiter, i, options)
                population[j].update_position()
            i += 1

        # print final results
        print('Optimal point:')
        print(pos_best_g)
        print('Optimal value:')
        print(fitness_best_g)
