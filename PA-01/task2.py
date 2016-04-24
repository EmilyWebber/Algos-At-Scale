from mrjob.job import MRJob 
import general as gen
import heapq

class Ten_Most_Visited(MRJob):

	def mapper(self, _, line):
		if not gen.is_header(line):
			name = gen.get_visitee_name(line.split(","))
			if name is not gen.MISSING:
				yield name, 1

	def combiner(self, name, counts):
		yield name, sum(counts)

	def reducer_init(self):
		l = [(i, " ") for i in range(10)]
		heapq.heapify(l)
		self.h = l

	def reducer(self, name, counts):
		s = sum(counts)		
		low, n = self.h[0]
		if s > low:
			heapq.heapreplace(self.h, (s, name))

	def reducer_final(self):
		self.h.sort(reverse=True)
		for n, c in self.h:
			yield n, c

if __name__ == "__main__":
	Ten_Most_Visited.run()