import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://127.0.0.1:2225/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"

headers = {
    'Content-Type': "application/yang-data+json",
    'Accept': "application/yang-data+json",
    'Authorization': "Basic dmFncmFudDp2YWdyYW50",
    }

response = requests.request("GET", url, headers=headers, verify=False)

print(response.text)