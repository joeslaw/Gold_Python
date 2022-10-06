#!/usr/bin/env python3.7

value = int(input("Enter an integer value: "))
if value % 5 == 0 and value % 3 == 0:
    print("FizBuzz")
elif value % 3 == 0:
    print("Fiz")
elif value % 5 == 0:
    print("Buzz")
    
else:
    print(value)