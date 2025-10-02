def another_one(digits):
    i = len(digits) - 1 
    while i >= 0 and digits[i] == 9:
        # Change all 9s to 0
        digits[i] = 0
        i -= 1

    # If we found a non-9 digit, just add 1
    if i >= 0:
        digits[i] += 1
        return digits
    
    # What should we do if all digits were 9?

result = another_one([1, 2, 3])
print(result)

