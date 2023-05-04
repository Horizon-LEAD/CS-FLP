#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Module description: calculates weight

def main(values):
    total_demand = sum(values)
    weight_factor = [round(d / total_demand, 2) for d in values]

    return weight_factor

if __name__ == "__main__":
    main()
