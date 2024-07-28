#!/usr/bin/python3
'''make change funcion'''


def makeChange(coins, total):
    '''function that returun the fewest
     number of change needed to meet the total'''
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
