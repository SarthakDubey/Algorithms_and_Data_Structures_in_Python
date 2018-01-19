def count_bits(x):
	num_bits = 0
	while x:
		num_bits += x & 1
		x = x >> 1
	return num_bits
a = input('Enter the number!\n')
print(count_bits(int(a)))