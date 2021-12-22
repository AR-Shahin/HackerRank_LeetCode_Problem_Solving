
def romanToInt(roman):
    hash = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    sum = 0

    for i in range(len(roman)):
        if i + 1 < len(roman) and hash[roman[i]] < hash[roman[i+1]]:
            sum -= hash[roman[i]]
        else:
            sum += hash[roman[i]]
    return sum


print(romanToInt("MCMXCIV"))
