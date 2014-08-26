import urllib

c =["http://ueyqwueywqiu.com","http://www.stackoverflow.com","http://www.google.com","http://simile.mit.edu/crowbar/nothing_here.html","http://mucipilbuga.com"]
k = 0
for i in c:
	try:
		m =  urllib.urlopen(i).getcode() 
		print ("%s - " % i) 
		print m
	except IOError, e:
		print ("%s - " % i)
		print "Error"
