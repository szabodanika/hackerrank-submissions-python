#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 0:
        # even
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n <= 20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        # odd
        print("Weird")

