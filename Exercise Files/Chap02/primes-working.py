#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def check_prime(n):
	if n <=1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	else:
		return True

def list_primes(n):
	for x in range (0, n):
		if check_prime(x) == True: print(x, end = ' ')

list_primes(100)
print()
print(multiprocessing.cpu_count())