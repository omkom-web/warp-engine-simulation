import numpy as np

class AlcubierreMetric:
    def __init__(self, v_s=0.5, sigma=1.0):
        self.v_s = v_s
        self.sigma = sigma

    def f(self, x, t):
        """Fonction de distorsion : gaussienne mobile"""
        return np.exp(-((x - self.v_s * t) ** 2) / self.sigma ** 2)

    def g11(self, x, t):
        """Composante g11 de la métrique simplifiée"""
        return (1 - self.v_s * self.f(x, t))**2
