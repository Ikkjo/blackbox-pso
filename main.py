import ann_criterion as crit
import pso

if __name__ == '__main__':
    opt = pso.MyOptions()
    opt.npart = 100
    opt.niter = 1000
    for i in range(1):
        print("Test number " + str(i + 1))
        pso.PSO(crit.optimality_criterion, 60, opt)
        print("\n\n")
