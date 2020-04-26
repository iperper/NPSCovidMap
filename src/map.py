"""
file: map.py
author: Margaret Trautner 
created: 04/25/2020
"""

import os
import folium
from folium import plugins
from branca.element import Template, MacroElement

print("Imports Complete")

def make_map(data, filename):

    m = folium.Map(location=[40.0150, -105.2705], zoom_start = 4, 
              tiles = 'Stamen Terrain')

    # Add markers 
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

    template = """
    {% macro html(this, kwargs) %}

    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>

     
    <div id='maplegend' class='maplegend' 
        style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
         border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
         
    <div class='legend-title'>Legend</div>
    <div class='legend-scale'>
      <ul class='legend-labels'>
        <li><span style='background:red;opacity:0.7;'></span>Closed</li>
        <li><span style='background:orange;opacity:0.7;'></span>Other</li>
        <li><span style='background:green;opacity:0.7;'></span>Open</li>

      </ul>
    </div>
    </div>
     
    </body>
    </html>

    <style type='text/css'>
      .maplegend .legend-title {
        text-align: left;
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 90%;
        }
      .maplegend .legend-scale ul {
        margin: 0;
        margin-bottom: 5px;
        padding: 0;
        float: left;
        list-style: none;
        }
      .maplegend .legend-scale ul li {
        font-size: 80%;
        list-style: none;
        margin-left: 0;
        line-height: 18px;
        margin-bottom: 2px;
        }
      .maplegend ul.legend-labels li span {
        display: block;
        float: left;
        height: 16px;
        width: 30px;
        margin-right: 5px;
        margin-left: 0;
        border: 1px solid #999;
        }
      .maplegend .legend-source {
        font-size: 80%;
        color: #777;
        clear: both;
        }
      .maplegend a {
        color: #777;
        }
    </style>
    {% endmacro %}"""

    macro = MacroElement()
    macro._template = Template(template)

    m.get_root().add_child(macro)
    m.save(filename) #filename should have .hmtl



if __name__ == "__main__":
    #Test Data
    data = [{"name": "Sunnyside Farm", "lon": -90.36971, "lat": 38.350260, "status": "other", "url": "cat-bounce.com", "desc": "I love Isaac, but he loves me more"}]

    make_map(data,'my_map.html')
    #To view, open file in browser
