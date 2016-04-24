from mrjob.job import MRJob 
import general as gen 

EXCLUDE = [gen.POTUS, gen.GENERIC, "VPOTUS, ", "FLOTUS, ", gen.MISSING, "POTUS/FLOTUS, "]

class Guest_and_Staff(MRJob):

	def mapper(self, _, line):
		if not gen.is_header(line):
			r = line.split(",")
			guest = gen.get_visitor_name(r)
			staff = gen.get_visitee_name(r)
			if (staff not in EXCLUDE) and (not gen.has_middle(r)):
				yield guest, staff

	def reducer_init(self):
		self.visitees, self.visitors = {}, {}

	def reducer(self, guest, staff):
		for s in list(staff):
			if s not in self.visitees:
				self.visitees[s] = True
		if guest not in self.visitors:
			self.visitors[guest] = True

	def reducer_final(self):
		for g in self.visitees.keys():
			if g in self.visitors:
				yield g, None

if __name__ == "__main__":
	Guest_and_Staff.run()