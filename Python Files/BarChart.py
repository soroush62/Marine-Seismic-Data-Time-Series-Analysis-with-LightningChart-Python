import lightningchart as lc
import pandas as pd
import numpy as np

with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/Data/output.csv'
df = pd.read_csv(file_path)

hist, bin_edges = np.histogram(df['trace_value'], bins=50)

data = [{'category': f'{(bin_edges[i] + bin_edges[i + 1]) / 2:.2f}', 'value': int(hist[i])} for i in range(len(hist))]

chart = lc.BarChart(
    vertical=True,
    theme=lc.Themes.Dark,
    title='Histogram of Seismic Trace Values'
)

chart.set_data(data)

chart.open()

x_axis_title = chart.add_textbox(text='Amplitude', x=50, y=95)
y_axis_title = chart.add_textbox(text='Frequency', x=5, y=50)
