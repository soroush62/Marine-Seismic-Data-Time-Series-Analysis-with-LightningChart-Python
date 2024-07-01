import lightningchart as lc
import pandas as pd
import numpy as np

lc.set_license('my-license-key')

file_path = 'output.csv'
df = pd.read_csv(file_path)

hist, bin_edges = np.histogram(df['trace_value'], bins=50)

log_hist = np.log10(hist + 1) 

data = [{'category': f'{(bin_edges[i] + bin_edges[i + 1]) / 2:.2f}', 'value': int(hist[i])} for i in range(len(hist))]


chart = lc.BarChart(
    vertical=True,
    theme=lc.Themes.Dark,
    title='Histogram of Seismic Trace Values',
    axis_type='logarithmic',
    axis_base=10
)

chart.set_sorting('disabled')

chart.set_data(data)

chart.open()


