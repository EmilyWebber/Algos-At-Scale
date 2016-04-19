import sys


def n_gen(n):
		for i in list(range(2*(n-1)+1)):
			if i % 2 == 0:
				yield i

for i in n_gen(10):
	print (i)

# if __name__ == "__main__":
# 	n_gen(sys.argv[2])