def Palindrome(s):
    return all (s[i] == s[~i] for i in range(len(s) //2))
print(Palindrome('aba'))

#Important here is that ~i = -(i+1) hence can be used in traversing list/array from both sides concurrently as arr[-ve number] starts from the end.