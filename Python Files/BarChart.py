import lightningchart as lc
import pandas as pd
import numpy as np

# Read the license key from a file
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load the CSV file
file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/Data/output.csv'
df = pd.read_csv(file_path)

# Calculate histogram data
hist, bin_edges = np.histogram(df['trace_value'], bins=50)

# Prepare data for the bar chart
data = [{'category': f'{(bin_edges[i] + bin_edges[i + 1]) / 2:.2f}', 'value': int(hist[i])} for i in range(len(hist))]

# Create a Bar Chart
chart = lc.BarChart(
    vertical=True,
    theme=lc.Themes.Dark,
    title='Histogram of Seismic Trace Values'
)

# Set the data for the bar chart
chart.set_data(data)

# Show the chart
chart.open()

# Add axis titles using text boxes
x_axis_title = chart.add_textbox(text='Amplitude', x=50, y=95)
y_axis_title = chart.add_textbox(text='Frequency', x=5, y=50)
