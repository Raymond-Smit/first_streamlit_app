
pip install folium
import folium

# Create a map centered at a specific location
m = folium.Map(location=[latitude, longitude], zoom_start=10)

# Add a marker to the map
folium.Marker(
    location=[latitude, longitude],
    popup="Marker Popup Text",
    icon=folium.Icon(color='blue')
).add_to(m)

# Save the map to an HTML file
m.save('map.html')

# Open the map in a web browser
import webbrowser
webbrowser.open('map.html')
