# Author: Michael Hans
# Software Engineer Intern
# Moutar Technology
# March, 28th 2021

# Roman Dictionary
rom_numeric = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

pre_numeric = {
    "I": None,
    "V": "I",
    "X": "I",
    "L": "X",
    "C": "X",
    "D": "C",
    "M": "C"
}

# Convert from roman string into numeric
def roman_converter(raw):
    total = 0
    lastValue = 0
    n = len(raw)
    for i in range(len(raw)):
        if (i > 0):
            if (raw[i] == "I"):
                lastValue = rom_numeric[raw[i]]
            elif (raw[i-1] == pre_numeric[raw[i]]):
                total -= lastValue
                lastValue = rom_numeric[raw[i]] - lastValue
            else:
                lastValue = rom_numeric[raw[i]]
        else:
            lastValue = rom_numeric[raw[i]]
        total += lastValue
    return total

# Main Program
raw_string = input()
print(roman_converter(raw_string))