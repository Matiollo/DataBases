import datetime
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('xtick', labelsize=8)


class View:
    @staticmethod
    def print_menu():
        choice = -1
        while not (choice in range(28)):
            print("Select an option:")
            print("1. Find a participant by id")
            print("2. Find a teacher by id")
            print("3. Find a competition by id")
            print("4. Find all students of teacher's id")
            print("5. Find all competitions on a particular sport")
            print("6. Find all competitions by a particular organizer")
            print("7. Find all participants")
            print("8. Find all teachers")
            print("9. Find all competitions")
            print("10. Add a participant")
            print("11. Add a teacher")
            print("12. Add a competition")
            print("13. Update a participant")
            print("14. Update a teacher")
            print("15. Update a competition")
            print("16. Delete a participant")
            print("17. Delete a teacher")
            print("18. Delete a competition")
            print("19. Find participant of a particular gender and where name like some text and teacher's name is" 
                  "like some text.")
            print("20. Find competition on a particular sport with participants whose height is between some range.")
            print("21. Generate participants")
            print("22. Generate teachers")
            print("23. Generate competitions")
            print("24. Generate participants and competitions connections")
            print("25. Count competitions of each year for a particular participant")
            print("26. Count participants of each gender for a particular competition")
            print("27. Exit ")
            try:
                choice = int(input ("Enter your choice:"))
            except Exception:
                print("Enter a number between 1 and 26.")
                continue
        return str(choice)

    @staticmethod
    def get_id():
        id = 0
        while True:
            try:
                id = int(input("Enter id:"))
                if id < 1:
                    print("Enter positive integer.")
                    continue
            except ValueError:
                print("Enter integer.")
                continue
            break
        return id

    def print_entities(self, entities):
        try:
            for entity in entities:
                print(entity)
        except TypeError:
            self.print_entity(entities)

    @staticmethod
    def print_entity(entity):
        print(entity)

    @staticmethod
    def get_number_generate():
        number = 0
        while True:
            try:
                number = int(input("Enter number for generate:"))
                if number < 0:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return number

    @staticmethod
    def print_mes(mes):
        print(mes)

    @staticmethod
    def get_sport():
        sport = input("Enter sport:")
        return sport

    @staticmethod
    def get_organizer():
        organizer = input("Enter organizer's name:")
        return organizer

    def add_participant(self):
        participant={}
        participant["name"] = input("Enter full name:")
        print("Date of birth:")
        participant["date_of_birth"] = self.get_date()
        while True:
            participant["gender"] = input("Enter gender M or F:")
            if participant["gender"] != "M" and participant["gender"] != "F":
                print("You should enter M or F.")
                continue
            break
        while True:
            try:
                participant["height"] = int(input("Enter height in inches:"))
                if participant["height"] < 25:
                    print("Height cannot be smaller than 25 inches.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            break
        while True:
            try:
                participant["weight"] = int(input("Enter weight in kg:"))
                if participant["weight"] < 10:
                    print("Weight cannot be smaller than 10 kg.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            break
        while True:
            try:
                participant["teacher_id"] = int(input("Enter teacher_id:"))
                if participant["teacher_id"] < 1:
                    print("You must enter positive integer.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            break
        return participant

    @staticmethod
    def get_date():
        date = datetime.date(1, 1, 1)
        while True:
            try:
                year = int(input("Enter year:"))
                month = int(input("Enter month:"))
                day = int(input("Enter day: "))
                if (year < 1) or (month < 1) or (day < 1):
                    print("You must enter positive integer.")
                    continue
                if year < 1801:
                    print("Year should be bigger than 1800.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            try:
                date = datetime.date(year, month, day)
                break
            except ValueError as e:
                print(e)
        return date

    def add_teacher(self):
        teacher = {}
        teacher["name"] = input("Enter full name:")
        print("Date of birth:")
        teacher["date_of_birth"] = self.get_date()
        while True:
            print("Date of the day started practicing:")
            teacher["started_practicing"] = self.get_date()
            if teacher["date_of_birth"] > teacher["started_practicing"]:
                print("Date of the day started practicing cannot be earlier than date of birth.")
                continue
            break
        return teacher

    @staticmethod
    def add_competition():
        competition = {}
        competition["name"] = input("Enter name of the competition:")
        competition["sport"] = input("Enter type of sport:")
        competition["organizer_name"] = input("Enter organizer's name:")
        while True:
            try:
                competition["budget"] = int(input("Enter budget:"))
                if competition["budget"] < 0:
                    print("Budget must be a positive number.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            break
        competition["country"] = input("Enter country:")
        while True:
            try:
                competition["year"] = int(input("Enter year:"))
                if competition["year"] < 1801:
                    print("Year must be bigger than 1800.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            break
        return competition

    @staticmethod
    def update_participant():
        participant = {}
        participant["name"] = input("Enter full name or nothing:")
        while True:
            try:
                participant["height"] = int(input("Enter height in inches:"))
                if participant["height"] < 25:
                    print("Height cannot be smaller than 25 inches.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            break
        while True:
            try:
                participant["weight"] = int(input("Enter weight in kg:"))
                if participant["weight"] < 10:
                    print("Weight cannot be smaller than 10 kg.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            break
        return participant

    @staticmethod
    def update_teacher():
        teacher = {}
        teacher["name"] = input("Enter full name or nothing:")
        return teacher

    @staticmethod
    def update_competition():
        competition = {}
        competition["name"] = input("Enter name of the competition or nothing:")
        competition["sport"] = input("Enter type of sport or nothing:")
        competition["organizer_name"] = input("Enter organizer's name or nothing:")
        while True:
            try:
                competition["budget"] = int(input("Enter budget or 0:"))
                if competition["budget"] < 0:
                    print("Budget must be a positive number.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            break
        competition["country"] = input("Enter country or nothing:")
        while True:
            try:
                competition["year"] = int(input("Enter year:"))
                if competition["year"] < 1801:
                    print("Year must be bigger than 1800.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            break
        return competition

    @staticmethod
    def get_participants_gender_name_teacher():
        result={}
        result["name"] = input("Enter name:")
        while True:
            result["gender"] = input("Enter gender M or F:")
            if result["gender"] != "M" and result["gender"] != "F":
                print("You should enter M or F.")
                continue
            break
        result["teacher_name"] = input("Enter teacher_name:")
        return result

    @staticmethod
    def get_competitions_sport_height_range():
        result = {}
        result["sport"] = input("Enter sport:")
        while True:
            try:
                result["height_min"] = int(input("Enter min height in inches:"))
                if result["height_min"] < 25:
                    print("Height cannot be smaller than 25 inches.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            break
        while True:
            try:
                result["height_max"] = int(input("Enter max height in inches:"))
                if result["height_max"] < 25:
                    print("Height cannot be smaller than 25 inches.")
                    continue
                if result["height_max"] < result["height_min"]:
                    print("Max height cannot be smaller than min height.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            break
        return result

    @staticmethod
    def get_year():
        while True:
            try:
                year = int(input("Enter year:"))
                if year < 1800:
                    print("Year must be bigger than 1800.")
                    continue
            except ValueError:
                print("You should enter integer.")
                continue
            return year

    @staticmethod
    def show_plot_bar(entity):
        entity.plot.bar()
        plt.show()
