import csv
district = []
with open('sweep.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		if reader.line_num == 1:
			continue
		neighborhood = row[-2]
		if neighborhood not in district:
			district.append(neighborhood)

print "found {} neighborhoods".format(len(district))
print sorted(district)

#when cleanest?

monday = 0
tuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0
sunday = 0




with open('sweep.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		day_of_week = row['WEE']
		if day_of_week == 'Mon':
			monday +=1
		if day_of_week == 'Tues':
			tuesday += 1
		if day_of_week == 'Wed':
			wednesday += 1
		if day_of_week == 'Thu':
			thursday += 1
		if day_of_week == 'Fri':
			friday += 1
		if day_of_week == 'Sat':
			saturday += 1
		if day_of_week == 'Sun':
			sunday += 1

	most_sweeps = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
	most_sweeps_of_all=max(most_sweeps)

	print '{} streets are swept on Mondays'.format(monday)
	print '{} streets are swept on Tuesdays'.format(tuesday)
	print '{} streets are swept on Wednesdays'.format(wednesday)
	print '{} streets are swept on Thursdays'.format(thursday)
	print '{} streets are swept on Fridays'.format(friday)
	print '{} streets are swept on Saturdays'.format(saturday)
	print '{} streets are swept on Sundays'.format(sunday)

	print 'BUT the most sweeps on any day is {}'.format(most_sweeps_of_all)

# records for street
def find_street (input_street):
	with open('sweep.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			street = row[5]
			if street == input_street:
				print row
				#return row

				#function to make it nice

find_street('Ulloa St')

# what days of week
street_sweep_dow = []

def street_day_of_week (input_street):
	with open('sweep.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			street = row[5]
			dow = row[1]
			if street == input_street:
				if dow not in street_sweep_dow:
					street_sweep_dow.append(dow)

	print '{}'.format(input_street) + ' is swept on ' + ', '.join(sorted(street_sweep_dow))

street_day_of_week('Ulloa St')

# what weeks of the month

weeks_of_month_swept = []
def weeks_of_month (input_street):
	with open('sweep.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			street = row[5]
			week_one = bool(row[10])
			week_two = bool(row[11])
			week_three = bool(row[12])
			week_four = bool(row[13])
			week_five = bool(row[14])
			if street == input_street:
				if week_one == True:
					if 'first' not in weeks_of_month_swept:
						weeks_of_month_swept.append('first')
				if week_two == True:
					if 'second' not in weeks_of_month_swept:
						weeks_of_month_swept.append('second')
				if week_three == True:
					if 'third' not in weeks_of_month_swept:
						weeks_of_month_swept.append('third')
				if week_four == True:
					if 'fourth' not in weeks_of_month_swept:
						weeks_of_month_swept.append('fourth')
				if week_five == True:
					if 'fifth' not in weeks_of_month_swept:
						weeks_of_month_swept.append('fifth')
	print '{}'.format(input_street) + ' is swept on the ' + ', '.join(weeks_of_month_swept) + ' week(s) of the month.'

weeks_of_month('Ulloa St')

#which address
def my_block(my_street, my_address):
	with open('sweep.csv') as f:
		reader = csv.reader(f)
		for row in reader: 
			street = row[5]
			day = row[1]
			if street == my_street:
				if my_address%2 == 0:
					try:
						from_number_even = int(row[17])
						to_number_even = int(row[16])
					except:
						print 'There was a problem with the data.'
						continue
					if from_number_even < my_address and to_number_even > my_address:
						day_coming = day
				else:
					try:
						from_number_odd = int(row[14])
						to_number_odd = int(row[15])
					except: 
						print 'There was an issue with the data.'
						continue
					if from_number_odd < my_address and to_number_odd > my_address:
						day_coming = day

		print 'The street in front of {}'.format(my_address) + ' {} '.format(my_street) + 'is swept on {}'.format(day_coming)

my_block('Harrison St', 910) 

			


# def find_street (input_street):
# 	with open('sweep.csv') as f:
# 		reader = csv.reader(f)
# 		search_street = raw_input("Enter street")
# 		for row in reader:
# 			street = row[5]
# 			if street == search_street:
# 				print row

# find_street('Ulloa')