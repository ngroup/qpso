# qpso
A Python implementation of quantum particle swarm optimization (QPSO).

    pip install qpso

This is a black-box optimization package built upon the quantum paricle swarm
optimization [1].

## Quickstart
The usage of this package is very simple.
For example, the following code shows how to solve a 10-dimensional opmitzation
problem by using QPSO with Delta potential well (QDPSO) proposed in [1].

```python
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
```

## Bibliography 

[1] Jun Sun, Bin Feng and Wenbo Xu, "Particle swarm optimization with particles having quantum behavior," Proceedings of the 2004 Congress on Evolutionary Computation (IEEE Cat. No.04TH8753), Portland, OR, USA, 2004, pp. 325-331 Vol.1.
doi: 10.1109/CEC.2004.1330875
