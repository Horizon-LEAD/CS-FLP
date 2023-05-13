# CS-FLP
A MILP formulation of the Facility Location Problem model focusing finding optimal locations of Charging Stations in Logistics Networks based on distance and demand. More specifically this is an implementation of a weighted p-median model that chooses optimal locations for Charging Stations to be placed out of N available locations (i.e. LSP depots). This model has been developed in the context of LEAD project, as a part of a wider decision support modelling library in last-mile logistics.

<img src="https://user-images.githubusercontent.com/10188642/236615578-8b6be06c-4497-4f1c-8830-a262bd080a0c.png" width="225" height="50"> <img src="https://user-images.githubusercontent.com/10188642/236615420-3b5ee101-4954-4f4c-b811-1461efa40a20.png" width="200" height="125">

### Input files:
1) Parcel deliveries data,
2) Depot data,
3) OpenStreetMap .osm.pbf file in the case that you need to deploy the OpenTripPlanner API.

### Input parameters:
1) Parameter P, which is the maximum number of facilities/depots to be selected out of the wider network of N facilities.

### Usage and overall outputs (based on entry file used):
1) weighted_p_median.py is Python script that includes most of the model logic, and is the entry point to the software. The results are i) the facilities to be selected are printed to console at the current version, ii) assignment of depots with no CS to depots with CS, iii) O-D matrices between depots. Results are pritned to console after execution.

## A figure of the CS-FLP with underlying components: 
<img src="https://user-images.githubusercontent.com/10188642/236616499-3e371eac-98aa-49f3-9343-b5129e470d63.png" width="600" height="400">

### Installation
To run the model you need to setup two environments:
1) Python 3.7 environment (e.g. based on Anaconda) and Python packages based on requirements.txt file,
2) Java 8 Runtime Environment in order to run OpenTripPlanner routing engine through the .bat file located in root_folder/opentripplanner.

### Development

Developed by the Inlecom LEAD team

### Support
Dimitris Rizopoulos, dimitris.rizopoulos@inlecomsystems.com
