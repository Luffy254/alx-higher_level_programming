#!/usr/bin/python3
def uppercase(str):
    result = ""
    tmp_str = list(str)
    for i in range(len(tmp_str)):
        if ord(tmp_str[i]) >= 97 and ord(tmp_str[i]) <= 122:
            result += chr(ord(tmp_str[i]) - 32)
        else:
            result += tmp_str[i]
    print(result)
