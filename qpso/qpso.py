import numpy as np
import random


class Particle(object):
    def __init__(self, bounds):
        self._x = np.zeros(len(bounds))
        for idx, (lo, hi) in enumerate(bounds):
            self._x[idx] = random.uniform(lo, hi)

        self._best = self._x.copy()
        self._best_value = np.NaN

    def __str__(self):
        return str(self._x)

    @property
    def best(self):
        return self._best

    def set_best(self, x):
        for i, v in enumerate(x):
            self._best[i] = v

    @property
    def best_value(self):
        return self._best_value

    def set_best_value(self, v):
        self._best_value = v

    def __getitem__(self, key):
        return self._x[key]

    def __setitem__(self, key, val):
        self._x[key] = val


class Swarm(object):
    def __init__(self, size, dim, bounds):
        self._particles = [Particle(bounds) for i in range(0, size)]
        self._dim = dim
        self._gbest_value = None
        self._gbest = None

    def size(self):
        return len(self._particles)

    def particles(self):
        return self._particles

    def mean_best(self):
        x = np.zeros(self._dim)
        for p in self._particles:
            x += p.best

        x /= self.size()

        return x

    @property
    def gbest(self):
        return self._gbest

    @property
    def gbest_value(self):
        return self._gbest_value

    def update_gbest(self):
        get_best_value = lambda x: x.best_value
        pg = min(self.particles(), key=get_best_value)
        if (not self._gbest_value) or self._gbest_value > pg.best_value:
            self._gbest = pg.best.copy()
            self._gbest_value = pg.best_value


class QPSO(Swarm):
    def __init__(self, cf, size, dim, bounds, maxIters):
        super(QPSO, self).__init__(size, dim, bounds)
        self._cf = cf
        self._maxIters = maxIters
        self._iters = 0
        self.init_eval()

    def init_eval(self):
        for p in self.particles():
            pc = self._cf(p[:])
            p.set_best_value(pc)

        self.update_gbest()

    def update_best(self):
        for p in self.particles():
            pc = self._cf(p[:])
            if pc < p.best_value:
                p.set_best(p[:])
                p.set_best_value(pc)

        self.update_gbest()

    def kernel_update(self, **kwargs):
        pass

    def update(self, callback=None, interval=None):
        while self._iters <= self._maxIters:
            self.kernel_update()
            self.update_best()
            if callback and (self._iters % interval == 0):
                callback(self)

            self._iters += 1

    @property
    def iters(self):
        return self._iters

    @property
    def maxIters(self):
        return self._maxIters


class QDPSO(QPSO):
    def __init__(self, cf, size, dim, bounds, maxIters, g):
        super(QDPSO, self).__init__(cf, size, dim, bounds, maxIters)
        self._g = g

    def kernel_update(self, **kwargs):
        for p in self._particles:
            for i in range(0, self._dim):
                u1 = random.uniform(0., 1.)
                u2 = random.uniform(0., 1.)
                u3 = random.uniform(0., 1.)
                rand_sign = 1 if random.random() > 0.5 else -1
                c = (u1 * p.best[i] + u2 * self._gbest[i]) / (u1 + u2)
                L = (1 / self._g) * abs(p[i] - c)
                p[i] = c + rand_sign * L * np.log(1. / u3)
