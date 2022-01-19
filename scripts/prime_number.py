
start = int(input('Sisesta algus: '))
end = int(input('Sisesta lõpp: '))

count = 0

print()
for x in range(start, end):
    if (x > 1):
        for divider in range(2, x):
            if x % divider == 0:
                break
        else:
            print(x)
            count += 1

print('\nKokku on selles vahemikus ' + str(count) + ' algarvu.')
