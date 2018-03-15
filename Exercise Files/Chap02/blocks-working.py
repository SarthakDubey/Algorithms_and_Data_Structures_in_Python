#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 51
y = 73

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))

x = x + y
y = y - x

if y < x:
	print(f'x < y : x is {x} and y is {y}')
