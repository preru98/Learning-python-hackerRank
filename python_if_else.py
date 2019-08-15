#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if(n>=1 and n<=100):
    if(n % 2!=0):
        print("Weird", end="")
    else:
        if(n>=2 and n<=5):
            print("Not Weird", end="")
        elif(n>=6 and n<=20):
            print("Weird", end="")
        elif(n>20):
            print("Not Weird", end="")
else:
    print("Not in Range")