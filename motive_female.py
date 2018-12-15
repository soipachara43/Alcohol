import pandas as pd
import pygal
from pygal.style import RedBlueStyle

def spirit():
    """start age"""
    gauge = pygal.SolidGauge(fill=True, interpolate='cubic', style=RedBlueStyle, inner_radius=0.70)
    gauge.add('เข้าสังคม/การสังสรรค์(61.00%)', [{'value': 1410978, 'max_value': 14000000}])
    gauge.add('อยากทดลองดื่ม(13.80%)', [{'value':  319205 , 'max_value': 14000000}])
    gauge.add('ตามอย่างเพื่อน/เพื่อนชวน(13.50%)', [{'value': 312266, 'max_value': 14000000}])  
    gauge.add('ตามอย่างดารา/ผู้มีชื่อเสียง(4.20%)', [{'value': 97149, 'max_value': 14000000}])
    gauge.add('เพื่อเจริญอาหาร(2.90%)', [{'value': 67079, 'max_value': 14000000}])
    gauge.add('เครียด/วิตกกังวล(2.10%)', [{'value': 48575, 'max_value': 14000000}])
    gauge.add('ความผิดหวัง(1.00%)', [{'value': 23130, 'max_value': 14000000}])
    gauge.add('เพื่อความโก๋เก๋(0.80%)', [{'value': 18505, 'max_value': 14000000}])
    gauge.add('ตามอย่างสมาชิกในครอบครัว((0.20%)', [{'value': 4626, 'max_value': 14000000}])
    gauge.add('เพื่อความเป็นผู้ใหญ่(0.20%)', [{'value': 4626, 'max_value': 14000000}])
    gauge.add('ผู้ใหญ่ใช้ไปซื้อ(0.20%)', [{'value': 4626, 'max_value': 14000000}])
    gauge.add('ใช้เป็นยา/ส่วยผสมของยา(0.10%)', [{'value': 2313, 'max_value': 14000000}])
    gauge.render_to_file("motive_female.svg")
spirit()
