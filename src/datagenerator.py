#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import math
import argparse
import csv

# python main.py --vehno 10 --newcusno 15 --precusno 8 --rebno 3 --seed 10 --tempgap 0.5 --algo 'alns'

parser = argparse.ArgumentParser()



parser.add_argument('--vehno', nargs='+', type=int)

parser.add_argument('--newcusno', nargs='+', type=int)

parser.add_argument('--precusno', nargs='+', type=int)

parser.add_argument('--rebno', nargs='+', type=int)

parser.add_argument('--seed', nargs='+', type=int)

args = parser.parse_args()



cost = 0.125 # per unit time
beta = 0.1

# data generating
# input number of veh, cusnow, cuspre, reb, sta,seed
nv = args.vehno[0]
ncn = args.newcusno[0]
ncp = args.precusno[0]
nr = args.rebno[0]
nsta = 1
seed = args.seed[0]



# index of veh, cusnow, , cuspre,reb, sta
veh = [i for i in range(nv)]
cusnow = [i for i in range(nv,ncn+nv)]
cuspre = [i for i in range(ncn+nv, ncp+ncn+nv)]
reb = [i for i in range(ncp+ncn+nv,nr+ncp+ncn+nv)]
sta = [i for i in range(nr+ncp+ncn+nv,nsta+nr+ncp+ncn+nv)]

# related attributes
# customers on board of vehicles
V = {}
for i in veh:
    V[i] = 0

# initial routes
r = [[veh[i]] for i in range(len(veh))]

# coordinates
coordinates = []
for i in veh:
    coordinates.append([random.uniform(0, 10), random.uniform(0, 10)])
for i in cusnow:
    if i <= 0.5 * ncn:
        coordinates.append([random.uniform(5, 10), random.uniform(5, 10)])
    elif i <= 0.8 * ncn:
        coordinates.append([random.uniform(5, 10), random.uniform(0, 5)])
    elif i <= 0.9 * ncn:
        coordinates.append([random.uniform(0, 5), random.uniform(5, 10)])
    else:
        coordinates.append([random.uniform(0, 5), random.uniform(0, 5)])
for i in cuspre:
    coordinates.append([random.uniform(5, 10), random.uniform(0, 5)])
if nr>0:
    for i in reb[:2]:
        coordinates.append([random.uniform(5, 10), random.uniform(5, 10)])
    for i in [reb[2]]:
        coordinates.append([random.uniform(5, 10), random.uniform(0, 5)])
for i in sta:
    coordinates.append([0, 0])

# demand of rebalancing center
D = {}
if nr>0:
    D[reb[0]] = math.floor(0.25*ncn)
    D[reb[1]] = math.floor(0.25*ncn)
    D[reb[2]] = math.floor(0.2*ncn)

# transporting time
t = []
for i in range(len(coordinates)):
    temp = []
    for j in range(len(coordinates)):
        temp.append(math.dist(coordinates[i],coordinates[j])/0.6)
    t.append(temp)

# fare and rebalancing fare computation

fare = {}
for i in cusnow+cuspre:
    fare[i] = 1.62 * t[i][sta[0]]*0.6 * 1.6 + 0.74 * t[i][sta[0]] # price $1.56 per km, $1.56*0.6 = $0.936 per min
    if fare[i] < 8:
        fare[i]== 8
for j in reb:
    if D[j] == 0:
        fare[j] = 0
    else:
        fare[j] = (1.62 * t[j][sta[0]]*0.6 * 1.6 + 0.74 * t[j][sta[0]])*2


#requested arrival time
ra  = {} # everthing
rra = {} # routes
for i in veh:
    ra[i] = 50
    rra[i] = 50
for i in cusnow:
    ra[i] = random.randrange(30,50,10)
for i in cuspre:
    ra[i] = random.randrange(20,40,10)

# time table
timetable = [30,40,50]

with open('instances/V'+str(nv)+'-C'+str(ncn)+'-P'+str(ncp)+'-R3'+'-'+str(seed)+'.txt', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['Vehicle Capacity'])
    writer.writerow(V.values())
    writer.writerow(['Original Route'])
    writer.writerow(r)
    writer.writerow(['Coordinates'])
    writer.writerow(coordinates)
    writer.writerow(['Demand of Rebalancing Centers'])
    writer.writerow(D.values())
    writer.writerow(['Travel Time between Nodes'])
    writer.writerow(t)
    writer.writerow(['Fare'])
    writer.writerow(fare.values())
    writer.writerow(['Requested Arrival Time of Customers and Vehicles'])
    writer.writerow(ra.values())
    writer.writerow(['Requested Arrival Time of Routes'])
    writer.writerow(rra.values())
