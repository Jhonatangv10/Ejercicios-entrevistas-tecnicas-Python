def Compound_Interest():
    principal = int(input("Starting amount: "))
    rate =  float(input("Percentage as interest: "))
    contribution = int(input("The amount you add at the end of each year: "))
    years = int(input("How many years do you want?: "))
    
    compound = principal

    for interest in range(0, years):
        compound += contribution + compound * (rate/100)

    return round(compound, 2)

    #return round((principal * (1 + (rate/100))**years  + contribution * (((1 + (rate/100))**years - 1) / (rate/100))), 2)

Result = f"The final sum will be: {Compound_Interest()}"
print(Result)