#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())


def isOdd(num):
    if num % 2:
        return True

    else:
        return False


decisionmaker = isOdd(N)

if decisionmaker:
    print('Weird')

else:
    if 2 <= N and N <= 5:
        print('Not Weird')

    elif N >= 6 and N <= 20:
        print('Weird')

    else:
        print('Not Weird')


