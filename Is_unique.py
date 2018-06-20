if __name__ == '__main__':
    #CTCI 1.1
    string = "How about this?"
    dictionary = set()
    for s in string:
        if s in dictionary:
            print('Not Unique')
            break
        else:
            dictionary.add(s)
    