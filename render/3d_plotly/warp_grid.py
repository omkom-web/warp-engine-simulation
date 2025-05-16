import numpy as np
import plotly.graph_objects as go
from core.metrics import AlcubierreMetric

def generate_warp_grid(v_s=0.5, sigma=1.0, t=10.0):
    metric = AlcubierreMetric(v_s, sigma)
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)

    Z = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            g = metric.g11(X[i, j], t)
            Z[i, j] = (1.0 / g)  # visualiser la contraction spatiale

    fig = go.Figure(data=[
        go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')
    ])

    fig.update_layout(
        title=f"Warp Field Distortion — t = {t}",
        scene=dict(
            xaxis_title='x',
            yaxis_title='y',
            zaxis_title='Warp Intensity (1/g11)'
        ),
        autosize=True,
        margin=dict(l=0, r=0, b=0, t=50)
    )

    fig.show()

if __name__ == "__main__":
    generate_warp_grid()
