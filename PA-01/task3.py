from mrjob.job import MRJob 
import general as gen 

class Two_Year_Visitor(MRJob):

	def mapper(self, _, line):
		if not gen.is_header(line):
			r = line.split(",")
			yield gen.get_visitor_name(r), gen.get_year(r)

	def combiner(self, name, years):
		yield name, list(years)

	def reducer(self, name, years):
		l = str(list(years))

		if gen.both_years(l):
		 	yield name, l

if __name__ == "__main__":
	Two_Year_Visitor.run()