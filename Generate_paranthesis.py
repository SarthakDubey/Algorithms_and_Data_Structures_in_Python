def paranthesis(number, left, right, s):
    if right == number:
        print (s)
        return
    if left < number:
        paranthesis(number, left+1, right, s+'(')
    if right < left:
        paranthesis(number, left, right+1, s+')')

if __name__ == '__main__':
    s = ''
    paranthesis(2, 0, 0, s)
