import numpy as np
from qpso import QDPSO


def sphere(args):
    f = sum([np.power(x, 2.) for x in args])
    return f


def log(s):
    best_value = [p.best_value for p in s.particles()]
    best_value_avg = np.mean(best_value)
    best_value_std = np.std(best_value)
    print("{0: >5}  {1: >9}  {2: >9}  {3: >9}".format("Iters.", "Best", "Best(Mean)", "Best(STD)"))
    print("{0: >5}  {1: >9.3E}  {2: >9.3E}  {3: >9.3E}".format(s.iters, s.gbest_value, best_value_avg, best_value_std))


NParticle = 40
MaxIters = 1000
NDim = 10
bounds = [(-2.56, 5.12) for i in range(0, NDim)]
g = 0.96
s = QDPSO(sphere, NParticle, NDim, bounds, MaxIters, g)
s.update(callback=log, interval=100)
print("Found best position: {0}".format(s.gbest))
