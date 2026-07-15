# Write a function that takes a string argument and returns a new string that
# contains the value of the original string with all consecutive duplicate
# characters collapsed into a single character.

def crunch(string):
    result = ''
    i = 0
    while i < len(string):
        char = string[i]
        next_char = string[i + 1:i + 2]
        if (not next_char) or (char != next_char):
            result += char

        i += 1

    return result

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

# Alternative solution
# def crunch(string):
#     result = ''
#     i = 0
#     while i < len(string):
#         result += string[i]
#         j = i + 1
#
#         while j < len(string):
#             if (string[i] != string[j]):
#                 break
#
#             j += 1
#
#         i = j
#
#     return result

# LS Solution
# def crunch(text):
#     index = 0
#     crunched_text = ''
#
#     while index < len(text):
#         if index == len(text) - 1 or text[index] != text[index + 1]:
#             crunched_text += text[index]
#
#         index += 1
#
#     return crunched_text
