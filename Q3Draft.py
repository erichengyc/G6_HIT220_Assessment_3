# Python 3 program to find number of
# points lie inside or on the circumference
# of circle for Q queries.
import math

# Computing the x^2 + y^2 for each
# given points and sorting them.
def preprocess(p, x, y, n):
	for i in range(n):
		p[i] = x[i] * x[i] + y[i] * y[i]

	p.sort()

# Return count of points lie inside
# or on circumference of circle using
# binary search on p[0..n-1]
def query(p, n, rad):

	start = 0
	end = n - 1
	while ((end - start) > 1):
		mid = (start + end) // 2
		tp = math.sqrt(p[mid])

		if (tp > (rad * 1.0)):
			end = mid - 1
		else:
			start = mid

	tp1 = math.sqrt(p[start])
	tp2 = math.sqrt(p[end])

	if (tp1 > (rad * 1.0)):
		return 0
	elif (tp2 <= (rad * 1.0)):
		return end + 1
	else:
		return start + 1

# Driver Code
if __name__ == "__main__":
	
	x = [ 1, 2, 3, -1, 4 ]
	y = [ 1, 2, 3, -1, 4 ]
	n = len(x)

	# Compute distances of all points and keep
	# the distances sorted so that query can
	# work in O(logn) using Binary Search.
	p = [0] * n
	preprocess(p, x, y, n)

	# Print number of points in a
	# circle of radius 3.
	print(query(p, n, 3))

	# Print number of points in a
	# circle of radius 32.
	print(query(p, n, 32))

print(x)
