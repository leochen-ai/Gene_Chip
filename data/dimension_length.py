def for_length(filename):
	f=open(filename,'r')
	a=f.readline()
	print len(a.split())
for_length("processedData_0.85.txt")
for_length("finalData.txt")