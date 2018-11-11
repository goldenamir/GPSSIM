import googlemaps

# importing the required API key
api_key = 'AIzaSyBMpkGlUUfduWjK4vyIJwXIVSfwSE2RcSM'

gm = googlemaps.Client(key=api_key)
goecode_result = gm.geocode('kiruna')[0]
print(goecode_result)

