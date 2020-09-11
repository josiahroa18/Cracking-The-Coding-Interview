# Given a string, return whether or not it uses capitalization correctly. 
# A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

# Ex: Given the following strings...

# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true

# Understand & Plan 
# Need to perform 3 checks
# All checks require that I loop through the whole string
# Loop through and check the capitalization of each string. Keep a count and boolean variable
# boolean variable - is the first letter capitalized
# count - number of capital characters
# At the end, check if length of string is equal to count
# true: return True
# check if count is one and boolean is true
# true: return True
# check if count is 0
# true: return True
# Otherwise, return False

# Reflect
# Time Complexity is O(n) where n is the number of chars in the string
# Space Complexity is O(1)
def correct_cappitalization(string):
    count = 0
    first_is_capital = True if string[0].isupper() else False

    for char in string:
        if char.isupper():
            count += 1

    if len(string) == count:
        return True
    if first_is_capital and count == 1:
        return True
    if count == 0:
        return True
    return False

def main():
    print(correct_cappitalization("USA")) # expect True
    print(correct_cappitalization("Calvin")) # expect True
    print(correct_cappitalization("compUter")) # expect False
    print(correct_cappitalization("coding")) # expect True

if __name__ == '__main__':
    main()