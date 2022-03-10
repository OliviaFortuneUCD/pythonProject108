import pandas as pd
import folium
location = "https://data.ehealthireland.ie/dataset/0261b860-9813-4ed0-b58f-797bd4020ed5/resource/f6727f58-a6bc-45f9-9657-84c9eecfd5b7/download/listofhospitalsinireland.csv"
hc = pd.read_csv(location)

# Keeping only necessary columns
hc_locations = hc[["y", "x", "name"]]
# Creating the map and adding points to it
map = folium.Map(location=[hc_locations.y.mean(), hc_locations.x.mean()], zoom_start=14, control_scale=True)

for index, location_info in hc_locations.iterrows():
    folium.Marker([location_info["y"], location_info["x"]], popup=location_info["name"]).add_to(map)
# Displaying the map
map.save('hc2.html')