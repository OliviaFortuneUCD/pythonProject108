import pandas as pd
import folium
location = "hccenters.csv"
hc = pd.read_csv(location)

# Keeping only necessary columns
hc_locations = hc[["LAT", "LONG", "Name"]]
# Creating the map and adding points to it
map = folium.Map(location=[hc_locations.LAT.mean(), hc_locations.LONG.mean()], zoom_start=14, control_scale=True)

for index, location_info in hc_locations.iterrows():
    folium.Marker([location_info["LAT"], location_info["LONG"]], popup=location_info["Name"]).add_to(map)
# Displaying the map
map.save('hc.html')