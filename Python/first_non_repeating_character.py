'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.
There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.
There are no characters in this string that do not repeat.

Understand: 
I need to return the first character that isn't repeated within the given string
If all characters in the string are repeating, return '_'
Otherwise, return the FIRST repeating character

Plan:
Create a hashtable - Expected format:
{
    character: count
}
Create a an array that keeps track of the order of characters

Loop through the characters of the string once
For each character:
- If it has not been seen: add it to a hashtable and set its count
- If it has been seend: increase its count

At the end, loop through the array of characters
- Access that char in the hashtable and get its count
- The first char to have a count of 1 is the first non-repeating character: return it

If all characters repeat: return '_'
'''
def first_not_repeating_character(s):
    chars = {}
    order = []
    for char in s:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
            order.append(char)
    for char in order:
        if chars[char] == 1:
            return char
    return '_'
    
'''
Reflect:
Time complexity is O(2n) -> O(n) since we have one loop to get the count of each char
  and another loop to find the first char that is non-repeating
Space complexity is O(n) since we have a hash table and an array that store the char count and 
  order of the chars in the string
'''
