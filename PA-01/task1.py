from mrjob.job import MRJob 
import general as gen

class MR_Minimum_Ten(MRJob):

	def mapper(self, _, line):
		if not gen.is_header(line):
			n = gen.get_visitor_name(line.split(",")), 1
			if n != gen.MISSING:
				yield n, 1

	def combiner(self, name, counts):
		yield name, sum(counts)

	def reducer(self, name, counts):
		s = sum(counts)
		if s >= 10:
			yield name, s

if __name__ == "__main__":
	MR_Minimum_Ten.run()