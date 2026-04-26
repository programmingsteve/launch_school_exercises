# Build a program that asks the user to enter the length and width of a room,
# in meters, then prints the room's area in both square meters and square feet.
#
# Note: 1 square meter == 10.7639 square feet

length = float(input('Enter the room length in meters: '))
width = float(input('Enter the room width in meters: '))

area_in_meters = length * width
area_in_feet = 10.7639 * area_in_meters

print(f'The area of the room in square meters is {area_in_meters:.2f}')
print(f'The area of the room in square feet is {area_in_feet:.2f}')
