#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Module description: creates a list of problem locations including depot and clients locations

# extracts based on date provided
def main(depot_coordinates, clients_to_be_served):
    list_of_problem_locations = []
    list_of_problem_locations.append((depot_coordinates[0], depot_coordinates[1]))
    for row in clients_to_be_served:
        list_of_problem_locations.append((row[12], row[13]))

    return list_of_problem_locations

