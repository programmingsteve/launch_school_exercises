# Write a function that takes a short line of text and prints it within a box.

# print_in_box('To boldly go where no one has gone before.')
# Output
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

# print_in_box('')
# Output
# +--+
# |  |
# |  |
# |  |
# +--+

def print_in_box(text):
    length = len(text)
    plus_line = f"+-{'-' * length}-+"
    bar_line = f"| {' ' * length} |"

    print(plus_line)
    print(bar_line)
    print(f"| {text} |")
    print(bar_line)
    print(plus_line)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')
