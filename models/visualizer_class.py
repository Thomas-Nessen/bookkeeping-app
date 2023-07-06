import plotly.graph_objects as go
import plotly.express as px
from datetime import timedelta
import pandas as pd
import numpy as np

class VisualizerClass(object):
    """
    This class is used to visualize the transaction data to the user.
    It includes functions for:
        - (Monthly) bar graph
        - (Monthly) pie chart
        - Single transactions
        
    """
    def __init__(self):
    # def __init__(self, cat_data):
        # self.data = cat_data
        self.colours = [
            "#ff6961", "#ffb480", "#f8f38d", "#42d6a4",
            "#08cad1", "#59adf6", "#9d94ff", "#c780e8"
            ] 

    
    def bar_graph_categories(self, data, x_column:str , y_column:str, colours=None):
        # use default colours if not given
        colours = self.colours if colours == None else colours

        try:
            # create dict with total sum of transactions per category
            cats = data[x_column].unique()    # Could also get these from sorting codes?
            vis_data = {}
            for cat in cats:
                #set category as key, select corresponding rows, set value as rounded sum of the 'Amount' column
                vis_data[cat] = data[data[x_column] == cat][y_column].sum().round(2)
        except AttributeError as e: 
            print(e)
            print("The data types of one or more of the columns is incorrect.")
        except KeyError as e:
            print(e)
            print("One or more of the columns given does not exist")

        fig = go.Figure(
            data=[go.Bar(
                x=list(vis_data.keys()),
                y=list(vis_data.values()),
                title = "Hoi",
                marker_color=colours)
            ]
        )

        fig.show()
        
    def stacked_bar_graph(self, data):
        fig = px.bar(
            data, x="Date", y="Amount", color="Category",
            hover_name=data["Name / Description"]) #, Tag="Tag"))

        fig.update_layout(
            title_text = "Daily expenses overview",
            colorway = self.colours
        )
        fig.update_xaxes(
            type='date',
            dtick = 86400000,
            range = [
                data['Date'].min() - timedelta(days=1),
                data['Date'].max() + timedelta(days=1)
                ]
            )
        fig.update_yaxes(tick0 = 0)
        
        fig.show()

    if __name__ == "__main__":
        stacked_bar_graph()

