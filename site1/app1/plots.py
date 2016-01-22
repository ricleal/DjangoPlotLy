from plotly.offline import plot
import plotly.plotly as py
import plotly.graph_objs as go

def plot1d():
    trace1 = go.Scatter(
        x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
    )
    trace2 = go.Scatter(
        x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    )
    data = [trace1, trace2]
    layout = go.Layout(
        xaxis=dict(
            type='log',
            autorange=True
        ),
        yaxis=dict(
            type='log',
            autorange=True
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div')
    return plot_div
