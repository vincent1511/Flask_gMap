#coding:utf-8
import sqlite3
import requests
import json
def dbRead(sql):
    try:
        db = sqlite3.connect("agency.db")
    except :
        print "Error : "
    cursor = db.cursor()
    cursor.execute(sql)
    lens = len(cursor.description)
    tmp1 = []
    results = []
    for row in cursor:
        for i in range(lens):
            tmp1.append(row[i])

        results.append(tmp1)
        tmp1 = []
    db.close()
    return results
def dbWrite(sql):
    try:
        db = sqlite3.connect("agency.db")
    except :
        print "Error : " 
    cursor = db.cursor()
    try:
        n = cursor.execute(sql)
    except:
        print 'write err'
        pass
    db.commit() #提交操作结果
def getGeoForAddress(address):
    #address = "台北市內湖區新明路"
    URL = "http://maps.googleapis.com/maps/api/geocode/json?address=" + address
    #中文url需要转码才能识别
    res = requests.get(URL)
    responseJson = json.loads(res.text)

    try:
        lat = responseJson.get('results')[0]['geometry']['location']['lat']
        lng = responseJson.get('results')[0]['geometry']['location']['lng']
    except:
        return None
    #print(address + ': %f, %f'  %(lat, lng))
    print type(lat)
    return [lat, lng]

class getGeoForAddress_c:
    def __init__(self,address):
        URL = "http://maps.googleapis.com/maps/api/geocode/json?address=" + address
        headers = {'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3'}
        res = requests.get(URL, headers=headers)
        responseJson = json.loads(res.text)
        #print responseJson.get('results')[0]['geometry']['location']['lat']
        #print responseJson.get('results')[0]['geometry']['location']['lng']
        #print responseJson.get('results')[0]['formatted_address']
        try:
            self.lat = responseJson.get('results')[0]['geometry']['location']['lat']
            self.lng = responseJson.get('results')[0]['geometry']['location']['lng']
            self.addr =responseJson.get('results')[0]['formatted_address'].encode('utf-8')
            self.area =responseJson.get('results')[0]['address_components'][1]['long_name'].encode('utf-8')
            if self.area.find("區") == -1:
                self.area =responseJson.get('results')[0]['address_components'][2]['long_name'].encode('utf-8')
    	except:
            self.lat = None
            self.lng = None
            self.addr = None
            self.area = None
            print "fail:"
    #print(address + ': %f, %f'  %(lat, lng))
