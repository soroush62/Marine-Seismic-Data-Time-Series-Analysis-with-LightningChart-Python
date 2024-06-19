import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
df = pd.read_csv('D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/Data/output.csv')

# Convert sample number to time (assuming the sample interval is in microseconds)
df['time_ms'] = df['sample_number'] * df['sample_interval_in_ms_for_this_trace'] / 1000.0

# Plot the time-series data for the first few traces
fig, ax = plt.subplots(figsize=(15, 6))

# Plotting traces: assuming you want to plot the first few traces
unique_traces = df['trace_sequence_number_within_line'].unique()
for trace in unique_traces[:1]:  # Plot first 5 traces for example
    trace_data = df[df['trace_sequence_number_within_line'] == trace]
    ax.plot(trace_data['time_ms'], trace_data['trace_value'], label=f'Trace {trace}')

# Set labels and title
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Amplitude')
ax.set_title('Time-Series Analysis of Seismic Data')
ax.legend()

# Show the plot
plt.show()
