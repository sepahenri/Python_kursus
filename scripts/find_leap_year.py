from_year = int(input('Sisesta aasta alates, millest soovid liigaastaid kuvada: '))

year = 2022

# for year in range(from_year, year, 4):
#     print(year)



# if year % 400 == 0 and year % 100 == 0:
#     print(str(year) + ' on liigaasta')

# elif year % 4 == 0 and year % 100 != 0:
#     print(str(year) + ' on liigaasta')

# else:
#     print(str(year) + ' ei ole liigaasta')


if from_year % 400 == 0 and year % 100 == 0:
    for year in range(from_year, year, 4):
        print(year)

elif from_year % 4 == 0 and year % 100 != 0:
    for year in range(from_year, year, 4):
        print(year)

else:
    print(str(from_year) + ' ei ole liigaasta')