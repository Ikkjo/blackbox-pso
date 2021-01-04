import ann_criterion as crit
import pso
import time

if __name__ == '__main__':
    opt = pso.MyOptions()
    for i in range(1):
        print("Test number " + str(i + 1))
        t = time.time()
        pso.PSO(crit.optimality_criterion, 60, opt)
        print(time.time() - t)
        print("\n\n")
