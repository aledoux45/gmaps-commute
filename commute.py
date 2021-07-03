"""
This script uses the GoogleMaps API to return the time it takes to go from 
point A to point B if leaving now
"""

import googlemaps
from datetime import datetime
import argparse
import csv

output_file = "data/times.csv"

# Parse input arguments
parser = argparse.ArgumentParser()

parser.add_argument('--pointA', help='Point A address')
parser.add_argument('--pointB', help='Point B address')
parser.add_argument('--mode', default='driving', help='Mode of Transportation')
parser.add_argument('--APIkey', help='GoogleMaps API Key')

args = parser.parse_args()

assert args.mode in ["driving", "walking", "bicycling", "transit"], "Mode of transportation must be one of: driving, walking, bicycling, transit"

# Start Gmaps client
gmaps = googlemaps.Client(key=args.APIkey)

# Request directions
now = datetime.now()
directions_result = gmaps.directions(args.pointA,
                                     args.pointB,
                                     mode="driving", # walking, bicycling, transit
                                     departure_time=now)

# Return the time in seconds
commute = directions_result[0]['legs'][0]['duration']['value']

# Write row in csv file
with open(output_file, 'a+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([now, commute])
