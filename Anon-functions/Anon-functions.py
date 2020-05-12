def anonFunction(n):
    '''Takes a random number n and prints 0 to n-1.'''
    
    print('Number chosen = {}'.format(n))
    functions = [lambda x=x : x for x in range(n)]
    for f in functions:
        print(f())

anonFunction(n = np.random.randint(1, 50))