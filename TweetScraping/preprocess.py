import urllib2
import json
response = urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=Chicago&sensor=false")
html = response.read()
result = json.loads(html)
if result[u'status'] == "OK":
  print (result[u'results'][0][u'geometry'][u'location'][u'lat'], result[u'results'][0][u'geometry'][u'location'][u'lng'])
