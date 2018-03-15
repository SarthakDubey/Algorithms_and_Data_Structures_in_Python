#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def stupid(i):
	if i == 20: return
	print ('The stupid function calling stupid - iteration {}'.format(i))
	i += 1
	stupid(i)

i = 1
stupid(i)