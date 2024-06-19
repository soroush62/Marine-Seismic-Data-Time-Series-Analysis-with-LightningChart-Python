import lightningchart as lc
import pandas as pd

# Read the license key from a file
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load the CSV file containing longitude and latitude data
file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/Navigation/navigation_data - Copy.csv'
df = pd.read_csv(file_path)

# Prepare data for plotting
points_data = [
    {'longitude': row['longitude'], 'latitude': row['latitude'], 'value': 1}  # value can be adjusted as needed
    for _, row in df.iterrows()
]

# Initialize the map chart
chart = lc.MapChart(map_type='USA', theme=lc.Themes.Dark, title='Seismic Data Points in Hawaii')

# Since we don't have ISO_A3 for Hawaii, we'll use coordinates directly
chart.invalidate_region_values([
    {'ISO_A3': 'USA', 'value': 1}  # Dummy data to ensure map initializes properly
])

# Add a point series to plot longitude and latitude points
point_series = chart.add_point_series()

# Add data points to the point series
for point in points_data:
    point_series.add_point(point['longitude'], point['latitude'])

# Customize the chart (optional)
chart.set_highlight_on_hover(enabled=True)
chart.set_background_color(lc.Color('#000000'))  # Set background color
chart.set_bounding_box_stroke(0.5, lc.Color('#FFFFFF'))  # Set stroke color

# Open the chart
chart.open()
