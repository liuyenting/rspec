import numpy as np
import plotly.graph_objs as go
import plotly.offline as offline

x = np.random.randn(2000)
y = np.random.randn(2000)

data = [
    go.Histogram2dContour(
        x=x, y=y, 
        contours=dict(coloring='heatmap')
    ),
    go.Scatter(
        x=x, y=y, 
        mode='markers', 
        marker={
            'color': 'white',
            'size': 3,
            'opacity': 0.3
        }
    )
]

layout = go.Layout(title="Purchases by place", showlegend=True)
figure = go.Figure(data=data, layout=layout)
offline.plot(figure)
