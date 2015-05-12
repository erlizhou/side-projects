import json
import operator

def readfile(filename):
	infile = open(filename, 'r')
	# keep track of index of line in the input file
	counter = 0
	# initialize entries and errors key in JSON format
	entries, errors = [], []
	total = {'entries': entries, 'errors': errors}
	for line in infile:
		objects = line.strip().split(',')
		# if length of splitted input is different than 4 or 5, the line does not satisfy any of the formats
		if len(objects) != 4 and len(objects) != 5:
			errors.append(counter)
		elif len(objects) == 4:
			# if length of telephone number is not equal to 10 or length of zipcode is not equal to 5, the line does not satisfy format number two
			if len(objects[3].translate(None, '()- ')) != 10 or len(objects[2].strip()) != 5:
				errors.append(counter)
			else:
				# satisfy format number two
				name = objects[0].strip().split(' ')
				format2 = {'color': objects[1].strip(), 'firstname': name[0], 'lastname': name[1], \
				'phonenumber': objects[3].strip().replace(' ', '-'), 'zipcode': objects[2].strip()}
				entries.append(format2)
		else:
			# if length of telephone number is not equal to 10, the line does not satisfy format number one for format number three
			if len(objects[2].translate(None, '()- ')) != 10 and \
			len(objects[3].translate(None, '()- ')) != 10:
				errors.append(counter)
			elif len(objects[2].translate(None, '()- ')) == 10:
				# if length of zipcode is not equal to 5, the line does not satisfy format number one
				if len(objects[4].strip()) != 5:
					errors.append(counter)
				else:
					# satisfy format number one
					format1 = {'color': objects[3].strip(), 'firstname': objects[1].strip(), 'lastname': objects[0].strip(), \
					'phonenumber': objects[2].strip().translate(None, '()'), 'zipcode': objects[4].strip()}
					entries.append(format1)
			else:
				# if length of zipcode is not equal to 5, the line does not satisfy format number three
				if len(objects[2].strip()) != 5:
					errors.append(counter)
				else:
					# satisfy format number three
					format3 = {'color': objects[4].strip(), 'firstname': objects[0].strip(), 'lastname': objects[1].strip(), \
					'phonenumber': objects[3].strip().replace(' ', '-'), 'zipcode': objects[2].strip()}
					entries.append(format3)
		counter += 1
	# sort entries alphabetically by lastname, then by firstname
	entries.sort(key = operator.itemgetter('lastname', 'firstname'))
	outfile = open('result.out', 'w')
	# output file in JSON format
	outfile.write(json.dumps(total, sort_keys = True, indent = 2, separators = (',', ': ')))

if __name__ == "__main__":
	readfile('data.in')