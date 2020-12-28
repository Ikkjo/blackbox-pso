import ann_criterion as crit
import pso

if __name__ == '__main__':
    opt = pso.MyOptions()
    opt.npart = 100
    opt.niter = 1000
    pso.PSO(crit.optimality_criterion, 60, opt)