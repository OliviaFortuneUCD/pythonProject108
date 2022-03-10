# import folium package
import folium

my_map2 = folium.Map(location=[53.350140, -6.266155],
                     zoom_start=12)

# CircleMarker with radius
folium.CircleMarker(location=[53.350140, -6.266155],
                    radius=50, popup=' FRI ').add_to(my_map2)

# save as html
my_map2.save("my_map2.html ")

