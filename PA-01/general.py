FIRST = 1
LAST = 0
MIDDLE = 2

YEAR = 11
VISITEE_LAST = 19
VISITEE_FIRST = 20

MISSING = "MISSING"
EMPTY = ""

GENERIC = "OFFICE, VISITORS"
POTUS = "POTUS"
OFFICE = "OFFICE"
HEADER = "NAMELAST"

YEAR_09 = '2009'
YEAR_10 = '2010'
BOTH = 'Both'

def has_middle(row):
	return len(row[MIDDLE]) != 0

def get_year(line):
	if YEAR_09 in line[YEAR]:
		return YEAR_09
	return YEAR_10

def both_years(years):
	return ((YEAR_10 in years) and (YEAR_09 in years)) or (BOTH in years)

def is_header(line):
	return HEADER in line

def not_canceled(row):
	return len(row[CANCEL]) == 0

def get_visitor_name(row):
	if row[LAST] == EMPTY and row[FIRST] == EMPTY and row[MIDDLE] == EMPTY:
		return MISSING
	if len(row[MIDDLE]) != 0:
		return row[LAST] + ", " + row[FIRST] + " " + row[MIDDLE]
	return row[LAST] + ", " + row[FIRST]

def get_visitee_name(row):
	if is_potus(row):
		return POTUS
	if row[VISITEE_LAST] == EMPTY and row[VISITEE_FIRST] == EMPTY:
		return MISSING
	name = row[VISITEE_LAST] + ", " + row[VISITEE_FIRST]
	if OFFICE in name:
		return GENERIC
	return name

def is_potus(row):
	return (row[VISITEE_LAST] == POTUS) or (row[VISITEE_FIRST] == POTUS)
