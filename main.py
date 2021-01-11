import ann_criterion as crit
import time
from options import MyOptions
from pso import PSO


if __name__ == '__main__':
    opt = MyOptions()
    for i in range(1):
        print("Test number " + str(i + 1))
        t = time.time()
        PSO(crit.optimality_criterion, 60, opt)
        print(time.time() - t)
        print("\n\n")
