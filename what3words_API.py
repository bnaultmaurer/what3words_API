import what3words

# define API key
api_key = "JBY0UH4P"

## connect to public API
geocoder = what3words.Geocoder(api_key)

## convert coordinates to what3words
#res = geocoder.convert_to_3wa(what3words.Coordinates(46.25, -93.25))
#print(res['words'])

# read in set of coordinates
