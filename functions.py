import random

def hello_world():
    print('Hello world!')
    print()

hello_world() # nüüd kutsume välja funktsiooni

# Väljundiga funktsioon
def print_random_number():
    number = random.randint(1, 1000000)
    print('Suvaline number: ' + str(number))
    return number

# print_random_number()

funktsiooni_vaartus = print_random_number()
print('Siin on randomiks: ' + str(funktsiooni_vaartus)) # None - mittemidagi

# 
def compare_integers(num_1, num_2):
    if num_1 > num_2:
        # print('Esimene arv on suurem kui teine.') # Need ei ole väljundid
        return 1
    elif num_1 < num_2:
        # print('Esimene arv on väiksem kui teine.')
        return -1
    else:
        # print('Arvud on võrdsed.')
        return 0

for n in range(0, 10):

    random_1 = random.randint(1, 100)
    random_2 = random.randint(1, 100)

    output = compare_integers(random_1, random_2)
    if output > 0:
        print('Esimene arv(' + str(random_1) + ') on suurem kui teine arv(' + str(random_2) + '). output=' + str(output))
    elif output < 0:
        print('Esimene arv(' + str(random_1) + ') on väiksem kui teine arv(' + str(random_2) + '). output=' + str(output))
    else:
        print('Arvud on võrdsed(' + str(random_1) + ') ja (' + str(random_2) + ') . output=' + str(output))

