import what3words
import pandas as pd
import numpy as np
import csv


# define API key
api_key = "JBY0UH4P"

## connect to public API
geocoder = what3words.Geocoder(api_key)

# read in set of coordinates
df = pd.read_csv('mn_county_centroids.txt', sep = '\t', skiprows = 1, names = ('stand', 'long', 'lat'))

# iterate through values
for index, row in df.head(5).iterrows():
    lat_long = str(df['lat'][index]) + ", " + str(df['long'][index])
    print(lat_long)



## convert coordinates to what3words
#res = geocoder.convert_to_3wa(what3words.Coordinates(46.25, -93.25))
#print(res['words'])
