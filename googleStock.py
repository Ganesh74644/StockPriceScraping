import urllib
import json
import time
"""import re


htmltext = urllib.urlopen("https://www.google.com/finance?q=NASDAQ%3AAAPL").read()
regex = '<span id="ref_[^.]*_l">(.+?)</span>'
pattern = re.compile(regex)
results = re.findall(pattern,htmltext)
print results
"""

"""htmltext  = urllib.urlopen("https://www.google.com/finance/getprices?q=AAPL&x=NASD&i=10&p=25m&f=c&df=cpct&auto=1&ts=1486403131325&ei=-7WYWMnnKZSGuQTqloPYDg").read()
print htmltext.split()[len(htmltext.split())-1]"""
symbolslist = open("/Users/jagdishkapkoti/Desktop/symbol.txt").read()
symbolslist = symbolslist.split()

for symbol in symbolslist:
	myfile = open("/Users/jagdishkapkoti/Desktop/StockData/"+symbol+".txt","w+")
	myfile.close()
	htmltext = urllib.urlopen("https://www.bloomberg.com/markets/chart/data/1D/"+symbol+":US")
	data = json.load(htmltext)
	datapoints = data["data_values"]
	myfile = open("/Users/jagdishkapkoti/Desktop/StockData/"+symbol+".txt","a")

	for point in datapoints:
		myfile.write(str(symbol+","+str(point[0])+","+str(point[1])+"\n"))
		#print "symbol",symbol,"price", point[1]
	time.sleep(5)
	myfile.close()








#htmltext = urllib.urlopen("https://www.bloomberg.com/markets/api/security/basic/AAPL%3AUS?locale=en")
	
#htmltext = urllib.urlopen("https://www.bloomberg.com/markets/api/security/basic/AAPL%3AUS?locale=en")




