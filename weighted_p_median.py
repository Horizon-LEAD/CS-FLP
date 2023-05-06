#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Module description: An implementation of a weight p median algorithm, solving the CS-FLP.

import random
from ortools.linear_solver import pywraplp

import os
import argparse

import read_file

from utilities.data_pre_processing import calculate_demand_per_depot
from utilities.data_pre_processing import calculate_weights
from routing import calculate_OD_matrix

def main():
    print("Data analysis started ..")
    parser = argparse.ArgumentParser(description="Solving the problem according to input parameters.")
    parser.add_argument('--deliveries_file', dest='deliveries_data_file', default='deliveries_data', help='Deliveries data or parcel data to be optimized.')
    # parser.add_argument('--output_directory', dest='output_directory', default='/', help='The output directory.')
    parser.add_argument('--depot_data_file', dest='depot_data_file', default='depot_data', help='Information about depot/store locations, etc.')
    args = parser.parse_args()

    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input")
    deliveries_data = read_file.read_file(base_dir, args.deliveries_data_file)
    depot_data = read_file.read_file(base_dir, args.depot_data_file)

    print("Reading data finished ..")
    print("Calculating O-D distances ..")

    num_facilities = len(depot_data)
    OD_distance_matrix, OD_travel_time_matrix = calculate_OD_matrix.main(depot_data)

    for row in OD_distance_matrix:
        print(row)

    for row in OD_travel_time_matrix:
        print(row)

    print("Calculating demand per depot ..")

    demand = calculate_demand_per_depot.main(depot_data, deliveries_data)

    print("Calculating weights ...")

    demand_weight_factors = calculate_weights.main(demand)
    # distance_weights = calculate_weights.main()
    # travel_time_weights = calculate_weights.main()

    print("Depots in the problem: ", [row[1] for row in depot_data])
    print("Total demand per depot: ", demand, " boxes.")
    print("Demand weight factors: ", demand_weight_factors)

    cost = OD_distance_matrix

    p = 5 # Only need to open one facility

    print("Starting FLP initialization and solution ..")

    # Initialize solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Initialize model
    # Define variables
    x = {}
    for i in range(num_facilities):
        for j in range(num_facilities):
            x[i, j] = solver.BoolVar('x[%d,%d]' % (i, j))

    y = {}
    for i in range(num_facilities):
        y[i] = solver.BoolVar('y[%d]' % i)

    # Define objective function
    # Switching in-between the two objective functions for the problem,
    # can take place by remove "*demand_weight_factors[i]" from line 82.
    objective = solver.Objective()
    for i in range(num_facilities):
        for j in range(num_facilities):
            objective.SetCoefficient(x[i, j], cost[i][j]*demand_weight_factors[i])
    objective.SetMinimization()

    # Define constraints
    for i in range(num_facilities):
        constraint = solver.Constraint(1, 1)
        for j in range(num_facilities):
            constraint.SetCoefficient(x[i, j], 1)

    constraint = solver.Constraint(0, p)
    for i in range(num_facilities):
        constraint.SetCoefficient(y[i], 1)

    for i in range(num_facilities):
        for j in range(num_facilities):
            constraint = solver.Constraint(-15000, 0)
            constraint.SetCoefficient(x[i, j], 1)
            constraint.SetCoefficient(y[j], -1)


    # Export model to LP format for debugging
    with open('printed_model.lp', 'w') as file:
        file.write(solver.ExportModelAsLpFormat(False))

    # Solve the problem
    status = solver.Solve()

    # Print the solution
    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', round(solver.Objective().Value()))
        for i in range(num_facilities):
            if y[i].solution_value() > 0:
                print("A facility is established at Location %s." % depot_data[i][1])
        for i in range(num_facilities):
            for j in range(num_facilities):
                if (x[i, j].solution_value() > 0):
                    print('- Facility %s is served by %s (demand = %d, cost = %d)' % (depot_data[i][1], depot_data[j][1], demand[i], cost[i][j]))
    else:
        print('The problem does not have an optimal solution.')

if __name__ == "__main__":
    main()