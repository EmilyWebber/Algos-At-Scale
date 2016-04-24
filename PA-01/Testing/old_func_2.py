	def combiner(self, name, years):
		yield name, list(years)
		# o9 = False
		# i0 = False

		# l = str(list(years))

		# if gen.YEAR_09 in l:
		# 	o9 = True
		# if gen.YEAR_09 in l:
		# 	i0 = True
		# if o9 and i0:
		# 	yield name, gen.BOTH
		# if o9: 
		# 	yield name, gen.YEAR_09
		# if i0:
		# 	yield name, gen.YEAR_10
