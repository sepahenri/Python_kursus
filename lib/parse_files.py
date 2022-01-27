from csv import excel
import pandas

fail = pandas.read_excel('kategooriad.xlsx')
# print(fail.info())
# print(fail.head())
# print(fail)

summad = {} # {'Toidukaubad': 30, 'Manguasjad': 1000, ...}


# [0: [Kogus, Tyki hind], 1: [10. 3], 2: [100, 10]]
for kategooria in fail:
    print(kategooria)