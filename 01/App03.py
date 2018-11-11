# Importing required libraries
import math

#Creating a class for changing the coordination based on latLon coordinate to decimal degrees

class Coord:

    def __init__(self, lat,lon):
        self.latdeg = lat
        self.longdeg = lon

    def __repr__(self):      #__repr__ should return a printable representation of the object, most likely one of the ways possible to create this object. 
        return "%f, %f" %(self.latdeg, self.longdeg)

    def __str__(self):       # Converting to Str format
        return repr(self)

    def __getattr__(self,name):   #Called when an attribute lookup has not found the attribute in the usual places (i.e. it is not an instance attribute nor is it found in the class tree for self).
        if name == "lon":
            return math.radians(self.londeg)
        elif name == "lat":
            return math.radians(self.latdeg)
        else:
            raise AttributeError



def haversine(start, end):
        """
        Implementation of the haversine formula that calculates the 
        angle between two point on a sphere. This returns the value in radians
        which then needs to be multiplied by the radius of the earth to get 
        the actual distance.
        It was inspired by the implementation that should be found here:
        http://gorny.edu.pl/haversine.py
        """

        start_lat = start.lat
        start_lon = start.lon
        end_lat = end.lat
        end_lon = end.lon

        d_lat = end_lat - start_lat
        d_lon = end_lon - start_lon

        a = (math.sin(d_lat/2)**2) + math.cos(start_lat) * math.cos(end_lat)\
                * (math.sin(d_lon/2)**2)
        c = 2 * math.asin(math.sqrt(a))

        return c
    
class SegmentIter:
    def __init__(self, start, end, speed):
        self.start = start
        self.end = end
        self.speed = speed

        self.d = haversine(start,end)

        self.distance = self.d * 637100
        self.count = 0

        time = self.distance / (self.speed/3.6)
        self.step = 1/time
        
