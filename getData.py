#coding:utf-8
from bs4 import BeautifulSoup
from tools import *
f = open("data","r")
soup = BeautifulSoup(f.read(),'lxml')
tab = soup.select('.lightBox')
name_tab = soup.select('em')
tprice = soup.select('.price')
addr = []
price = []
size = []
floor = []
name = []
for cnt in range(37,len(name_tab),4):
	print cnt,name_tab[cnt].text
	name.append(name_tab[cnt].text)
for cnt in range(len(tab)):
		
	_addr = tab[cnt].select('em')
	for addrCnt in range(len(_addr)):
		print _addr[addrCnt].text
		addr.append(_addr[addrCnt].text)
	area = tab[cnt].text.split('|')
	try:
		#print area[1].replace(" ","").replace("\n",'').replace(u"坪",""),
		size.append(float(area[1].replace(" ","").replace("\n",'').replace(u"坪","")))
		#print area[2].split("/")[1].replace(" ","").replace("\n",''),
		floor.append(int(area[2].split("/")[1].replace(" ","").replace("\n",'')))
	except:
		pass
		
		
	#print 

	#print cnt,tab[cnt]
print len(tprice)
for cnt in range(1,len(tprice)):
	print cnt,tprice[cnt].text.replace(u'元/月','').replace(',','').replace(" ","").replace("\n",'')
	price.append(int(tprice[cnt].text.replace(u'元/月','').replace(',','').replace(" ","").replace("\n",'')))

SQL_WRITE = 'INSERT INTO object values("{}","{}","{}","{}",{},{},{},{},{})'
for i in range(len(addr)):
	print addr[i].encode('utf-8'),
	print price[i],
	print int(size[i]),
	print floor[i]
	while True:
		a = getGeoForAddress_c(addr[i])
		if a.lng != None:
			break;
	dbWrite(SQL_WRITE.format(name[i].encode('utf-8'),"0933213234",addr[i].encode('utf-8'),a.area,price[i],size[i],floor[i],a.lat,a.lng))
