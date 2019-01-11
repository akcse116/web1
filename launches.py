import urllib.request
import requests
import json
import datetime


url1 = "https://api.spacexdata.com/v3/launches/upcoming?limit=10"
url2 = "https://api.spacexdata.com/v3/launches/past"
url3 = "https://api.spacexdata.com/v3/launches/past?limit=10"
url4 = "https://api.spacexdata.com/v3/launches/latest"


def get_launch_data(url):
    launches = []
    a = urllib.request.urlopen(url)
    b = a.read().decode()
    c = json.loads(b)
    
    for mission in c:
        temp = []
        if mission["flight_number"] == None:
            temp.append('undisclosed')
        else:
            temp.append(mission["flight_number"])
        
        if mission["mission_name"] == None:
            temp.append('undisclosed')
        else:
            temp.append(mission["mission_name"])
        
        if mission["launch_date_utc"] == None:
            temp.append('undisclosed')
        else:
            time = datetime.datetime.strptime(mission["launch_date_utc"], "%Y-%m-%dT%H:%M:%S.%fZ")
            temp.append(time.strftime("%a %x %X"))
        
        if mission["rocket"]["rocket_name"] == None:
            temp.append('undisclosed')
        else:
            temp.append(mission["rocket"]["rocket_name"])
        
        if mission["rocket"]["second_stage"]["payloads"][0]["payload_type"] == None:
            temp.append('undisclosed')
        else:
            temp.append(mission["rocket"]["second_stage"]["payloads"][0]["payload_type"])
        
        if mission["rocket"]["second_stage"]["payloads"][0]["payload_mass_kg"] == None:
            temp.append('undisclosed')
        else:
            temp.append(str(mission["rocket"]["second_stage"]["payloads"][0]["payload_mass_kg"]) + ' kg')
        
        if mission["rocket"]["second_stage"]["payloads"][0]["customers"] == None:
            temp.append('undisclosed')
        else:
            temp.append(mission["rocket"]["second_stage"]["payloads"][0]["customers"])
        
        if mission["launch_site"]["site_name_long"] == None:
            temp.append('undisclosed')
        else:
            temp.append(mission["launch_site"]["site_name_long"])
        
        if mission["links"]["video_link"] == None:
            temp.append('--')
        else:
            link = mission["links"]["video_link"]
            temp.append("<a href=\"" + link + "\">Link</a>")
        
        launches.append(temp)
    return json.dumps(launches)


def get_launch_data_past_sort(url):
    launches = []
    a = urllib.request.urlopen(url)
    b = a.read().decode()
    c = json.loads(b)
    
    for mission in c:
        if mission["flight_number"] > (len(c) - 10):
            temp = []
            if mission["flight_number"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["flight_number"])
            
            if mission["mission_name"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["mission_name"])
            
            if mission["launch_date_utc"] == None:
                temp.append('undisclosed')
            else:
                time = datetime.datetime.strptime(mission["launch_date_utc"], "%Y-%m-%dT%H:%M:%S.%fZ")
                temp.append(time.strftime("%a %x %X"))
            
            if mission["rocket"]["rocket_name"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["rocket"]["rocket_name"])
            
            if mission["rocket"]["second_stage"]["payloads"][0]["payload_type"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["rocket"]["second_stage"]["payloads"][0]["payload_type"])
            
            if mission["rocket"]["second_stage"]["payloads"][0]["payload_mass_kg"] == None:
                temp.append('undisclosed')
            else:
                temp.append(str(mission["rocket"]["second_stage"]["payloads"][0]["payload_mass_kg"]) + ' kg')
            
            if mission["rocket"]["second_stage"]["payloads"][0]["customers"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["rocket"]["second_stage"]["payloads"][0]["customers"])
            
            if mission["launch_site"]["site_name_long"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["launch_site"]["site_name_long"])
            
            if mission["links"]["video_link"] == None:
                temp.append('--')
            else:
                link = mission["links"]["video_link"]
                temp.append("<a href=\"" + link + "\">Link</a>")
            
            launches.append(temp)
    launches.reverse()
    return json.dumps(launches)


def get_latest_launch_data(url):
    launches = []
    temp = []
    a = urllib.request.urlopen(url)
    b = a.read().decode()
    c = json.loads(b)
    if c["flight_number"] == None:
            temp.append('undisclosed')
    else:
        temp.append(c["flight_number"])
        
    if c["mission_name"] == None:
            temp.append('undisclosed')
    else:
        temp.append(c["mission_name"])
    
    if c["launch_date_utc"] == None:
            temp.append('undisclosed')
    else:
        time = datetime.datetime.strptime(c["launch_date_utc"], "%Y-%m-%dT%H:%M:%S.%fZ")
        temp.append(time.strftime("%a %x %X"))
    
    if c["rocket"]["rocket_name"] == None:
        temp.append('undisclosed')
    else:
        temp.append(c["rocket"]["rocket_name"])
    
    if c["rocket"]["second_stage"]["payloads"][0]["payload_type"] == None:
            temp.append('undisclosed')
    else:
        temp.append(c["rocket"]["second_stage"]["payloads"][0]["payload_type"])
    
    if c["rocket"]["second_stage"]["payloads"][0]["payload_mass_kg"] == None:
            temp.append('undisclosed')
    else:
        temp.append(str(c["rocket"]["second_stage"]["payloads"][0]["payload_mass_kg"]) + ' kg')
    
    if c["rocket"]["second_stage"]["payloads"][0]["customers"] == None:
            temp.append('undisclosed')
    else:
        temp.append(c["rocket"]["second_stage"]["payloads"][0]["customers"])
    
    if c["launch_site"]["site_name_long"] == None:
            temp.append('undisclosed')
    else:
        temp.append(c["launch_site"]["site_name_long"])
    
    if c["links"]["video_link"] == None:
        temp.append('--')
    else:
        link = c["links"]["video_link"]
        temp.append("<a href=\"" + link + "\">Link</a>")
    
    launches.append(temp)
    return json.dumps(launches)


def get_failed_launches(url):
    launches = []
    a = urllib.request.urlopen(url)
    b = a.read().decode()
    c = json.loads(b)
    
    for mission in c:
        if mission["launch_success"] == False:
            temp = []
            if mission["flight_number"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["flight_number"])
            
            if mission["mission_name"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["mission_name"])
            
            if mission["launch_date_utc"] == None:
                temp.append('undisclosed')
            else:
                time = datetime.datetime.strptime(mission["launch_date_utc"], "%Y-%m-%dT%H:%M:%S.%fZ")
                temp.append(time.strftime("%a %x %X"))
            
            if mission["rocket"]["rocket_name"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["rocket"]["rocket_name"])
            
            if mission["rocket"]["second_stage"]["payloads"][0]["payload_type"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["rocket"]["second_stage"]["payloads"][0]["payload_type"])
            
            if mission["rocket"]["second_stage"]["payloads"][0]["payload_mass_kg"] == None:
                temp.append('undisclosed')
            else:
                temp.append(str(mission["rocket"]["second_stage"]["payloads"][0]["payload_mass_kg"]) + ' kg')
            
            if mission["rocket"]["second_stage"]["payloads"][0]["customers"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["rocket"]["second_stage"]["payloads"][0]["customers"])
            
            if mission["launch_site"]["site_name_long"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["launch_site"]["site_name_long"])
            
            if mission["details"] == None:
                temp.append('undisclosed')
            else:
                temp.append(mission["details"])
            
            if mission["links"]["video_link"] == None:
                temp.append('--')
            else:
                link = mission["links"]["video_link"]
                temp.append("<a href=\"" + link + "\">Link</a>")
            
            launches.append(temp)
    return json.dumps(launches)


def launch_locations(url):
    atoll = 0
    canaveral = 0
    vandenberg = 0
    kennedy = 0
    a = urllib.request.urlopen(url)
    b = a.read().decode()
    c = json.loads(b)
    for mission in c:
        if mission["launch_site"]["site_name"] == 'Kwajalein Atoll':
            atoll += 1
        if mission["launch_site"]["site_name"] == 'CCAFS SLC 40':
            canaveral += 1
        if mission["launch_site"]["site_name"] == 'VAFB SLC 4E':
            vandenberg += 1
        if mission["launch_site"]["site_name"] == 'KSC LC 39A':
            kennedy += 1
    return json.dumps([atoll, canaveral, vandenberg, kennedy])


print(get_latest_launch_data(url4))