import csv
def findstreet(search_street):
	with open('sweep.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			street = row[-4]
			if search_street == street:
				print "we found "+search_street+"!"
			else:
				print search_street+" not found.  Try another one!"
