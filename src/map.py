"""
file: map.py
author: Margaret Trautner 
created: 04/25/2020
"""

import os
import folium
from folium import plugins

print("Imports Complete")

def make_map(data, filename):

    m = folium.Map(location=[40.0150, -105.2705], zoom_start = 4, 
              tiles = 'Stamen Terrain')

    # Add markers 
    data = data[0:358]
    for park in data:
        status = park["status"]
        name = park["name"]
        desc = park["desc"]
        url = park["url"]
        i_color = None
        if status == "closed":
            i_color = 'red'
        elif status == "open":
            i_color = 'green'
        else: i_color = "orange"

        test = folium.Html('<strong>'+name+'</strong><br/>'+desc + '<br/><a href='+url+">More Information</a>", script=True)
        popup = folium.Popup(test, max_width=500)

        folium.Marker(
            location = [park["lat"],park["lon"]],
            popup = popup,
            icon = folium.Icon(icon = 'tree',prefix = 'fa',color = i_color)).add_to(m)


    # Display m
    m.save(filename) #filename should have .hmtl

if __name__ == "__main__":
    #Test Data
    data = [{"name": "Sunnyside Farm", "lon": -90.36971, "lat": 38.350260, "status": "other", "url": "cat-bounce.com", "desc": "I love Isaac, but he loves me more"}]

    make_map(data,'my_map.html')
    #To view, open file in browser
