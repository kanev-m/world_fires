import csv
from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/world_fires_105_705.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # яркость, долгота, широта, дата
    brightness, lons, lats, date = [], [], [], []
    for index, column_header in enumerate(header_row):
        print(index, column_header)

        for info in reader:
            lons.append(float(info[1]))
            lats.append(float(info[0]))
            date.append(info[5])
            bright = info[2].split('.')
            brightness.append(int(bright[0]))


# данные на карте
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': date,
    'marker': {
        'size': [(br/100) * 2 for br in brightness],
        'color': brightness,
        'colorscale': 'ylorrd',
        'colorbar': {'title': 'Brightness'},
    },
}]


my_layout = Layout(title='World fires: 1 may 2024 - 7 may 2024')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')