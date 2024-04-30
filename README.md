# Bus-Service-Planner
[![Pylint Score](https://img.shields.io/badge/pylint_score-10-green.svg)](https://github.com/Phantawat/Bus-Service-Planner)

## Summary
The Kasetsart University Shuttle Bus Service Route Planner is a project aimed at providing students and staff with an efficient way to navigate the campus using the university's shuttle bus service. The application utilizes graph theory algorithms to compute optimal bus routes and schedules, helping users reach their destinations quickly and conveniently.

## Description
This project aims to develop a comprehensive Shuttle Bus Service Route Planner for Kasetsart University, integrating graph theory algorithms to provide users with optimal bus routes and schedules within the campus. The application allows users to select a starting point and destination, computes the shortest route using graph vertices, and displays the route on the user interface. In case there are multiple routes available, the application automatically selects the shortest route by distance.

## Main Features
Compute the Shortest Route: Utilizes graph theory algorithms to compute the shortest route between selected starting point and destination.
Show Shortest Route on Display: Displays the shortest route on the user interface for easy navigation.
User Input: Allows users to select the route, starting point, and destination interactively.
Distance Calculation: Displays the distance between two points to provide users with additional information.
Graph Visualization: Provides visualization of data correlations, helping users understand the bus service better.
Data Used
The project utilizes the KU-Transportation dataset, which includes information about bus routes, shuttle bus lines, and bus stops. The dataset contains numerical attributes that are used for descriptive statistics and correlation analysis.

## Dataset Information:

Shuttle Bus Lines: 4 lines, but only 3 lines are used depending on the current situation.
Bus Stops: Compose of 3 shuttle bus lines, with Line 1 containing 23 stops, Line 3 containing 25 stops, and Special Line containing 3 stops.
Dataset Source: Kasetsart University Car Service Routes

Columns Used for Analysis:

Distance for Line 1 (Km)
Distance for Line 3 (Km)
Distance for Special Line (Km)
Distance between 2 Stations (Km)
Time Between 2 Station Line 1 (mins)
