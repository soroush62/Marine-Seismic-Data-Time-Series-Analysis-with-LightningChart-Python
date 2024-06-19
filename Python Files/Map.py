import lightningchart as lc
import pandas as pd

# Read the license key from a file
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load the CSV file containing longitude and latitude data
file_path = 'D:/path_to_your_csv_file.csv'  # Update this with your file path
df = pd.read_csv(file_path)

# Assuming your CSV file has 'longitude' and 'latitude' columns
# If not, you can add these columns based on the known geographic feature (Hawaii)

# Initialize MapChart
map_chart = lc.MapChart(
    map_type='World',
    theme=lc.Themes.Dark,
    title='Map of Seismic Data Points in Hawaii'
)

# Add a point series to plot longitude and latitude points
point_series = map_chart.add_point_series()

# Set data for the point series
for index, row in df.iterrows():
    point_series.add_point(row['longitude'], row['latitude'])

# Customize the map chart (optional)
map_chart.set_highlight_on_hover(enabled=True)
map_chart.set_solid_color(lc.Color('#000000'))  # Set map color
map_chart.set_stroke(0.5, lc.Color('#FFFFFF'))  # Set border color

# Open the map chart
map_chart.open()
