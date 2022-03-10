# import folium package
import folium

my_map4 = folium.Map(location=[53.426448 ,-6.249910],
                     zoom_start=12)



folium.Marker([53.426448 ,-6.249910],
              popup='Dublin').add_to(my_map4)

folium.Marker([53.428665 ,-8.3320801],
              popup='Center').add_to(my_map4)

# Add a line to the map by using line method .
# it connect both coordinates by the line
# line_opacity implies intensity of the line

folium.PolyLine(locations=[(53.426448 ,-6.249910), (53.428665 ,-8.3320801)],
                line_opacity=0.5).add_to(my_map4)

my_map4.save("my_map4.html")

