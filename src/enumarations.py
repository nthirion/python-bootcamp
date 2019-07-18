

if __name__ == '__main__':
    l1 = ['eat','run','work','run','eat','sleep']
    s1 = 'thirion'

    print(list(enumerate(l1)))
    print(list(enumerate(s1)))

    for c, el in enumerate(l1):
        print(c, el)
