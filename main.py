instruction_list = ['Please enter the radius of the wind turbine in meters.',
                    'Please enter the efficiency of the wind turbine as a '
                    'percentage.', 'Please enter the average wind speed in '
                                   'm/s.']

print('Your input may be a decimal, integer, or fraction consisting of integers.')

input_list = []  # [radius, efficiency, wind_speed]

for cc in range(3):

    print(instruction_list[cc])

    value = input()
    input_list.append(value)

    test_value = str(input_list[cc])  # the value that will be modified to test if it's a number

    # check if there is a decimal place
    if test_value.count(".") == 1 and test_value.count("/") == 0:
        # replace the "." with a 1
        test_value = test_value.replace(".", "1")

    # check if there is a /
    elif test_value.count("/") == 1:
        # replace the "/" with a 1
        test_value = test_value.replace("/", "1")

    # check if there are characters other than numbers
    if not test_value.isdecimal():
        print("One or more inputs was not a number, please re-enter values.")
        exit()

    # check if the input is a fraction by finding /
    slash_position = input_list[cc].find("/")
    if slash_position != -1:
        # if it is a fraction, find the percentage
        fraction = input_list[cc].split("/")
        input_list[cc] = float(fraction[0]) / float(fraction[1])
        input_list[cc] = input_list[cc] * 100  # decimal to %

    # change value to a float type
    input_list[cc] = float(input_list[cc])

    cc = cc + 1

print(input_list)