def is_same_stripes(matrix):
	"""
	It determines if the elements in a matrix have identical diagonal stripes.
	:param matrix: (list) List of arrays 
	:return: (True or False) True for identical diagonal stripes. False if not.
			-list_matrix (list): Contains a list of the diagonal stripes
			-list_compare (list): Contains a list of each value of the matrix given
			-list_true_false (True or False): True for each identical stripe. False if not.

	"""
	list_matrix = []
	list_compare = []
	list_true_false = []
	for x in range(0, len(matrix)):
		for y in range(0, len(matrix[x])):
			list_matrix.append(matrix[x][y])
	for z in range(0,len(list_matrix)):
		if z == len(matrix):
			list_compare.append(list_matrix[z:(len(matrix[x])+1):(len(matrix[x])+1)])
		else:
			list_compare.append(list_matrix[z::(len(matrix[x])+1)])
	for i in range(0, len(list_compare)):
		if list_compare[i][0] == sum(list_compare[i])//len(list_compare[i]):
			list_true_false.append(True)
		else:
			list_true_false.append(False)
	if False in list_true_false:
		return(False)
	else:
		return(True)


result = is_same_stripes([[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]])
print(result)

#[[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]]
#[[8, 23], [69, 1]]