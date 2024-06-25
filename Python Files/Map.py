import lightningchart as lc

with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

region_data = [
    {'ISO_A3': "USA", 'value': 1}  
]

chart = lc.MapChart(map_type='USA', theme=lc.Themes.Dark, title='Seismic Data Points in Hawaii')

chart.invalidate_region_values(region_data)

chart.set_highlight_on_hover(enabled=True)

chart.set_palette_colors(
    steps=[
        {'value': 0, 'color': lc.Color('#fcba03')},
        {'value': 1, 'color': lc.Color('#fc3d03')},
    ],
    look_up_property='value',
    percentage_values=False
)

chart.open(live=True)