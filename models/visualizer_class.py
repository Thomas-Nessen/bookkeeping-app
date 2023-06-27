import plotly.graph_objects as go

class DisplayClass(object):
    """
    This class is used to visualize the transaction data to the user.
    It includes functions for:
        - (Monthly) bar graph
        - (Monthly) pie chart
        - Single transactions
        
    """
    def __init__(self, cat_data):
        self.data = cat_data

    
    def bar_graph(self, data):
        # pass

        #  Get a convenient list of x-values
        years = data['year']
        x = list(range(len(years)))

        # Specify the plots
        bar_plots = [
            go.Bar(x=x, y=data['conservative'], name='Conservative', marker=go.bar.Marker(color='#0343df')),
            go.Bar(x=x, y=data['labour'], name='Labour', marker=go.bar.Marker(color='#e50000')),
            go.Bar(x=x, y=data['liberal'], name='Liberal', marker=go.bar.Marker(color='#ffff14')),
            go.Bar(x=x, y=data['others'], name='Others', marker=go.bar.Marker(color='#929591')),
        ]

        # Customise some display properties
        layout = go.Layout(
            title=go.layout.Title(text="Election results", x=0.5),
            yaxis_title="Seats",
            xaxis_tickmode="array",
            xaxis_tickvals=list(range(27)),
            xaxis_ticktext=tuple(data['year'].values),
        )

        # Make the multi-bar plot
        fig = go.Figure(data=bar_plots, layout=layout)

        # Tell Plotly to render it
        fig.show()