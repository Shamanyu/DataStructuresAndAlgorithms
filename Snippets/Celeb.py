import urllib
import json as m_json

celebrity = raw_input("Enter the name of the celebrity: ")
celebrity = urllib.urlencode({'q' : celebrity})
response = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + celebrity).read()
json = m_json.loads(response)
results = json['responseData']['results']
print results
