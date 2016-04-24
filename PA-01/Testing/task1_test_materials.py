import csv

FILE = "/home/egwebber/egwebber/PA-01/Data/WhiteHouse.csv"

OUT = "/home/egwebber/egwebber/PA-01/Output/task-one-sanity-check.txt"

FIRST = 1
LAST = 0
MIDDLE = 2

CANCEL = 13
MISSING = "MISSING"
EMPTY = ""

# probably should equip this to tell me how many times this person came
# just to eyeball it and make sure all the counts are greater than 10

# what if there are random mistakes with the names? like first name closely approximating last name, other mess ups

def read():

	# final list for output
	at_least_ten = []

	# counting dictionary
	counts = {}

	with open(FILE, 'rU') as f:
		fields = csv.reader(f)
		headers = next(fields)

		for row in fields:

			if not_canceled:

				name = get_visitor_name(row)

				if name not in at_least_ten:
					counts[name] = counts.setdefault(name, 1) + 1

					if counts[name] >= 10:
						at_least_ten.append(name)

	return at_least_ten

def not_canceled(row):
	return len(row[CANCEL]) == 0

def get_visitor_name(row):
	if row[LAST] == EMPTY and row[FIRST] == EMPTY and row[MIDDLE] == EMPTY:
		return MISSING
	if len(row[MIDDLE]) != 0:
		return row[LAST] + ", " + row[FIRST] + " " + row[MIDDLE]
	return row[LAST] + ", " + row[FIRST]


def write(ten):
	'''
	Takes a list of full names, where each person has visited the White House at least one time
	Writes list to a text file to use for testing purposes
	'''
	with open(OUT, 'w') as f:
		f.write("List of people who have visited the White House \nAt least ten times\n")
		for name in sorted(ten):
			f.write("\n" + name)


if __name__ == "__main__":
	ten = read()
	write(ten)