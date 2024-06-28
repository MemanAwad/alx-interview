#!/usr/bin/python3
'''utf8-validation'''


def validUTF8(data):
    '''function that return true if valid
    utf8 validation and return false otherwise'''
    count = 0
    for num in data:
        if count == 0:
            if num >> 5 == 0b110 or num >> 5 == 0b1110:
                count = 1
            elif num >> 4 == 0b1110:
                count = 2
            elif num >> 3 == 0b11110:
                count = 3
            elif num >> 7 == 0b1:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            count -= 1
    return count == 0
