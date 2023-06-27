#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    div_result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            if isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                try:
                    division = dividend / divisor
                except (ZeroDivisionError):
                    division = 0
                    print("division by 0")
            else:
                division = 0
                print("wrong type")
        except (IndexError):
            division = 0
            print("out of range")
        finally:
            div_result.append(division)
    return (div_result)
