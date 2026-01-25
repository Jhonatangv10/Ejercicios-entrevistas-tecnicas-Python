def romanToInt(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    increment = 1
    
    for num in range(0, len(s)):
        if len(s) == 1:
            integer = roman[s]
            break
        
        if increment in range(0, len(s)):
            if roman[s[num]] > roman[s[increment]]:
                integer += roman[s[num]]
            if roman[s[num]] < roman[s[increment]]:
                integer -= roman[s[num]]
            if roman[s[num]] == roman[s[increment]]:
                integer += roman[s[num]]
        else:
            integer += roman[s[num]]
        increment += 1
    return integer

conversion = romanToInt("XXI")

print(conversion)