import os, re, json, sys

# there exists different key names for different data source
KEYS_PM2_5 = [ 's_d0', 'pm25', 'PM2_5' ]
KEYS_PM10 = [ 's_d1', 'PM10' ]
KEYS_TEMP = [ 's_t0', 's_t4', 'Temperature', 'temperature']
KEYS_HUMD = [ 's_h0', 's_h4', 'Humidity', 'humidity']
KEYS_ID = [ 'device_id', 'SiteID' ]

def retrieveValue( data, KEYS ):
    for KEY in KEYS:
        try:
            return str( data[ KEY ] )
        except:
            pass
    return  'NULL'

string = ''
for i in range(1, 29):
    if i < 10:
        string = '0' + str(i)
    else:
        string = str(i)
    resourceFile = 'JSON/2018-08-' + string + '.json'
    inputFile = 'CSV/2018-08-' + string + '.csv'
    with open(resourceFile, 'r') as infile:
        with open(inputFile, 'w') as outfile:
            header = 'app,date,deviceID,fmt_opt,gps_alt,gps_fix,gps_lat,gps_lon,gps_num,s_0,s_1,s_2,s_3,PM2_5,PM10,s_d2,Humidity,Temperature,tick,time,timestamp,ver_app,ver_format'
            outfile.write(header)
            outfile.write('\n') 
            sourcefile = infile.read()
            dict_data = json.loads(sourcefile)
            for data in dict_data['feeds'][0]['AirBox']:
                for dt in data.values():
                    gps_num = retrieveValue(dt, ['gps_num'])
                    app = retrieveValue(dt, ['app'])
                    PM10 = retrieveValue(dt, KEYS_PM10)
                    fmt_opt = retrieveValue(dt, ['fmt_opt'])
                    s_d2 = retrieveValue(dt, ['s_d2'])
                    PM2_5 = retrieveValue(dt, KEYS_PM2_5)
                    gps_alt = retrieveValue(dt, ['gps_alt'])
                    Humidity = retrieveValue(dt, KEYS_HUMD)
                    gps_fix = retrieveValue(dt, ['gps_fix'])
                    ver_app = retrieveValue(dt, ['ver_app'])
                    gps_lat = retrieveValue(dt, ['gps_lat'])
                    Temperature = retrieveValue(dt, KEYS_TEMP)
                    timestamp = retrieveValue(dt, ['timestamp'])
                    gps_lon = retrieveValue(dt, ['gps_lon'])
                    date = retrieveValue(dt, ['date'])
                    tick = retrieveValue(dt, ['tick'])
                    deviceID = retrieveValue(dt, KEYS_ID)
                    s_1 = retrieveValue(dt, ['s_1'])
                    s_0 = retrieveValue(dt, ['s_0'])
                    s_3 = retrieveValue(dt, ['s_3'])
                    s_2 = retrieveValue(dt, ['s_2'])
                    ver_format = retrieveValue(dt, ['ver_format'])
                    time = retrieveValue(dt, ['time'])

                    row = app + ',' + date + ',' + deviceID + ',' + fmt_opt + ',' + gps_alt + ',' + gps_fix + ',' + gps_lat + ',' + gps_lon + ',' + gps_num + ',' + s_0 + ',' + s_1 + ',' + s_2 + ',' + s_3 + ',' + PM2_5 + ',' + PM10 + ',' + s_d2 + ',' + Humidity + ',' + Temperature + ',' + tick + ',' + time + ',' + timestamp + ',' + ver_app + ',' + ver_format
                    outfile.write(str(row))
                    outfile.write('\n')
