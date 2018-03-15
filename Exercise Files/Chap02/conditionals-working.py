#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x, y = 4, 4

if x < y:
	print(f'x {x} is less than y {y}')

#alternatively
if x < y: print ('X {} is less than Y {}'.format(x, y))
elif y <x : print ('LOL')
else : print ('There was nothing to do.')