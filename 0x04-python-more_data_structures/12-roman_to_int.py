#!/usr/bin/python3

def roman_to_subtract(list_num):
    roman_to_sub = 0
    total_list = max(list_num)

    for n in list_num:
        if total_list > n:
            roman_to_sub += n

    return (total_list - roman_to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num_keys = list(roman_num.keys())

    no = 0
    end_rom = 0
    list_num = [0]

    for update in roman_string:
        for rom_num in num_keys:
            if rom_num == update:
                if roman_num.get(update) <= end_rom:
                    no += roman_to_subtract(list_num)
                    list_num = [rom_num.get(update)]
                else:
                    list_num.append(roman_num.get(update))
                end_rom = roman_num.get(update)

    no += roman_to_subtract(list_num)

    return (no)
