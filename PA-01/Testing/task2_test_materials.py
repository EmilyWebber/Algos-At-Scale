import csv
import task1_test_materials as one

FILE = "/home/egwebber/egwebber/PA-01/Data/WhiteHouse.csv"

OUT = "/home/egwebber/egwebber/PA-01/Output/task-two-sanity-check.txt"

LAST = 19
FIRST = 20

GENERIC = "OFFICE, VISITORS"
POTUS = "POTUS"
MISSING = "MISSING"
EMPTY = ""

def read():

	top_ten = {}

	total_counts = {}

	with open(FILE, 'rU') as f:
		fields = csv.reader(f)
		headers = next(fields)
		for row in fields:

			name = get_visitee_name(row)

			if one.not_canceled(row):

				# if the name is already in the top ten, add one more to the count
				if name in top_ten:
					top_ten[name] += 1

				else:

					# get that person's count
					count, total_counts = get_count(name, total_counts)

					# if top ten has less than ten elements
					if len(list(top_ten.keys())) < 10:
						top_ten[name] = top_ten.setdefault(name, 1) + 1

					else:

						for n, c in top_ten.items():
							if count > c:
								
								# remove n and c from top_ten and add to total_counts
								total_counts[n] = top_ten.pop(n)

								# remove person from total counts and add to top_ten
								top_ten[name] = total_counts.pop(name)
								break


	return top_ten

def get_count(name, total_counts):
	'''
	Takes a name and a counting dictionary, updates the dictionary and returns the full count for that person
	'''
	if name not in total_counts:
		total_counts[name] = 1
	else:
		total_counts[name] += 1
	return total_counts[name], total_counts

def get_visitee_name(row):
	if is_potus(row):
		return POTUS
	if row[LAST] == EMPTY and row[FIRST] == EMPTY:
		return MISSING
	return row[LAST] + ", " + row[FIRST]

def is_potus(row):
	return (row[LAST] == POTUS) or (row[FIRST] == POTUS)


def write(top):
	with open(OUT, 'w') as f:
		f.write("Top Ten Most Visited White House Staff\n\n")
		for name, count in top.items():
			f.write("{} was visited {} times\n".format(name, count))


if __name__ == "__main__":
	top = read()
	write(top)