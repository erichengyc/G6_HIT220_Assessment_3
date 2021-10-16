# Efficient Python3 program to find
# minimum time required to produce m items.
import sys

def findItems(arr, n, temp):
	ans = 0
	for i in range(n):
		ans += temp // arr[i]
	return ans

# Binary search to find minimum time
# required to produce M items.
def bs(arr, n, m, high):
	low = 1

	# Doing binary search to find minimum
	# time.
	while low < high:

		# Finding the middle value.
		mid = (low + high) >> 1

		# Calculate number of items to
		# be produce in mid sec.
		itm = findItems(arr, n, mid)

		# If items produce is less than
		# required, set low = mid + 1.
		if itm < m:
			low = mid + 1

		# Else set high = mid.
		else:
			high = mid
	return high

# Return the minimum time required to
# produce m items with given machine.
def minTime(arr, n, m):
	maxval = -sys.maxsize

	# Finding the maximum time in the array.
	for i in range(n):
		maxval = max(maxval, arr[i])

	return bs(arr, n, m, maxval * m)

# Driver Code
if __name__ == "__main__":
	arr = [6, 16]
	n = len(arr)
	m = 2
	print(minTime(arr, n, m))

