# Instance Generator
This repository contains a data generator for the instances of the order dispatching and vacant vehicle rebalancing in first-mile ride-sharing problem discussed in the article Ye, J., Pantuso, G., Pisinger, D.. "Adaptive Large Neighborhood Search for Order Dispatching and
Vacant Vehicle Rebalancing in First-mile Ride-sharing Problem". The instance generator is written in Python and is thoroughly described in the article. Particularly this repository contains two folders: The Src folder, which contains the Python code, and the Instances folder, which contains the data files processed by the code to generate instances.

# How to generate instances
In order to generate instances the code accepts the following command line arguments
<ul>
  <li>-vehno the number of vehicles (required)</li>
  <li>-newcusno the number of new customers (required)</li>
  <li>-precusno the number of previous customers</li>
  <li>-rebno the number of rebalancing centers (required)</li>
  <li>-seed the seed of generating random instances(required)</li>
</ul>


# Example usage

<code>python datagenerator.py --vehno 150 --newcusno 300 --precusno 75 --rebno 3 --seed 1</code>
creates an instance with 150 vehicles, 300 new customers, 75 previous customers, 3 rebalancing centers under random seed 1

The user can extend and modify the code to export instances information as required.

# Instances

This repository contains 10 instances, V20-C40-P10-R3, V30-C60-P15-R3, V40-C80-P30-R3, V50-C100-P45-R3, V100-C200-P50-R3, V150-C300-P75-R3, V50-C150-P45-R3, V100-C300-P50-R3, V150-C450-P75-R3, V200-C600-P100-R3. In addition, the instances are generated with random seed = 1. The files are explained below.

From the first line to the last line, each line contains:
<ul>
  <li>Vehicle Capacity (Name)</li>
  <li>Vehicle Capacity (Values)</li>
  <li>Original Route (Name)</li>
  <li>Original Route (Values)</li>
  <li>Coordinates (Name)</li>
  <li>Coordinates (Values)</li>
  <li>Demand of Rebalancing Centers (Name)</li>
  <li>Demand of Rebalancing Centers (Values)</li>
  <li>Travel Time between Nodes (Name)</li>
  <li>Travel Time between Nodes (Values)</li>
  <li>Fare (Name)</li>
  <li>Fare (Values)</li>
  <li>Requested Arrival Time of Customers and Vehicles (Name)</li>
  <li>Requested Arrival Time of Customers and Vehicles (Values)</li>
  <li>Requested Arrival Time of Routes (Name)</li>
  <li>Requested Arrival Time of Routes (Values)</li>
</ul>
