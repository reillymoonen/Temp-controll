def round_ans(val):
    """
    Rounds temperature to nearest degree
    :param val: Number to be rounded
    :return: Number rounded to nearest degree
    """
    return round(val)  # Use Python's round directly to return real rounded values.


def to_celsius(to_convert):
    """
    Converts temperature from °F to °C
    :param to_convert: Temperature to be converted in °C
    :return: Converted temperature in °C
    """
    answer = (to_convert - 32) * 5 / 9
    return round_ans(answer)


def to_fahrenheit(to_convert):
    """
    Converts temperature from °C to °F
    :param to_convert: Temperature to be converted in °F
    :return: Converted temperature in °F
    """
    answer = to_convert * 1.8 + 32
    return round_ans(answer)


# Main Routine / Testing starts here
# to_c_test = [0, 100, -459]
# to_f_test = [0, 100, 40, -273]
#
# # Convert from Celsius to Fahrenheit
# for item in to_f_test:
#     ans = to_fahrenheit(item)
#     print(f"{item}°C is {ans}°F")
#
# print()
#
# # Convert from Fahrenheit to Celsius
# for item in to_c_test:
#     ans = to_celsius(item)
#     print(f"{item}°F is {ans}°C")
