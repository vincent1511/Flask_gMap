# coding: utf-8
from tools import *
import requests
from flask import Flask, render_template,request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import json
import pickle
app = Flask(__name__, template_folder="templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "IzaSyDTauRCrxTy5zguKkjjsnH_jwOVkh40JhE"

# you can also pass key here
GoogleMaps(app, key="AIzaSyDTauRCrxTy5zguKkjjsnH_jwOVkh40JhE")
try:
    with open("marks.txt", "rb") as fp:   # Unpickling
        marks = pickle.load(fp)
except:
    marks = []
#marks = [[25.056075, 121.580203], [25.056075, 121.582203]]
data = dbRead("SELECT * FROM object")
@app.route("/")
def mapview():
    mymap = Map(
        identifier="view-side",  # for DOM element
        varname="mymap",  # for JS object name
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        varname="sndmap",
        lat=25.053868,
        lng=121.580122,
        markers={
            icons.dots.green: [(25.053868, 121.580122), (25.053868, 121.582000)],
            icons.dots.blue: [(37.4300, -122.1400, "Hello World")]
        }
    )

    trdmap = Map(
        identifier="trdmap",
        varname="trdmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': icons.alpha.B,
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "Hello I am <b style='color:green;'>GREEN</b>!"
            },
            {
                'icon': icons.dots.blue,
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "Hello I am <b style='color:blue;'>BLUE</b>!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'lat': 37.4500,
                'lng': -122.1350,
                'infobox': (
                    "Hello I am <b style='color:#ffcc00;'>OW</b>!"
                    "<h2>It is HTML title</h2>"
                    "<img src='//placehold.it/50'>"
                    "<br>Images allowed!"
                )
            }
        ]
    )

    clustermap = Map(
        identifier="clustermap",
        varname="clustermap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'lat': 37.4500,
                'lng': -122.1350
            },
            {
                'lat': 37.4400,
                'lng': -122.1350
            },
            {
                'lat': 37.4300,
                'lng': -122.1350
            },
            {
                'lat': 36.4200,
                'lng': -122.1350
            },
            {
                'lat': 36.4100,
                'lng': -121.1350
            }
        ],
        zoom=12,
        cluster=True
    )

    movingmap = Map(
        identifier="movingmap",
        varname="movingmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'lat': 37.4500,
                'lng': -122.1350
            }
        ],
        zoom=12
    )

    movingmarkers = [
        {
            'lat': 37.4400,
            'lng': -122.1350
        },
        {
            'lat': 37.4430,
            'lng': -122.1350
        },
        {
            'lat': 37.4450,
            'lng': -122.1350
        },
        {
            'lat': 37.4490,
            'lng': -122.1350
        }
    ]

    rectangle = {
        'stroke_color': '#0000FF',
        'stroke_opacity': .8,
        'stroke_weight': 5,
        'fill_color': '#FFFFFF',
        'fill_opacity': .1,
        'bounds': {
            'north': 33.685,
            'south': 33.671,
            'east': -116.234,
            'west': -116.251
        }
    }

    rectmap = Map(
        identifier="rectmap",
        varname="rectmap",
        lat=33.678,
        lng=-116.243,
        rectangles=[
            rectangle,
            [33.678, -116.243, 33.671, -116.234],
            (33.685, -116.251, 33.678, -116.243),
            [(33.679, -116.254), (33.678, -116.243)],
            ([33.689, -116.260], [33.685, -116.250]),
        ]
    )

    circle = {
        'stroke_color': '#FF00FF',
        'stroke_opacity': 1.0,
        'stroke_weight': 7,
        'fill_color': '#FFFFFF',
        'fill_opacity': .8,
        'center': {
                  'lat': 33.685,
                  'lng': -116.251
        },
        'radius': 2000,
    }

    circlemap = Map(
        identifier="circlemap",
        varname="circlemap",
        lat=33.678,
        lng=-116.243,
        circles=[
            circle,
            [33.685, -116.251, 1000],
            (33.685, -116.251, 1500),
        ]
    )

    polyline = {
        'stroke_color': '#0AB0DE',
        'stroke_opacity': 1.0,
        'stroke_weight': 3,
        'path': [{'lat': 33.678, 'lng': -116.243},
                 {'lat': 33.679, 'lng': -116.244},
                 {'lat': 33.680, 'lng': -116.250},
                 {'lat': 33.681, 'lng': -116.239},
                 {'lat': 33.678, 'lng': -116.243}]
    }

    path1 = [(33.665, -116.235), (33.666, -116.256),
             (33.667, -116.250), (33.668, -116.229)]

    path2 = ((33.659, -116.243), (33.660, -116.244),
             (33.649, -116.250), (33.644, -116.239))

    path3 = ([33.688, -116.243], [33.680, -116.244],
             [33.682, -116.250], [33.690, -116.239])

    path4 = [[33.690, -116.243], [33.691, -116.244],
             [33.692, -116.250], [33.693, -116.239]]

    plinemap = Map(
        identifier="plinemap",
        varname="plinemap",
        lat=33.678,
        lng=-116.243,
        polylines=[polyline, path1, path2, path3, path4]
    )

    polygon = {
        'stroke_color': '#0AB0DE',
        'stroke_opacity': 1.0,
        'stroke_weight': 3,
        'fill_color': '#ABC321',
        'fill_opacity': .5,
        'path': [{'lat': 33.678, 'lng': -116.243},
                 {'lat': 33.679, 'lng': -116.244},
                 {'lat': 33.680, 'lng': -116.250},
                 {'lat': 33.681, 'lng': -116.239},
                 {'lat': 33.678, 'lng': -116.243}]
    }

    pgonmap = Map(
        identifier="pgonmap",
        varname="pgonmap",
        lat=33.678,
        lng=-116.243,
        polygons=[polygon, path1, path2, path3, path4]
    )

    collapsible = Map(
        identifier="collapsible",
        varname="collapsible",
        lat=60.000025,
        lng=30.288809,
        zoom=13,
        collapsible=True
    )

    infoboxmap = Map(
        identifier="infoboxmap",
        zoom=12,
        lat=59.939012,
        lng=30.315707,
        markers=[{
            'lat': 59.939,
            'lng': 30.315,
            'infobox': 'This is a marker'
        }],
        circles=[{
            'stroke_color': '#FF00FF',
            'stroke_opacity': 1.0,
            'stroke_weight': 7,
            'fill_color': '#FF00FF',
            'fill_opacity': 0.2,
            'center': {
                'lat': 59.939,
                'lng': 30.3
            },
            'radius': 200,
            'infobox': "This is a circle"
        }],
        rectangles=[{
            'stroke_color': '#0000FF',
            'stroke_opacity': .8,
            'stroke_weight': 5,
            'fill_color': '#FFFFFF',
            'fill_opacity': .1,
            'bounds': {
                'north': 59.935,
                'south': 59.93,
                'east': 30.325,
                'west': 30.3,
            },
            'infobox': "This is a rectangle"
        }],
        polygons=[{
            'stroke_color': '#0AB0DE',
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': [
                [59.94, 30.318],
                [59.946, 30.325],
                [59.946, 30.34],
                [59.941, 30.35],
                [59.938, 30.33]
            ],
            'infobox': 'This is a polygon'
        }],
        polylines=[{
            'stroke_color': '#0AB0DE',
            'stroke_opacity': 1.0,
            'stroke_weight': 10,
            'path': [
                (59.941, 30.285),
                (59.951, 30.31),
                (59.95, 30.36),
                (59.938, 30.358)
            ],
            'infobox': 'This is a polyline'
        }]
    )

    return render_template(
        'example.html',
        mymap=mymap,
        sndmap=sndmap,
        trdmap=trdmap,
        rectmap=rectmap,
        circlemap=circlemap,
        plinemap=plinemap,
        pgonmap=pgonmap,
        clustermap=clustermap,
        movingmap=movingmap,
        movingmarkers=movingmarkers,
        collapsible=collapsible,
        infoboxmap=infoboxmap
    )
@app.route('/list',methods=['GET'])
def list_show():
    #global marks;
    #return render_template('list.html',marks = data)
    marks = []
    for cnt in range(len(data)):
        marks.append((data[cnt][7],data[cnt][8]))
    mark = tuple(marks)
    try:
        lat = marks[0][0]
        lng= marks[0][1]
    except:
        lat = 25.056075
        lng= 121.580203
    sndmap = Map(
        style= "height:700px;width:700px;margin:0;",
        zoom = 13,
        identifier="sndmap",
        lat= lat,
        lng=lng,
        markers={icons.dots.green: mark}
    )
    #return render_template('app.html', sndmap=sndmap)
    return render_template('list.html',marks = data, sndmap=sndmap)
@app.route('/list',methods=['POST'])
def list_get():
    global marks;
    SQL = 'SELECT * FROM object'
    area = request.form.get('check_area')
    floor = request.form.get('check_floor')
    price = request.form.get('check_price')
    size = request.form.get('check_size')
    if area == None and floor ==None and price == None and size == None:
        pass
    else:
        check = 0		
        SQL += " WHERE "
        if size != None:
            size_low =  request.form.get('size_low')			
            SQL += "size >= " + size_low 
            size_high =  request.form.get('size_high')			
            SQL += " and size <= " + size_high
            check = 1
        if price != None:
            if check == 1:
               SQL += " and "
            price_low =  request.form.get('price_low')			
            SQL += "price >= " + price_low 
            price_high =  request.form.get('price_high')			
            SQL += " and price <= " + price_high
            check = 1
        if area != None:
            if check == 1:
               SQL += " and "
            text_area =  request.form.get('text_area')			
            SQL += "area = " + '"' + text_area + '"'
            check = 1
        if floor != None:
            if check == 1:
               SQL += " and "
            text_floor =  request.form.get('text_floor')			
            SQL += "floor = " + text_floor 
    print SQL
    data = dbRead(SQL)
    marks = []
    for cnt in range(len(data)):
        marks.append((data[cnt][7],data[cnt][8]))
    mark = tuple(marks)
    try:
        lat = marks[0][0]
        lng= marks[0][1]
    except:
        lat = 25.056075
        lng= 121.580203
    sndmap = Map(
        style= "height:700px;width:700px;margin:0;",
        zoom = 13,
        identifier="sndmap",
        lat= lat,
        lng=lng,
        markers={icons.dots.green: mark}
    )
    #return render_template('app.html', sndmap=sndmap)
    return render_template('list.html',marks = data, sndmap=sndmap)
@app.route('/add',methods=['GET'])
def add_show():
    return render_template('add.html')
@app.route('/add',methods=['POST'])
def add():
    name = request.form.get('name').encode('utf-8')
    phone = request.form.get('phone').encode('utf-8')
    addr = request.form.get('addr').encode('utf-8')
    floor = request.form.get('floor')
    price = request.form.get('price')
    size = request.form.get('size')
    print type(name)
    SQL_WRITE = 'INSERT INTO object values("{}","{}","{}",{},{},{},{},{})'
    while True:
        a = getGeoForAddress_c(addr)
        if a.lng != None:
            break;
    dbWrite(SQL_WRITE.format(name,phone,addr,price,size,floor,a.lat,a.lng))
    return render_template('add.html')
@app.route('/app',methods=['GET'])
def mapview_1():
    global marks;
    mark = tuple(marks)
    lat = 25.056075
    lng= 121.580203
    sndmap = Map(
        style= "height:900px;width:900px;margin:0;",
        zoom = 16,
        identifier="sndmap",
        lat= lat,
        lng=lng,
        markers={icons.dots.green: mark,
                 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png': [(25.056075, 121.584203, "Hello World")]}
    )
    return render_template('app.html', sndmap=sndmap)
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
@app.route('/app',methods=['POST'])
def mapview_2():
    global marks;

    #x = request.form.get('text_1')
    #y = request.form.get('text_2')
    while True:
        data = getGeoForAddress(request.form.get('text_1'))
        if data != None:
            break;
    event = request.form.get('submit')
    print event
    if event == "addAddress":
        marks.append(data)
        with open("marks.txt", "wb") as fp:   #Pickling
            pickle.dump(marks, fp)
        lat = 25.056075
        lng= 121.580203

    elif event == "review":
        lat = data[0]
        lng = data[1]
    else:
        lat = 25.056075
        lng= 121.580203
    mark = tuple(marks)
    sndmap = Map(
        style= "height:900px;width:900px;margin:0;",
        identifier="sndmap",
        lat = lat,
        lng= lng,
        markers={icons.dots.green: mark,
                 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png': [(25.056075, 121.584203, "Hello World")]}
    )
    return render_template('app.html', sndmap=sndmap, marks = marks)



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, use_reloader=True)
