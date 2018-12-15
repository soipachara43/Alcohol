import pandas as pd
import pygal
from pygal.style import RedBlueStyle

def spirit():
    """start age"""
    gauge = pygal.SolidGauge(fill=True, interpolate='cubic', style=RedBlueStyle, inner_radius=0.70)
    gauge.add('เข้าสังคม/การสังสรรค์(49.30%)', [{'value': 7379565, 'max_value': 14000000}])
    gauge.add('อยากทดลองดื่ม(23.25%)', [{'value': 3480221, 'max_value': 14000000}])
    gauge.add('ตามอย่างเพื่อน/เพื่อนชวน(19.25%)', [{'value': 2881473, 'max_value': 14000000}])  
    gauge.add('ตามอย่างดารา/ผู้มีชื่อเสียง(2.90%)', [{'value': 434093, 'max_value': 14000000}])
    gauge.add('เพื่อเจริญอาหาร(1.60%)', [{'value': 239500, 'max_value': 14000000}])
    gauge.add('เครียด/วิตกกังวล(1.40%)', [{'value': 209562, 'max_value': 14000000}])
    gauge.add('ความผิดหวัง(0.60%)', [{'value': 89813, 'max_value': 14000000}])
    gauge.add('เพื่อความโก๋เก๋(0.55%)', [{'value': 82328, 'max_value': 14000000}])
    gauge.add('ตามอย่างสมาชิกในครอบครัว(0.50%)', [{'value': 74844, 'max_value': 14000000}])
    gauge.add('เพื่อความเป็นผู้ใหญ่(0.35%)', [{'value': 52391, 'max_value': 14000000}])
    gauge.add('ผู้ใหญ่ใช้ไปซื้อ(0.15%)', [{'value': 22450, 'max_value': 14000000}])
    gauge.add('ใช้เป็นยา/ส่วยผสมของยา(0.15%)', [{'value': 22450, 'max_value': 14000000}])
    gauge.render_to_file("motive_all.svg")
spirit()
