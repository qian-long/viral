import urllib
import json
import sys

def removeNonAscii(string):
  return "".join(i for i in string if ord(i)<128)

def get_coords(location_str):
  try:
    clean_location = urllib.quote_plus(removeNonAscii(location_str))
    sys.stderr.write(clean_location)
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % (clean_location)
    #print "location_str", location_str
    #print urllib.quote(location_str)
    response = urllib.urlopen(url)
    html = response.read()
    result = json.loads(html)
    
    if result[u'status'] == "OK":
      #array
      """
      addr_components = result[u'results'][0][u'types']
      for comp in addr_components:
        if comp == "point_of_interest":
          return None
      """
      return (result[u'results'][0][u'geometry'][u'location'][u'lat'], result[u'results'][0][u'geometry'][u'location'][u'lng'])
    return None
  except (KeyError):
    return None

def process_data(array):
  nocoord_count_pre = 0
  nocoord_count_post = 0
  coords = []
  for i in xrange(len(array)):
    if i % 500 == 0:
      sys.stderr.write("at: " + str(i) + "\n")
    tweet = array[i]
    location = tweet[u'loc']
    if tweet[u'lat'] == None:
      nocoord_count_pre += 1
      #coords_tup = get_coords(location)
      #coords.append((location, coords_tup))
      #if coords_tup != None:
      #  tweet[u'lat'] = coords_tup[0]
      #  tweet[u'long'] = coords_tup[1]
      #else:
      #  nocoord_count_post += 1
  print "//pre no coord count", nocoord_count_pre
  #print "//post no coord count", nocoord_count_post
  print "//total", len(array)
  return array
    
if __name__ == "__main__":
  filename = sys.argv[1]
  f = open(filename, 'r')
  data = json.load(f)
  result = process_data(data)
  #print result
