#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Module description: Executes OTP query and get back distance between two points.

import datetime, json, codecs

from routing.Config import Config
from routing import haversine
from urllib.request import urlopen

reader = codecs.getreader("utf-8")

def main(point_1_coordinates, point_2_coordinates):
    distance = 0
    now = datetime.datetime.now()
    current_date = now.strftime("%m-%d-%Y")
    current_time = now.strftime("%H:%M")

    # unpacking lat, lons since OTP and haversine module receive seperately
    lat_1 = point_1_coordinates[0]
    lon_1 = point_1_coordinates[1]
    lat_2 = point_2_coordinates[0]
    lon_2 = point_2_coordinates[1]
    
    url = Config.get('OTP_URL', 'http://localhost:8080/otp/')
    string = str(url + 'routers/default/plan?fromPlace=' +
                str(lat_1) + ',' + str(lon_1) + '&toPlace=' +
                str(lat_2) + ',' + str(lon_2) +
                '&time=' + current_time + '&date=' + current_date + '&mode=CAR&arriveBy=false')

    response = urlopen(string, timeout=int(Config.get('REQUEST_TIMEOUT', 60)))
    obj = json.load(reader(response))

    # Error handling for OTP query
    OTP_result_1 = obj.get('plan')
    OTP_result_2 = False
    if OTP_result_1:
        OTP_result_2 = OTP_result_1.get('itineraries')
    if OTP_result_1 and OTP_result_2:
        for leg in obj['plan']['itineraries'][0]['legs']:
            distance += leg['distance']
        duration = (obj['plan']['itineraries'][0]
                    ['duration']) / 60  # In minutes
    else:
        distance = int(haversine.main(
                    float(lat_1), float(lon_1), 
                    float(lat_2), float(lon_2)))
        duration = distance / 330

    return int(distance), int(duration)

if __name__ == "__main__":
    main([41.137404, -8.63816], [41.216732, -8.601842])
