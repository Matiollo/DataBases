import csv
import random


class TextReading:
    @staticmethod
    def get_random_participant_name():
        try:
            name = ''
            surname = ''
            with open('./csv_files/names.csv') as f1:
                reader = csv.reader(f1)
                name = random.choice(list(reader))
            with open('./csv_files/surnames.csv') as f2:
                reader = csv.reader(f2)
                surname = random.choice(list(reader))
            res = name + " " + surname
            return res
        except:
            return 'Anna'
