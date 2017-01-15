import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],
    zoom_start=5, tiles='Stamen Terrain')

def color(elev):
    minimum = int(min(df['ELEV']))
    maximum = int(max(df['ELEV']))
    step = int((maximum - minimum) / 3)
    if elev in range(minimum, minimum + step) :
        col = 'green'
    elif elev in range(minimum + step, minimum + step * 2):
        col = 'orange'
    else:
        col = 'red'
    return col


for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.add_child(folium.Marker(location=[lat, lon], popup=name,
        icon=folium.Icon(color=color(elev), icon_color='green')))

map.add_child(folium.GeoJson(data=open('World_population.json'),
    name = 'World Population'))
map.save(outfile='map_with_markers.html')
