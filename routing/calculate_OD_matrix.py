#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Module description: Takes as input the depot coordinates and clients locations /
#                     and returns the OD matrix.

from routing import get_distance_OTP

def main(depot_data):

    list_of_problem_locations = []
    for row in depot_data:
        list_of_problem_locations.append((row[9], row[10]))

    OD_distance_matrix = []
    OD_travel_time_matrix = []
    for row in list_of_problem_locations:
        OD_distance_matrix_row = []
        OD_travel_time_matrix_row = []
        for column in list_of_problem_locations:
            OD_distance_matrix_row.append(get_distance_OTP.main(row, column)[0])
            OD_travel_time_matrix_row.append(get_distance_OTP.main(row, column)[1])
        OD_distance_matrix.append(OD_distance_matrix_row)
        OD_travel_time_matrix.append(OD_travel_time_matrix_row)

    return OD_distance_matrix, OD_travel_time_matrix
