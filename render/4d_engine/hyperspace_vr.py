import numpy as np
from core.metrics import AlcubierreMetric
from core.simulation import generate_field
import plotly.express as px

def render_4d_slice(v_s=0.5, sigma=1.0):
    metric = AlcubierreMetric(v_s, sigma)
    x_vals = np.linspace(-10, 10, 100)
    t_vals = np.linspace(0, 20, 100)

    data = generate_field(metric, x_vals, t_vals)

    fig = px.imshow(
        data,
        labels=dict(x="x", y="t", color="g11"),
        x=x_vals,
        y=t_vals,
        aspect="auto",
        color_continuous_scale="viridis"
    )

    fig.update_layout(
        title="Projection 4D : g11(x, t)",
        xaxis_title="Position x",
        yaxis_title="Temps t"
    )

    fig.show()

if __name__ == "__main__":
    render_4d_slice()
