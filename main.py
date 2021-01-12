import ann_criterion as crit
import time
from options import Options
from pso import PSO


if __name__ == '__main__':
    opt = Options()
    for i in range(1):
        print("Test number " + str(i + 1))
        t = time.time()
        pso = PSO(crit.optimality_criterion, 100, 300, 60, opt)
        print(time.time() - t)
        print("\n\n")
        print('Optimal point:')
        print(pso.best_position)
        print('Optimal value:')
        print(pso.best_value)