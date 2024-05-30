#!/usr/bin/python3

def pascal_triangle(n):
    """ this function is designed to genarate pascal trinagle"""
    pascal = []
    if n <= 0:
        return pascal

    pascal = [[1]]

    for i in range(1, n):
        temp = [1]
        for j in range(len(pascal[i - 1]) - 1):
            num = (pascal[i - 1][j] + pascal[i - 1][j + 1])
            temp.append(num)
        temp.append(1)
        pascal.append(temp)

    return (pascal)
