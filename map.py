# We will use the Folium.py library to create a map of france where we will display the data
# The data will be extracted from the merged.csv file
# We will display the some point sized by the column "Tranche pour 1000 habitants" and colored by the max of the columns Arthaud	Roussel	Macron	Lassalle	Le Pen	Zemmour	Mélanchon	Hidalgo	Jadot	Pécresse	Poutou	Dupont-Aignan
# We will also display the name of the city when the user hover over the point

# The file merged.csv got the following columns: Code du departement	Inscrits	Abstentions	Votants	Blancs	Nuls	Exprimés	Arthaud	Roussel	Macron	Lassalle	Le Pen	Zemmour	Mélanchon	Hidalgo	Jadot	Pécresse	Poutou	Dupont-Aignan	Ville	Tranche pour 1000 habitants

import pandas as pd
import folium as fl
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap
import os

# Load the data
df = pd.read_csv("merged.csv", sep=";")
df = df.dropna()

# Create the map
m = fl.Map(location=[46.603354, 1.888334], zoom_start=6)

# Create a MarkerCluster
marker_cluster = MarkerCluster().add_to(m)

# Create a colormap for the columns Arthaud	Roussel	Macron	Lassalle	Le Pen	Zemmour	Mélanchon	Hidalgo	Jadot	Pécresse	Poutou	Dupont-Aignan
colormapper = {
    "Arthaud": "red",
    "Roussel": "green",
    "Macron": "blue",
    "Lassalle": "yellow",
    "Le Pen": "purple",
    "Zemmour": "orange",
    "Mélanchon": "pink",
    "Hidalgo": "black",
    "Jadot": "brown",
    "Pécresse": "cyan",
    "Poutou": "magenta",
    "Dupont-Aignan": "gray"
}

#add an html legend transparent on the map to explain the colors
legend_html = """
        <div style="position: fixed;
                    bottom: 50px; left: 50px; width: 150px; height: 370px;
                    border:2px solid grey; z-index:9999; font-size:14px;
                    background-color: white;
                    opacity: 0.8;
                    ">
        &nbsp; Arthaud &nbsp; <i class="fa fa-map-marker fa-2x" style="color:red"></i><br>
        &nbsp; Roussel &nbsp; <i class="fa fa-map-marker fa-2x" style="color:green"></i><br>
        &nbsp; Macron &nbsp; <i class="fa fa-map-marker fa-2x" style="color:blue"></i><br>
        &nbsp; Lassalle &nbsp; <i class="fa fa-map-marker fa-2x" style="color:yellow"></i><br>
        &nbsp; Le Pen &nbsp; <i class="fa fa-map-marker fa-2x" style="color:purple"></i><br>
        &nbsp; Zemmour &nbsp; <i class="fa fa-map-marker fa-2x" style="color:orange"></i><br>
        &nbsp; Mélanchon &nbsp; <i class="fa fa-map-marker fa-2x" style="color:pink"></i><br>
        &nbsp; Hidalgo &nbsp; <i class="fa fa-map-marker fa-2x" style="color:black"></i><br>
        &nbsp; Jadot &nbsp; <i class="fa fa-map-marker fa-2x" style="color:brown"></i><br>
        &nbsp; Pécresse &nbsp; <i class="fa fa-map-marker fa-2x" style="color:cyan"></i><br>
        &nbsp; Poutou &nbsp; <i class="fa fa-map-marker fa-2x" style="color:magenta"></i><br>
        &nbsp; Dupont-Aignan &nbsp; <i class="fa fa-map-marker fa-2x" style="color:gray"></i><br>
        </div>
        """
m.get_root().html.add_child(fl.Element(legend_html))

# Create a HeatMap for the column "Tranche pour 1000 habitants" and add it to the map
HeatMap(
    data=df[["Latitude", "Longitude", "Tranche pour 1000 habitants"]].values.tolist(),
    radius=15
).add_to(m)

# Use the colormap to color the markers based on the max of the columns Arthaud	Roussel	Macron	Lassalle	Le Pen	Zemmour	Mélanchon	Hidalgo	Jadot	Pécresse	Poutou	Dupont-Aignan
for i in range(0, len(df)):
    max_column = max(df.iloc[i][["Arthaud", "Roussel", "Macron", "Lassalle", "Le Pen", "Zemmour", "Mélanchon", "Hidalgo", "Jadot", "Pécresse", "Poutou", "Dupont-Aignan"]])
    for key in colormapper:
        if df.iloc[i][key] == max_column:
            fl.Marker(
                location=[df.iloc[i]["Latitude"], df.iloc[i]["Longitude"]],
                popup=df.iloc[i]["Ville"],
                icon=fl.Icon(color=colormapper[key])
            ).add_to(marker_cluster)
    
# Save the map
m.save("map.html")

# Open the map
os.system("map.html")