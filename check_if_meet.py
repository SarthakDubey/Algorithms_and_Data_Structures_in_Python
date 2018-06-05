def check(a, b, c, d):
    if a == c and b ==d:
        return True
    if a > c or b > d:
        return False
    return check(a+b, b, c, d) or check(a, a+b, c, d)   
print(check(1, 2, 65, 46))

"""Check if right movement or upwards movement -> a, b -> a+b, b and a, b-> a, a+b leads to a point c, d"""

def check_target(a, b, c):
    if b<=a:
        return -1
    job_a = a
    job_b = b
    day = 0
    while job_b < job_a+c:
        day+=1
        job_a+=a
        job_b+=b
    return day

print(check_target(50, 51, 150))    