import structures as struct


class View:
    @staticmethod
    def generate_items():
        while True:
            print("Generate random data for DB tables? Y/N")
            res = input()
            if res == "Y":
                return True
            if res == "N":
                return False

    @staticmethod
    def get_number_of_items_to_generate(entity_type):
        num = -1
        while num <= 0:
            print("How many {} to generate?", entity_type)
            try:
                num = int(input())
            except ValueError:
                print("Number of items must be a positive whole number.")
        return num

    @staticmethod
    def display_menu():
        choice = 0
        while choice < 1 or choice > 5:
            print("Choose what you want to do:")
            print("1. Insert data")
            print("2. Update data")
            print("3. Search for data")
            print("4. Delete data")
            print("5. Exit")
            try:
                choice = int(input())
            except ValueError:
                print("Write a number from 1 to 5.")
        return choice

    @staticmethod
    def choose_item_type():
        while True:
            print("What entities do you want to work with? Companies (C) / Developers (D) / Projects (P)")
            res = input()
            if res == "C":
                return "companies"
            if res == "D":
                return "developers"
            if res == "P":
                return "projects"

    @staticmethod
    def choose_search_type():
        choice = 0
        while choice < 1 or choice > 3:
            print("There are 3 types of searches available. Type in the number of the most suitable.")
            print("1. Returns PROJECTS by developer's id, project's title and budget;")
            print("2. Returns DEVELOPERS by company's id, project's id, developer's name and specialization")
            print("3. Returns COMPANIES that run projects with certain budget and customer's name and on which work "
                  "developers with certain specialization")
            try:
                choice = int(input())
            except ValueError:
                print("Write a number from 1 to 3.")
        return choice

    # CUD parameters
    @staticmethod
    def get_company():
        name = ""
        ceo = ""
        while len(name) == 0:
            print("Write company's name:")
            name = input()
        while len(ceo) == 0:
            print("Write company's CEO:")
            ceo = input()
        company = struct.Company(-1, name, ceo)
        return company

    @staticmethod
    def get_developer():
        name = ""
        specialization = ""
        while len(name) == 0:
            print("Write developer's name:")
            name = input()
        while len(specialization) == 0:
            print("Write developer's specialization:")
            specialization = input()
        developer = struct.Developer(-1, name, specialization)
        return developer

    @staticmethod
    def get_project():
        title = ""
        customer = ""
        budget = -1
        company_id = -1
        while len(title) == 0:
            print("Write project's title:")
            title = input()
        while len(customer) == 0:
            print("Write customer's name:")
            customer = input()
        while budget <= 0:
            print("Write project's budget:")
            try:
                budget = int(input())
            except ValueError:
                print("Budget must be a positive whole number.")
        while company_id <= 0:
            print("Write id of the company that runs the project:")
            try:
                company_id = int(input())
            except ValueError:
                print("Company id must be a positive whole number.")
        project = struct.Project(-1, title, customer, budget, company_id)
        return project

    @staticmethod
    def get_id(entity_type):
        i = -1
        while i <= 0:
            print("Write {}'s id: ".format(entity_type))
            try:
                i = int(input())
            except ValueError:
                print("Id must be a positive whole number.")
        return i

    # search parameters

    @staticmethod
    def get_developer_id():
        print("Write developer's id: (if you don't want to sort by it, enter anything but a whole positive number.")
        try:
            i = int(input())
            if i >= 1:
                return i
            return -1
        except ValueError:
            return -1

    @staticmethod
    def get_project_title():
        print("Write project's title: (if you don't want to sort by it, leave the field blank.")
        title = input()
        return title

    @staticmethod
    def get_project_budget():
        print("Write project's budget: (if you don't want to sort by it, enter anything but a whole positive number.")
        try:
            budget = int(input())
            if budget >= 1:
                return budget
            return 0
        except ValueError:
            return 0

    @staticmethod
    def get_company_id():
        print("Write company's id: (if you don't want to sort by it, enter anything but a whole positive number.")
        try:
            i = int(input())
            if i >= 1:
                return i
            return -1
        except ValueError:
            return -1

    @staticmethod
    def get_project_id():
        print("Write project's id: (if you don't want to sort by it, enter anything but a whole positive number.")
        try:
            i = int(input())
            if i >= 1:
                return i
            return -1
        except ValueError:
            return -1

    @staticmethod
    def get_developer_name():
        print("Write developer's name: (if you don't want to sort by it, leave the field blank.")
        name = input()
        return name

    @staticmethod
    def get_developer_specialization():
        print("Write developer's specialization: (if you don't want to sort by it, leave the field blank.")
        specialization = input()
        return specialization

    @staticmethod
    def get_project_customer():
        print("Write project's customer: (if you don't want to sort by it, leave the field blank.")
        customer = input()
        return customer

    # result

    @staticmethod
    def print_inserted_entity(entity_type, id):
        print("{} was successfully inserted. Its id is {}.".format(entity_type, id))

    @staticmethod
    def print_updated_entity(entity_type):
        print("{} was successfully updated.".format(entity_type))

    @staticmethod
    def print_update_error(entity_type, id):
        print("{} with id {} does not exist and therefore it wasn't updated.".format(entity_type, id))

    @staticmethod
    def print_deleted_entity(entity_type):
        print("{} was successfully deleted.".format(entity_type))

    @staticmethod
    def print_delete_error(entity_type, id):
        print("{} with id {} does not exist and therefore it wasn't deleted.".format(entity_type, id))

    @staticmethod
    def print_companies(companies):
        for com in companies:
            print("Id:", com.id, ", Name:", com.name, ", CEO:", com.ceo)

    @staticmethod
    def print_developers(developers):
        for dev in developers:
            print("Id:", dev.id, ", Name:", dev.name, ", Specialization:", dev.specialization)

    @staticmethod
    def print_projects(projects):
        for proj in projects:
            print("Id:", proj.id, ", Title:", proj.title, ", Customer:", proj.customer,
                  ", Budget:", proj.budget, ", Company id:", proj.company_id)
