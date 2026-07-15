# Write a function that takes a positive integer, n, as an argument and prints
# a right triangle whose sides each have n stars. The hypotenuse of the
# triangle (the diagonal side in the images below) should have one end at the
# lower-left of the triangle, and the other end at the upper-right.

def triangle(n):
    spaces = n - 1
    while spaces >= 0:
        print(f"{spaces * ' '}{(n - spaces) * '*'}")
        spaces -= 1

triangle(5)
# Output
#     *
#    **
#   ***
#  ****
# *****

triangle(9)
# Output
#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********
