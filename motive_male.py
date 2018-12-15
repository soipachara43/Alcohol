import pandas as pd
import pygal
from pygal.style import RedBlueStyle

def spirit():
    """start age"""
    gauge = pygal.SolidGauge(fill=True, interpolate='cubic', style=RedBlueStyle, inner_radius=0.70)
    gauge.add('เข้าสังคม/การสังสรรค์(37.60%)', [{'value': 7379565, 'max_value': 14000000}])
    gauge.add('อยากทดลองดื่ม(32.70%)', [{'value':  4138385 , 'max_value': 14000000}])
    gauge.add('ตามอย่างเพื่อน/เพื่อนชวน(25.00%)', [{'value': 3163903, 'max_value': 14000000}])  
    gauge.add('ตามอย่างดารา/ผู้มีชื่อเสียง(1.60%)', [{'value': 202490, 'max_value': 14000000}])
    gauge.add('เพื่อเจริญอาหาร(0.90%)', [{'value': 113900, 'max_value': 14000000}])
    gauge.add('เครียด/วิตกกังวล(0.70%)', [{'value': 88589, 'max_value': 14000000}])
    gauge.add('ความผิดหวัง(0.50%)', [{'value': 63278, 'max_value': 14000000}])
    gauge.add('เพื่อความโก๋เก๋(0.30%)', [{'value': 37967, 'max_value': 14000000}])
    gauge.add('ตามอย่างสมาชิกในครอบครัว((0.20%)', [{'value': 25312, 'max_value': 14000000}])
    gauge.add('เพื่อความเป็นผู้ใหญ่(0.20%)', [{'value': 25311, 'max_value': 14000000}])
    gauge.add('ผู้ใหญ่ใช้ไปซื้อ(0.20%)', [{'value': 25311, 'max_value': 14000000}])
    gauge.add('ใช้เป็นยา/ส่วยผสมของยา(0.10%)', [{'value': 12656, 'max_value': 14000000}])
    gauge.render_to_file("motive_male.svg")
spirit()
