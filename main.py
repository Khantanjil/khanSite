# Importing pandas and folium
import folium # visualize data
import requests # HTTP Library
from color import * # Function to fill the color
import pandas # Read the file


# Map
class Meterology():
    global i

    """
    The map shows the informations of the basics meteorology, if it's rainning return blue on the each country, return yellow if it's a good time!
    """

    # Constructs a base map
    def __init__(self):

        global base_map
        
        """Base map with folium"""
        base_map = folium.Map(
            location = [41.1579, -8.6291], # Coordinates
            min_zoom = 3,
            max_zoom = 10,
            zoom_start = 10,
            tiles = 'OpenStreetMap' # Background map
        )

    def saveFile(self):
        """ Save the map file in the html file """
        
        base_map.save("templates/meteo.html") # Save the file on html

 
    def populationGroup(self):
        """
        Add the GeoJson layers on the map
        """
        fgP = folium.FeatureGroup(name="Population on the world") # Add feature group of the population
        
        fgP.add_child(folium.GeoJson(data=open('jsons/world.json', 'r').read(),
        style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
        else 'red'}))
        base_map.add_child(fgP) # Add to the feature group

    def portugalGroup(self):
        """GeoJson for portugal"""
        fg_portugal = folium.FeatureGroup(name="Portugal") # Feature group Portugal
        fg_portugal.add_child(folium.GeoJson("jsons/portugal.json"), name="geojson")
        base_map.add_child(fg_portugal) # Add to the feature group
        
    def meteorologia(self):
        """ Temperatura maxima (no dia atual)"""
        # Depois de acabar isso
        # Temperatura maxima nos dias proximos (Previsao)
        fg_met = folium.FeatureGroup(name="Temperatura Maxima") # Feature group temperatura
        # Read the file, create columns and rows with id
        data = pandas.read_csv("coordinates.txt")
        latitude = list(data["Latitude"]) # Make a list of the latitude
        longitude = list(data["Longitude"]) # Make a list of the longitude
        city = list(data["City"]) # Make a list of the cities
        temperature = list(data["Temperature"]) # Make a list of the temperatures
        for tm, ct, lt, ln in zip(temperature, city, latitude, longitude):
            # HTML POPUP FOLIUM ICON
            html = """<h3>Informations about the %s:</h3>
            <p>The max temperature: %s<p>
            <p>The latitude: %s</p>
            <p>The longitude: %s</p>
            """
                
            iframe = folium.IFrame(html = html % (str(ct), str(tm), str(lt), str(ln)), width=200, height=200) # Add the html to POPUP
            fg_met.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe),fill=True,radius=8, fill_color=producerColor(tm), color="black", fill_opacity=1)) # Add the icon to temps
            base_map.add_child(fg_met)



    
    def addControl(self):
        """ Add the layer control on the map"""
        folium.LayerControl().add_to(base_map)

    def readInfo(self):
        data = pandas.read_csv("coordinates.txt")
        #print(data)
