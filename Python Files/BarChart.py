# import lightningchart as lc
# import pandas as pd
# import numpy as np

# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/Data/output.csv'
# df = pd.read_csv(file_path)

# hist, bin_edges = np.histogram(df['trace_value'], bins=50)

# data = [{'category': f'{(bin_edges[i] + bin_edges[i + 1]) / 2:.2f}', 'value': int(hist[i])} for i in range(len(hist))]

# chart = lc.BarChart(
#     vertical=True,
#     theme=lc.Themes.Dark,
#     title='Histogram of Seismic Trace Values'
# )

# chart.set_data(data)

# chart.open()



# import lightningchart as lc
# import pandas as pd
# import numpy as np

# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/output1.csv'
# df = pd.read_csv(file_path)

# hist, bin_edges = np.histogram(df['trace_value'], bins=50)

# log_hist = np.log10(hist + 1)  # Adding 1 to avoid log(0)

# x_data = [(bin_edges[i] + bin_edges[i + 1]) / 2 for i in range(len(hist))]
# y_data = [log_hist[i] for i in range(len(hist))]


# chart = lc.ChartXY(
#     theme=lc.Themes.Dark,
#     title='Histogram of Seismic Trace Values'
# )

# line_series = chart.add_line_series()

# line_series.add(x_data, y_data)

# chart.get_default_y_axis().set_title('Frequency (log scale)')
# chart.get_default_x_axis().set_title('Amplitude')

# chart.open()



import lightningchart as lc
import pandas as pd
import numpy as np

# Load the license key
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load the CSV file
file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/output1.csv'
df = pd.read_csv(file_path)

# Compute the histogram
hist, bin_edges = np.histogram(df['trace_value'], bins=50)

# Apply a logarithmic transformation to the histogram values
log_hist = np.log10(hist + 1)  # Adding 1 to avoid log(0)

# Prepare data for the bar chart
data = [{'category': f'{(bin_edges[i] + bin_edges[i + 1]) / 2:.2f}', 'value': log_hist[i]} for i in range(len(hist))]

# Print the data for debugging
print("Data for the chart:")
for point in data:
    print(point)

# Create a bar chart
chart = lc.BarChart(
    vertical=True,
    theme=lc.Themes.Dark,
    title='Histogram of Seismic Trace Values'
)

# Set the sorting to disabled
chart.set_sorting('disabled')

# Set the data for the bar chart
chart.set_data(data)

# Open the chart
chart.open()
