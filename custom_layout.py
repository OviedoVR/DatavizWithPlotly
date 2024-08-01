import plotly.express as px

# Define a custom layout dictionary
custom_layout = {
    'width': 700,
    'height': 400,
    'paper_bgcolor': 'white',
    'plot_bgcolor': 'white',
    'font': {'family': 'Palatino', 'size': 12},
    'xaxis_showgrid': False,
    'yaxis_showgrid': False,
    'xaxis_linecolor': 'lightgray',
    'yaxis_linecolor': 'lightgray',
    'xaxis_zeroline': False,
    'xaxis': {'showline': True}
}

# Set the default template:
px.defaults.template = 'simple_white'

# Defining a color palette:
color_discrete_sequence = ['#ff9f1c', '#086375', '#47D45A', '#a4133c', '#61CBF4', '#3c1642']

# Create a custom marker style dictionary
custom_marker_style = {
    'size': 10,            # Adjust the size as needed
    'line_width': 1,
    'opacity': 0.7         # Adjust the opacity as needed
}

def update_facet_axes(fig):
    # Atualizar todos os eixos de facetas
    fig.update_xaxes(showgrid=False, showline=True, linecolor='lightgray', tickcolor='lightgray')
    fig.update_yaxes(showgrid=False, showline=True, linecolor='lightgray', tickcolor='lightgray')
    return fig
