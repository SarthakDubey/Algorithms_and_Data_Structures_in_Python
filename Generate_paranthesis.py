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


class Solution:
    def generateParenthesis(self, n, left=0, right=0, s=''):
        """
        :type n: int
        :rtype: List[str]
        """
        array = []
        if right == n:
            return s
        array.append(s)
        if left < n:
            s = self.generateParenthesis(n, left+1, right, s+'(')
        if right < left:
            s = self.generateParenthesis(n, left, right+1, s+')')
        return array

a = Solution()
print(a.generateParenthesis(2))