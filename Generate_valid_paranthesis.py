def print_all_parens(n):
    def print_parens(left, right, s):
        if right == n:
            print(s)
            return
        if left < n:
            print_parens(left + 1, right, s + "(")
        if right < left:
            print_parens(left, right + 1, s + ")")

    print_parens(0, 0, "")


print_all_parens(2)

def print_all_paranthesis(n):
    def print_paranthesis(left, right, s):
        if right == n:
            print(s)
            return
        if left < n:
            print_paranthesis(left+1, right, s + "(")
        if right < left:
            print_paranthesis(left, right+1, s + ")")
    print_paranthesis(0, 0, "")