import csv


numTd = 0
with open('pbp-2021.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        if(row['OffenseTeam'] == 'NO' and row['IsTouchdown'] == '1'):
            numTd += 1
print(numTd)

# class Play:
#     def __init__(self) -> None:
#         pass
