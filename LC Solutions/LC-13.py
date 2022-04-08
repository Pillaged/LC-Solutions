def romanToInt(s: str):
    """
    Numerals are written from smallest left to right based on their log10 location
    Might need dictionary with key values pairs to define each letter
    If numbers are to the right, add to the total
    If left, subtract from the largest numeral to the right.        

    LVIII => 58
    XLIX => 49
    """
    vals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = 0
    for numbyor, letter in enumerate(s):
        t= s+"I"
        if vals[letter] < vals[t[numbyor+1]]:
            a = (-vals[letter])
            total += a
        else:
            b = vals[letter]
            total += b
    return total

#romanToInt("XLIX")
#romanToInt("III")
#romanToInt("VX")