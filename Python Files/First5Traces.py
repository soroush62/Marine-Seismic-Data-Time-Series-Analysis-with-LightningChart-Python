import lightningchart as lc
import pandas as pd

lc.set_license('my-license-key')

file_path = 'output.csv'
df = pd.read_csv(file_path)

df['time_ms'] = df['sample_number'] * df['sample_interval_in_ms_for_this_trace'] / 1000.0

trace_max_amplitudes = df.groupby('trace_sequence_number_within_line')['trace_value'].max()
top_traces = trace_max_amplitudes.nlargest(5).index

chart = lc.ChartXY(
    theme=lc.Themes.Black,
    title='Top 5 Traces with Largest Amplitude Values'
)

chart.get_default_y_axis().dispose()

legend = chart.add_legend()

for i, trace in enumerate(top_traces):
    trace_data = df[df['trace_sequence_number_within_line'] == trace]
    axis_y = chart.add_y_axis(stack_index=i)
    axis_y.set_margins(15 if i > 0 else 0, 15 if i < 4 else 0)  
    axis_y.set_title(title=f'Trace {trace}')
    series = chart.add_line_series(y_axis=axis_y, data_pattern='ProgressiveX')
    series.add(trace_data['time_ms'].tolist(), trace_data['trace_value'].tolist())
    series.set_name(f'Trace {trace}')
    legend.add(series)

x_axis = chart.get_default_x_axis()
x_axis.set_title('Time (ms)')

chart.open()
