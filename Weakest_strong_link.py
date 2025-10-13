def weakest_strong_link(strength):
    """
    It gets the weakest strong link of a matrix. The Weakest Strong Link is defined as 
    the weakest chain-link in its row but also the strongest link in its column.

    :param strength: (List) List of arrays
    :return: (int) Return the weakest strong link if it exists; otherwise, return -1.
            -minus_strength (list): Contains a list of the minimun values of each row
            -max_strength (list): Contains a list of the higher values of each column
            -strength_list (list): Contains a list of each individual value of the matrix
            -column_list (list): Contains a list of the columns of the strength matrix
            -position (int): Value to get the position in a for cicle
            -x (int): Value to modify the position value
    """

    minus_strength = []
    max_strength = []
    strength_list = []
    columns_matrix = []
    column_list = []
    position = 1
    x = 1
    #Get a list with the lower values of each row
    for row in range(0, len(strength)):
        new_row = strength[row]
        new_row.sort()
        minus_strength.append(new_row[0])
    
    #Get a list of the matrix
    for row in range(0, len(strength)):
        for column in range(0, len(strength[row])):
            new_column = strength[row][column]
            strength_list.append(new_column)

    #Get the columns of the matrix based on the matrix list above
    for column_value in range(0, len(strength_list)):
        #To prevent out of index error
        if position - 1 < len(strength_list):
            column_list.append(strength_list[position-1])
        else:
            break
        position += len(strength)

        if len(column_list) == len(strength):
            columns_matrix.append(column_list)
            position = 1
            position += x
            x += 1
            column_list = []

    #Get a list with the higher values of each row
    for row in range(0, len(columns_matrix)):
        new_row = columns_matrix[row]
        new_row.sort(reverse=True)
        max_strength.append(new_row[0])

    #Getting the weakest_strong_link
    minus_set = set(minus_strength)
    max_set = set(max_strength)
    w_s_link = minus_set.intersection(max_set)

    if minus_set.intersection(max_set):
        w_s_link = list(w_s_link)
        return w_s_link[0]
    else:
        return -1
   

link = weakest_strong_link([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(link)

#Try this matrices to verify
#[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#[[9, 8, 10],[6, 15, 4]]