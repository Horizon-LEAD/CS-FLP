#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Module description: calculates demand per depot

def main(depot_data, deliveries_data):
    demand_per_depot = []
    for depot in depot_data:
        sum_depot_demand = 0
        for delivery in deliveries_data:
            if depot[0] == delivery[8]:
                sum_depot_demand += delivery[18]
        demand_per_depot.append(sum_depot_demand)

    return demand_per_depot

if __name__ == "__main__":
    main()
