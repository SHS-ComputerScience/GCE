# Linear Search Algorithm

def linear_search(array, value):

	for i in range(len(array)):
		if array[i] == value:
			return True

	return False