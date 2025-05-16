import matplotlib.pyplot as plt

def setup_plot():
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(0, 1.5)
    ax.set_title("Composante $g_{11}(x, t)$ — warp metric")
    ax.set_xlabel("x")
    ax.set_ylabel("g11")
    return fig, ax
