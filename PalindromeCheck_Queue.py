from collections import deque

def check_palindrome(str):
	que = deque()
	for s in str:
		que.append(s)
	Valid = True
	while len(que) > 1 and Valid:
		if que.pop() != que.popleft(): Valid = False
	return Valid
print(check_palindrome('ab21ba'))