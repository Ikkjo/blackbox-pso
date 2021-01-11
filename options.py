from math import inf


# This class defines default values of the options within the options structure.
class MyOptions(object):
    def __init__(self):
        self.num_particles = 30  # The number of particles.
        self.num_iters = 100  # The number of iterations.
        self.cp_init = 2.5  # Initial value of the individual-best acceleration factor.
        self.cp_final = 0.5  # Final value of the individual-best acceleration factor.
        self.cg_init = 0.5  # Initial value of the global-best acceleration factor.
        self.cg_final = 2.5  # Final value of the global-best acceleration factor.
        self.w_init = 0.9  # Initial value of the inertia factor.
        self.w_final = 0.4  # Final value of the inertia factor.
        self.vmax = inf  # Absolute speed limit. It is the primary speed limit.
        self.vmaxscale = float('nan')  # Relative speed limit. Used only if absolute limit is unspecified.
        self.vspaninit = 1  # The initial velocity span. Initial velocities are initialized
        self.initpopulation = float('nan')
        self.initoffset = 0  # Offset of the initial population.
        self.initspan = 1  # Span of the initial population.
        self.trustoffset = 0  # If set to 1 (true) and offset is vector, than the offset is
        # believed to be a good solution candidate, so it is included in
        # the initial swarm.
