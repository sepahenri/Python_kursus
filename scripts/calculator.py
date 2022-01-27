 # Loome 4 funktiooni, liida, lahuta, korruta, jaga


# Küsime kasutajalt input väärtused
arv1 = input('Sisesta esimene arv: ')
arv2 = input('Sisesta teine arv: ')

# Defineerime funktsioonid
def liida(arv1, arv2):
    summa = float(arv1) + float(arv2)
    return summa

def lahuta(arv1, arv2):
    vahe = float(arv1) - float(arv2)
    return vahe

def korruta(arv1, arv2):
    korrutis = float(arv1) * float(arv2)
    return korrutis

def jaga(arv1, arv2):
    jagatis = float(arv1) / float(arv2)
    return jagatis

# Kutsume välja kõik fuktsioonid
summa = liida(arv1, arv2)
vahe = lahuta(arv1, arv2)
korrutis = liida(arv1, arv2)
jagatis = liida(arv1, arv2)

# Prindime tulemused
print('\nTulemused\n=========')
print('Kahe arvu summa on ' + str(summa))
print('Kahe arvu vahe on ' + str(vahe))
print('Kahe arvu korrutis on ' + str(korrutis))
print('Kahe arvu jagatis on ' + str(jagatis))