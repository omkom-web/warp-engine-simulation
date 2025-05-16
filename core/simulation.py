import numpy as np

def generate_field(metric, x_vals, t_vals):
    """Génère un tableau 2D des valeurs g11(x, t)"""
    field = np.zeros((len(t_vals), len(x_vals)))
    for i, t in enumerate(t_vals):
        field[i, :] = metric.g11(x_vals, t)
    return field
