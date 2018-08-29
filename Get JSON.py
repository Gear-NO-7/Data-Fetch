import csv, json
import os, sys
import requests

string = ""
for i in range(1, 29):
    if i < 10:
        string = "0" + str(i)
    else:
        string = str(i)
    fileName = '2018-08-' + string + '.json'
    webName = "https://pm25.lass-net.org/data/history-date.php?device_id=74DA38AF4812&date=2018-08-" + string
    with open(fileName, 'w') as outfile:
        response = requests.get("https://pm25.lass-net.org/data/history-date.php?device_id=74DA38AF4812&date=2018-08-01")
        response_dic = response.json()
        json.dump(response_dic, outfile)

