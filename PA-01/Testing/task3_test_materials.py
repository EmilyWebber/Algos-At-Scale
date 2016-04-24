import csv
import task1_test_materials as one

FILE = "/home/egwebber/egwebber/PA-01/Data/WhiteHouse.csv"
OUT = "/home/egwebber/egwebber/PA-01/Output/task-three-sanity-check.txt"

def read():

	counts = {}

	with open(FILE, 'rU') as f, open(OUT, 'w') as w:
		w.write("List of visitors from either 2009 or 2010\n")
		fields = csv.reader(f)
		headers = next(fields)
		for row in fields:
			if one.not_canceled(row):
				name = one.get_visitor_name(row)
				if name not in counts:
					counts[name] = "written"
					w.write("\n{}".format(name))

if __name__ == "__main__":
	read()