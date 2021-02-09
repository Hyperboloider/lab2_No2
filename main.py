import os

directory = "D:/homework2/lab2/csvs/"
files = os.listdir(directory)
csvs = []
teams = []

def find_csv(directory):
    csvs = []
    for f in files:
        if f.endswith(".csv"):
            csvs.append(f)
    return csvs

csvs = find_csv(directory)

print(csvs)

for csv in csvs:
    with open(directory + csv, 'r') as table:
        numberOfRows = int(table.readline())
        for _ in range(numberOfRows):
            print(table.readline(), end='')
        print('\n')