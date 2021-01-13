import ann_criterion as crit
import time
from options import Options
from pso import PSO


if __name__ == '__main__':
    opt = Options()
    for i in range(10):
        print("Test number " + str(i + 1))
        pso = PSO(crit.optimality_criterion, 30, 100, 60, opt)
        print('Optimal point:')
        print(pso.best_position)
        print('Optimal value:')
        print(pso.best_value)
        print("\n\n")
