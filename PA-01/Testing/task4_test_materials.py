import csv
import task1_test_materials as one
import task2_test_materials as two


FILE = "/home/egwebber/cmsc12300/PA-01/Data/WhiteHouse.csv"

OUT = "/home/egwebber/cmsc12300/PA-01/Output/task-four-sanity-check.txt"



# oh, maybe this isn't matching because of the middle name append? 
def read():

	visitors = {}
	visitees = {}

	with open(FILE, 'rU') as f, open(OUT, 'w') as w:
		w.write("List of people who were both a guest and a staff member \n in 2009 and 2010\n")

		fields = csv.reader(f)
		headers = next(fields)
		for row in fields:
			if one.not_canceled(row):
				guest = one.get_visitor_name(row)
				staff = two.get_visitee_name(row)

				if guest not in visitors:
					visitors[guest] = 1
				if staff not in visitees:
					visitees[staff] = 1

		for g in list(visitees.keys()):
			if g in visitors:
				w.write("\n{}".format(g))



if __name__ == "__main__":
	read()
