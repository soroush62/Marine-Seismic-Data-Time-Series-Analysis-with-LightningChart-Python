import lightningchart as lc
import pandas as pd

# Read the license key from a file
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load the CSV file
file_path = 'D:/wenprograming23/src/team6/Marine-Seismic-Data-Time-Series-Analysis-with-LightningChart-Python/Data/output.csv'
df = pd.read_csv(file_path)

# Convert sample number to time (assuming the sample interval is in microseconds)
df['time_ms'] = df['sample_number'] * df['sample_interval_in_ms_for_this_trace'] / 1000.0

# Create a Scatter Plot
chart = lc.ChartXY(
    theme=lc.Themes.Dark,
    title='Scatter Plot of Amplitude vs. Time'
)

# Add a Point Series for the scatter plot
point_series = chart.add_point_series()

# Set data for the point series
point_series.add(df['time_ms'].values.tolist(), df['trace_value'].values.tolist())

# Customize axis titles
chart.get_default_x_axis().set_title('Time (ms)')
chart.get_default_y_axis().set_title('Amplitude')

# Show the chart
chart.open()
