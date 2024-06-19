import lightningchart as lc

# Read the license key from a file
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Define data for Hawaii
region_data = [
    {'ISO_A3': "USA-HI", 'value': 1}  # Dummy data to ensure map initializes properly
]

# Initialize the map chart
chart = lc.MapChart(map_type='USA', theme=lc.Themes.Dark, title='Seismic Data Points in Hawaii')

# Invalidate region values with the dummy data for Hawaii
chart.invalidate_region_values(region_data)

# Customize the chart
chart.set_highlight_on_hover(enabled=True)

# Set palette colors to visualize the data without making everything black
chart.set_palette_colors(
    steps=[
        {'value': 0, 'color': lc.Color('#fcba03')},
        {'value': 1, 'color': lc.Color('#fc3d03')},
    ],
    look_up_property='value',
    percentage_values=False
)

# Open the chart
chart.open(live=True)
