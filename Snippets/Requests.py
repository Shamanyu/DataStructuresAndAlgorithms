import requests

r=requests.get("http://192.168.3.117:8086/query?db=GreyOrange&q=select%20*%20from%20put%20where%20installation_id='shamanyu'%20order%20by%20time%20desc%20")
print r.text
