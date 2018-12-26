#!/usr/bin/env python3
from math import log
print("NOTE: Hit Ctrl-C to interrupt the program")
print("NOTE: Values too large for float representation will be printed in a logarithmic scale")
c = int(input("Enter value for c : "))
n = 3
try:
    while True:
        n += 1
        goal = c**n
        logGoal = log(goal)
        for a in range(1,c):
            for b in range(1,c):
                test = a**n + b**n
                if test > goal:
                    break
                if (test == goal):
                    print("Fermat disproved, publish these values and you'll be famous: a = %d, b = %d, c = %d, n = %d" % (a,b,c,n))
                    exit(0)
                else:
                    try:
                        print("a: %d, b: %d, c: %d, n: %d | a^n + b^n: %.2E | c^n: %.2E" % (a,b,c,n,test,goal))
                    except OverflowError:
                        logTest = log(test)
                        print("a: %d, b: %d, c: %d, n: %d | log(a^n + b^n): %.2E | log(c^n): %.2E" % (a,b,c,n,logTest,logGoal))
except KeyboardInterrupt:
    print("Script interrupted...")
