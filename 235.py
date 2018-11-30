import pygal
import pandas as pd

def spirit():
    """start age"""
    data = pd.read_csv("Ttt235.csv")
    line_graph = pygal.Bar()
    line_graph.title = "ช่วงอายุที่เริ่มดื่มสุรา"
    line_graph.x_labels = data.AGE
    line_graph.y_labels = map(int, range(10000, 600000, 30000))
    line_graph.add("COUNT1", data.COUNT1)
    line_graph.add("COUNT2", data.COUNT2)
    line_graph.add("COUNT3", data.COUNT3)
    line_graph.add("COUNT4", data.COUNT4)
    line_graph.add("COUNT5", data.COUNT5)
    line_graph.add("COUNT6", data.COUNT6)
    line_graph.add("COUNT7", data.COUNT7)
    line_graph.render_to_file("Ttt235.svg")
spirit()
