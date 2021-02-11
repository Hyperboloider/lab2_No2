import os
from classes import Team


def path_input():
    choice = input('What kind of path you want to insert?\nRelative-"r", Absolute-"a":\n')
    if choice == 'r':
        directory = input('Insert the directory name: ')
        path = os.getcwd() + '\\' + directory +'\\'
        return path
    elif choice == 'a':
        path = input('Insert the path: ')
        return path
    else:
        print("unsupported choice")

def find_csv(directory):
    csvs = []
    for f in files:
        if f.endswith(".csv"):
            csvs.append(f)
    return csvs

def team_creator(directory, csvs, teams):
    for csv in csvs:
        with open(directory + csv, 'r') as table:
            numberOfRows = int(table.readline())
            for _ in range(numberOfRows):
                teams.append(Team(table.readline()))

def sorter(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = lst[len(lst)//2]
        less = [n for n in lst if n < mid]
        equal = [n for n in lst if n == mid]
        bigger = [n for n in lst if n > mid]

        return sorter(bigger) + equal + sorter(less)

def create_csv(teams):
    with open("result.csv", "w") as result:
        for position in range(len(teams)):
            result.write(f"{position + 1},{teams[position].name},{teams[position].points},{','.join(teams[position].games)}\n")

directory = path_input()
files = os.listdir(directory)
teams = []
csvs = find_csv(directory)
team_creator(directory, csvs, teams)
teams = sorter(teams)
create_csv(teams)

print("================================================")
for team in teams:
    print (team.name, team.points)