import csv
from random import randrange


def get_competition_parameters_from_csv():
    try:
        with open('data/summer.csv') as csv_file:
            readCSV = list(csv.reader(csv_file, delimiter=',', quotechar='"'))
            index = randrange(0, 31164)
            row = readCSV[index]
            competition = {}
            competition["name"] = row[7]
            competition["sport"] = row[2]
            competition["organizer_name"] = row[1]
            competition["country"] = row[5]
            return competition
    except Exception as error:
        print("Error in get_competition_parameters_from_csv():", error)
        return "Failed to read"
