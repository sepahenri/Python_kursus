size = int(input('Vali püramiidi suurus: '))
k = 0

for i in range(1, size + 1):
    for space in range(1, (size - i) + 1):
        print(end = '  ')
    
    while k != (2 * i - 1):
        print('* ', end = '')
        k += 1
    
    k = 0
    print() # Seda on vaja, et uuele reale liikuda