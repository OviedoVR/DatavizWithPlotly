import plotly.express as px

def apply_custom_layout(fig, title='', title_x=0.5):
    # Define a custom layout dictionary
    custom_layout = {
        'template': 'simple_white',
        'width': 800,
        'height': 300,
        'font': {'family': 'Palatino', 'size': 15},
        'font_color': 'gray',
        'xaxis_showgrid': False,
        'yaxis_showgrid': False,
        'xaxis_linecolor': 'black',
        'yaxis_linecolor': 'black',
        'xaxis_zeroline': False,
        'xaxis': {'showline': True, 'linecolor': 'lightgray', 'tickcolor': 'lightgray'},
        'yaxis': {'showline': True, 'linecolor': 'lightgray', 'tickcolor': 'lightgray'},
        'title': {'text': title, 'x': title_x, 'xanchor': 'center'}
    }

    # Update the figure layout
    fig.update_layout(**custom_layout)

    # Update the marker style for all traces
    custom_marker_style = {
        'size': 10,            # Adjust the size as needed
        'line_width': 0.08,
        'opacity': 0.7         # Adjust the opacity as needed
    }

    for trace in fig.data:
        if 'marker' in trace:
            trace.marker.update(custom_marker_style)

    # Define the custom color sequence
    color_discrete_sequence = ['#708090', '#8A9A5B', 'crimson', '#B87333', '#ffd60a']
    fig.update_traces(marker=dict(color=color_discrete_sequence))

    # Atualizar todos os eixos de facetas
    fig.update_xaxes(showgrid=False, showline=True, linecolor='lightgray', tickcolor='lightgray')
    fig.update_yaxes(showgrid=False, showline=True, linecolor='lightgray', tickcolor='lightgray')
    
    return fig
