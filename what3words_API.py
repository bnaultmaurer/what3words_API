import what3words
import pandas as pd
import numpy as np
import csv


# define API key
api_key = "JBY0UH4P"

input_file = 'mn_county_centroids.txt'
output_file ='mn_county_centroids_out.csv'

## connect to public API
geocoder = what3words.Geocoder(api_key)

# read in set of coordinates
df = pd.read_csv(input_file, sep = '\t', skiprows = 1, names = ('stand', 'long', 'lat'))
df['what3words'] = None

# iterate through values
for index, row in df.iterrows():
    #lat_long = str(df['lat'][index]) + ", " + str(df['long'][index])
    #print(lat_long)

    # convert coordinates to what3words
    res = geocoder.convert_to_3wa(what3words.Coordinates(df['lat'][index], df['long'][index]))
    df['what3words'][index] = res['words']
    #print(res['words'], df['what3words'][index])

# write dataframe to file
df.to_csv(output_file)
