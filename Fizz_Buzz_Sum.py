def fizz_buzz_sum(target):
    """
    Find the sum of all multiples of 3 or 5 below a target value.

    :param target: (int) Target value
    :return: (int) Return the sum of all multiples of 3 or 5 below a target value.
            -multiple_three_list (List): Contains a list of all multiples of three below a target number
            -multiple_five_list (List): Contains a list of all multiples of five below a target number
    """
    multiple_three_list = []
    multiple_five_list = []

    for x in range(1, target+1):
        sum_multiple_three = x * 3
        sum_multiple_five = x * 5
        if sum_multiple_three < target:
            multiple_three_list.append(sum_multiple_three)
        if sum_multiple_five < target:
            multiple_five_list.append(sum_multiple_five)
        if sum_multiple_three > target:
            sum_multiple_three = 0
        if sum_multiple_five > target:
            sum_multiple_three = 0
            
    #Transforming lists to sets in order to get the intersection between them
    set_multiple_three = set(multiple_three_list)
    set_multiple_five = set(multiple_five_list)
    sets = set_multiple_three.union(set_multiple_five)
    set_list = list(sets)
    sum_set_list = sum(set_list)
    
    return sum_set_list

sum_result = fizz_buzz_sum(16)
print(sum_result)