#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    unique = set(s)

    # Counting unique charaters in the company name
    n = []
    for i in unique:
        n.append((i, s.count(i)))

    n.sort()
    n.sort(key=lambda x: x[1], reverse=True)

    print(n[0][0], n[0][1])
    print(n[1][0], n[1][1])
    print(n[2][0], n[2][1])
