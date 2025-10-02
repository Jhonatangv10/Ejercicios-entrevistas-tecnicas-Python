def intersection(a, b):
	"""
	It gets the instersection between two lists

	:param a: (list) List of int numbers
	:param b: (list) List of int numbers
	:return: A list with the intersections.
			-intersection_list(list): List with the intersections between a and b

	"""
	intersection_list = []
	for x in a:
		if x in b:
			intersection_list.append(x)
		else:
			continue
	return(intersection_list)



result = intersection([1, 2, 3, 4, 5], [0, 1, 3, 7])
print(result)