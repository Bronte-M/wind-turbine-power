#######################################################################
# Program Filename: main.py
# Author:  Bronte McKinnis
# Date: 4/7/2022
# Description: Determine actual and max power of a wind turbine.
# Input: radius (m), efficiency (%), average wind speed (m/s)
# Output: max power (Watts), actual power (Watts)
#######################################################################

import math

# constants:
AIR_DENSITY = 1.2  # kg/m^3

# instructions for input
instruction_list = ['Please enter the radius of the wind turbine in meters.',
                    'Please enter the efficiency of the wind turbine as a %.',
                    'Please enter the average wind speed in m/s.']

# initial instructions
print('Your input may be a decimal, integer or fraction (of integers).')

input_list = []  # [radius, efficiency, wind_speed]

# prints input instructions, checks it's a number, and saves input to a list
for cc in range(3):

    print(instruction_list[cc])

    value = input()
    input_list.append(value)

    test_value = str(input_list[cc])  # altered in testing
    length = len(test_value)

    # check if there is a decimal place and no /
    if test_value.count(".") == 1 and test_value.count("/") == 0:
        test_value = test_value.replace(".", "1")  # could still be a number

    # check if there is a / not at the beginning or end: 1 / is good
    elif test_value.count("/") == 1:
        if input_list[cc].find('/') != 0:
            if input_list[cc].find('/') != (length - 1):
                test_value = test_value.replace("/", "1")

    # check if there are characters other than numbers
    if not test_value.isdecimal():
        print("One or more inputs was not a number, please re-enter values.")
        exit()

    # check if the input is a fraction by finding / and convert to decimal
    slash_position = input_list[cc].find("/")

    if slash_position != -1:
        fraction = input_list[cc].split("/")
        input_list[cc] = float(fraction[0]) / float(fraction[1])

        # for efficiency, change the decimal to a percentage
        if cc == 1:
            input_list[cc] = input_list[cc] * 100  # decimal to %

    # change value to a float type
    input_list[cc] = float(input_list[cc])

# place all items in input_list into separate variables for readability
radius = input_list[0]
efficiency = input_list[1] / 100  # convert percentage to decimal
wind_speed = input_list[2]

# check that efficiency is <= 1
if efficiency > 1:
    print('The efficiency value was more than 100%. Please re-enter values.')
    exit()

# calculate area
area = math.pi * (radius ** 2)  # m^2
# print('The area of the wind turbine is ' + str(area) + ' m^2.')

# calculate the maximum power
max_power = 0.5 * AIR_DENSITY * area * (wind_speed ** 3)  # Watts

print('Maximum power: ' + str(round(max_power, 4)) + ' Watts.')

# calculate actual power
actual_power = efficiency * max_power  # Watts

print('Actual power: ' + str(round(actual_power, 4)) + ' Watts')
