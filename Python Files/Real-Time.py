import lightningchart as lc
import pandas as pd
import numpy as np
import time

# Read the license key from a file
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load the CSV file
file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/Data/output.csv'
df = pd.read_csv(file_path)

# Convert sample number to time (assuming the sample interval is in microseconds)
df['time_ms'] = df['sample_number'] * df['sample_interval_in_ms_for_this_trace'] / 1000.0

# Create a ChartXY for real-time rendering
chart = lc.ChartXY(
    theme=lc.Themes.Dark,
    title='Real-Time Seismic Trace Display'
)

# Add a Point Series for displaying the trace
point_series = chart.add_point_series()

# Customize axis titles
chart.get_default_x_axis().set_title('Time (ms)')
chart.get_default_y_axis().set_title('Amplitude')

# Function to update the chart with a new trace
def update_chart(trace_number):
    # Get the data for the specified trace
    trace_data = df[df['trace_sequence_number_within_line'] == trace_number]
    if not trace_data.empty:
        x_values = trace_data['time_ms'].values.tolist()
        y_values = trace_data['trace_value'].values.tolist()
        # Update the point series with new data
        point_series.clear().add(x_values, y_values)

# Loop through all traces and update the chart in real-time
for trace_number in df['trace_sequence_number_within_line'].unique():
    update_chart(trace_number)
    time.sleep(0.1)  # Delay to simulate real-time update

# Open the chart in the default web browser
chart.open()
