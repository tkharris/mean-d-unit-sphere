#!/usr/bin/env python

import numpy as np
from scipy import stats
import time

np.random.seed(int(time.time()))

def def_point_in_unit_spheroid(d):
    def point_in_unit_spheroid(n=1):
        while n>0:
            v = np.random.random_sample(d)*2-1
            if v.dot(v) <= 1:
                n = n-1
                yield v
    return point_in_unit_spheroid

def point_pair_distance(source, n=1):
    for _ in range(n):
        p1, p2 = source(2)
        yield np.linalg.norm(p2-p1)

n = 100
hyp_mean = 36/35

# we want to be 1/1000 confident that our hypothesized mean is no more than 0.01 off
conf = 0.999
interval = 0.01 * 2
while True:
    print(f'for N={n}')

    d3_data = np.empty(n)
    for i, el in enumerate(point_pair_distance(def_point_in_unit_spheroid(3), n)): d3_data[i] = el
    sample_mean, sample_standard_error = d3_data.mean(), stats.sem(d3_data)
    conf_low, conf_hi = stats.t.interval(conf, n-1, sample_mean, sample_standard_error)

    print(f'd3 mean: {np.mean(d3_data)}')
    print(f'conf_int: {conf_low}, {conf_hi}')

    if hyp_mean < conf_low or hyp_mean > conf_hi:
        print("rejected!")
        break
    elif conf_hi - conf_low < interval:
        print("accepted!")
        break
    else:
        print(f'interval is: {conf_hi - conf_low}, still testing...')

    n *= 2
