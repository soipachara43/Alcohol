import pygal
import pandas as pd
from pygal.style import DarkStyle

def spirit():
    """start age"""
    data = pd.read_csv("Ttt235.csv")
    line_graph = pygal.Bar(fill=True, interpolate='cubic', style=DarkStyle)
    line_graph.x_labels = data.AGE
    line_graph.y_labels = map(int, range(0, 600001, 20000))
    line_graph.add("10-14 years old", data.ttt)
    line_graph.add("15-19 years old", data.rrr)
    line_graph.add("20-24 years old", data.yyy)
    line_graph.add("26-29 years old", data.iii)
    line_graph.add("30-34 years old", data.ooo)
    line_graph.add("35-39 years old", data.ppp)
    line_graph.add("Above 40 years old", data.ddd)
    line_graph.render_to_file("กราฟ1.svg")
spirit()

