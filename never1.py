import pandas as pd
import pygal
from pygal.style import DarkStyle

def spirit():
    """start age"""
    data = pd.read_csv("neverall.csv")
    line_graph = pygal.Pie(fill=True, interpolate='cubic', style=DarkStyle)
    line_graph.x_labels = data.AGE
    line_graph.add("10-14 years old", data.TENTOFOURTEEN)
    line_graph.add("15-19 years old", data.FIFTHTEENTONINETEEN)
    line_graph.add("20-24 years old", data.TWENTYTOTWENTYFOUR)
    line_graph.add("25-29 years old", data.TWENTYFIVETOTWENTYNINE)
    line_graph.add("30-34 years old", data.THIRTYTOTHIRFOUR)
    line_graph.add("35-39 years old", data.THIRFIVETOTHIRNINE)
    line_graph.add("Above 40 years old", data.ABOVEFORTY)
    line_graph.render_to_file("neverall1.svg")
spirit()

