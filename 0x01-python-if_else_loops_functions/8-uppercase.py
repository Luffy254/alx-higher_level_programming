#!/usr/bin/python3
def uppercase(str):
    tmp_str = list(str)
    for i in range(len(tmp_str)):
        if ord(tmp_str[i]) >= 97 and ord(tmp_str[i]) <= 122:
            tmp_str[i] = chr(ord(tmp_str[i]) - 32)
    print("{}".format("".join(tmp_str[i])))
