# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#dayoftheweek

def whatdayoftheweek():
    month = input("what month is it? (Enter Numerical Values)")
    m = int (month)

    day = input("what day is it? (Enter Numerical Values)" )
    d = int(day)

    year = input("what year is it? (Enter Numerical Values)")
    y = int(year)

    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31*m0) // 12) % 7
    
    print (d0)
    
    
whatdayoftheweek()