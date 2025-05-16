import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from core.metrics import AlcubierreMetric
from core.visual_utils import setup_plot

def run():
    metric = AlcubierreMetric(v_s=0.5, sigma=1.0)
    x_vals = np.linspace(-10, 10, 400)
    t_vals = np.linspace(0, 20, 100)

    fig, ax = setup_plot()
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        t = t_vals[frame]
        y_vals = metric.g11(x_vals, t)
        line.set_data(x_vals, y_vals)
        ax.set_title(f"$g_{{11}}(x, t)$ — t = {t:.2f}")
        return line,

    ani = FuncAnimation(fig, update, frames=len(t_vals), init_func=init, blit=True)
    plt.show()
