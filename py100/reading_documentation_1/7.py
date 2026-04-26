# Out Of Bounds

# What happens if we take the list ['fish', 'and', 'chips'] and try to access
# the element at index position 10? First try to determine what will happen by
# consulting the documentation, then verify your understanding in the Python
# REPL.

lis = ['fish', 'and', 'chips']

# According to the docs, seq.index 'Raises ValueError if value is not found in
# sequence.' The entry of ValueError exceptions states that they are raised
# 'when an operation or function receives an argument that has the right
# type but an inappropriate value, and the situation is not described by a more
# precise exception such as IndexError.' Thus, an IndexError will be raised as 
# shown below.

print(lis[10])
