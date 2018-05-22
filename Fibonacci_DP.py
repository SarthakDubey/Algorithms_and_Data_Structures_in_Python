import time
def fibonacci(fib, lookup={}):
    if fib <= 1:
        return 1
    elif fib not in lookup:
        lookup[fib] = fibonacci(fib-1) + fibonacci(fib-2)
    return lookup[fib]

def _fibonacci(fib):
    if fib <= 1:
        return 1
    else:
        return _fibonacci(fib-1) + _fibonacci(fib-2)

def main():
    fib = 25
    start = time.process_time()
   
    print(fibonacci(fib))
    
    print("Time :{}s".format(time.process_time()-start))

    start = time.process_time()
    
    print(_fibonacci(fib))

    print("Time :{}s".format(time.process_time()-start))

if __name__ == '__main__':
    main()
