import json
import sys

def removeNonAscii(string):
  if string == "" or string == None:
    return ""
  return "".join(i for i in string if ord(i)<128)

def main(data, counter):
  output = []
  pk = counter
  for tweet in data:
    model = {}
    model["model"] = "tweetmap.tweet"
    model["pk"] = pk
    model["fields"] = {}
    model["fields"]["location"] = removeNonAscii(tweet[u'loc'])
    model["fields"]["text"] = removeNonAscii(tweet[u'text'])
    model["fields"]["tweet_id"] = tweet[u'ID']
    model["fields"]["timestamp"] = tweet[u'time']
    model["fields"]["lat"] = tweet[u'lat']
    model["fields"]["lng"] = tweet[u'long']
    pk = pk + 1
    output.append(model)
  return output

if __name__ == "__main__":

  filename = sys.argv[1]
  counter = int(sys.argv[2])
  f = open(filename, 'r').readline()
  #print removeNonAscii(f)
  #data = json.loads(removeNonAscii(f))
  #print json.dumps(main(data, counter))
  with open(filename, 'r') as input:
    data = json.load(input)
    print json.dumps(main(data, counter))
     
