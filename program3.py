# import folium package
import folium

my_map3 = folium.Map(location=[53.350140, -6.266155],
                     zoom_start=15)

# Pass a string in popup parameter
folium.Marker([53.350140, -6.266155],
              popup=' Ourcompany ').add_to(my_map3)

my_map3.save(" my_map3.html ")