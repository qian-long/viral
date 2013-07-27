import json
import sys

def removeNonAscii(string):
  if string == "" or string == None:
    return ""
  return "".join(i for i in string if ord(i)<128)

def main(data):
  output = []
  for tweet in data:
    model = {}
    if (tweet[u'lat'] != None and tweet[u'lat']):
      model["time"] = tweet[u'time']
      model["lat"] = tweet[u'lat']
      model["long"] = tweet[u'long'] 
      output.append(model)
  return output

if __name__ == "__main__":

  filename = sys.argv[1]
  count = sys.argv[2]
  f = open(filename, 'r').readline()
  with open(filename, 'r') as input:
    data = json.load(input)
    print "var data" + count + "=", json.dumps(main(data))
 
