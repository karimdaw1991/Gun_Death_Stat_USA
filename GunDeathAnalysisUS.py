import datetime
import csv

file = open("guns.csv","r")

data = list(csv.reader(file))
print(data[:10])

headers = data[0]

data = data[1:]

print(data[:5])

years = [int(row[1]) for row in data]
month = [int(row[2]) for row in data]
print(years[:30])

year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] = year_counts[year] + 1
    else:
        year_counts[year] = + 1

#print(year_counts)

dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day =1) for row in data]

date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] = date_counts[date] + 1
    else:
        date_counts[date] = + 1
print(date_counts)

sexs = [row[5] for row in data]

sex_counts = {}
for sex in sexs:
    if sex in sex_counts:
        sex_counts[sex] = sex_counts[sex] + 1
    else:
        sex_counts[sex] = + 1

races = [row[7] for row in data]

race_counts = {}
for race in races:
    if race in race_counts:
        race_counts[race] = race_counts[race] + 1
    else:
        race_counts[race] = + 1

f = open('census.csv', 'r')
census = csv.reader(f)
for row in census:
    #print(row[16])


mapping = {'White': 197318956,'Hispanic':44618105,'Black':40250635,
'Native American/Native Alaskan': 3739506,
'Asian/Pacific Islander':15159516 + 674625,
}

race_per_hundredk = {}

for key_race, key_mapping in zip(race_counts.items(),mapping.items()):
    print(key_race[0])
    num = 100000 * (key_race[1]/key_mapping[1])
    count = 0
    if key_race[0] in race_per_hundredk:
        print('already in here')
        pass
    else:
        race_per_hundredk[key_race[0]] = num

#print(race_per_hundredk)

intents = [intent[3] for intent in data]
races = [race[7] for race in data]

homicide_race_counts = {}

for index, race in enumerate(races):

    if intents[index] == 'Homicide':
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 1
        else:
            homicide_race_counts[race] += 1
#print(homicide_race_counts)

for key_race, key_mapping in zip(homicide_race_counts.items(),mapping.items()):
    #print(key_race[0])
    num = 100000 * (key_race[1]/key_mapping[1])
    homicide_race_counts[key_race[0]] = num

#print(homicide_race_counts)
