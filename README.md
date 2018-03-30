1.Gmap use flask web framewrok
	data : 抓取測試資料
	getData.py : 抓取測試資料的程式
	app.py : flask 主程式
	agency.db : sqlite3 database
		格式：
		name TEXT,phone TEXT,addr TEXT,area TEXT,price INT,size REAL,floor INT,lat REAL,lng REAL
	tools.py
		dbWrite
		dbRead
		getGeoForAddress_c		
