import pandas as pd
import pygal
from pygal.style import RedBlueStyle

def spirit():
    """start age"""
    data = pd.read_csv("ailing.csv")
    date_chart = pygal.HorizontalBar()
    date_chart.add("โรคตับแข็ง", 42)
    date_chart.add("โรคความดันโลหิตสูง", 28)
    date_chart.add("โรคหัวใจ", 20)
    date_chart.add("อื่นๆ", 10)
    date_chart.render_to_file("last.svg")
spirit()
