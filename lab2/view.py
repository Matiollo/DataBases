import structures as struct


class View:
    @staticmethod
    def generate_items():
        while True:
            print("Generate random data for DB tables? Y/N")
            res = input()
            if res == "Y" or res == "y":
                return True
            if res == "N" or res == "n":
                return False

    @staticmethod
    def get_number_of_items_to_generate(entity_type):
        num = -1
        while num <= 0:
            print(f"How many {entity_type} to generate?")
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
            if res == "C" or res == "c":
                return "companies"
            if res == "D" or res == "d":
                return "developers"
            if res == "P" or res == "p":
                return "projects"
            print("Type C, D or P.")

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
    def get_company_with_id():
        i = 0
        name = ""
        ceo = ""
        while i < 1:
            print("Write company's id:")
            try:
                i = int(input())
            except ValueError:
                print("Id must be a positive whole number.")
        while len(name) == 0:
            print("Write company's name:")
            name = input()
        while len(ceo) == 0:
            print("Write company's CEO:")
            ceo = input()
        company = struct.Company(i, name, ceo)
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
    def get_developer_with_id():
        i = 0
        name = ""
        specialization = ""
        while i < 1:
            print("Write developer's id:")
            try:
                i = int(input())
            except ValueError:
                print("Id must be a positive whole number.")
        while len(name) == 0:
            print("Write developer's name:")
            name = input()
        while len(specialization) == 0:
            print("Write developer's specialization:")
            specialization = input()
        developer = struct.Developer(i, name, specialization)
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
    def get_project_with_id():
        i = 0
        title = ""
        customer = ""
        budget = -1
        company_id = -1
        while i < 1:
            print("Write project's id:")
            try:
                i = int(input())
            except ValueError:
                print("Id must be a positive whole number.")
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
        project = struct.Project(i, title, customer, budget, company_id)
        return project

    @staticmethod
    def get_id(entity_type) -> int:
        i = -1
        while i <= 0:
            print(f"Write {entity_type}'s id: ")
            try:
                i = int(input())
            except ValueError:
                print("Id must be a positive whole number.")
        return i

    # search parameters

    @staticmethod
    def get_project_title():
        title = ""
        while len(title) == 0:
            print("Write project's title: ")
            title = input()
        return title

    @staticmethod
    def get_project_budget():
        budget = -1
        while budget <= 0:
            print("Write project's budget: ")
            try:
                budget = int(input())
            except ValueError:
                print("Budget must be a positive whole number.")
        return budget

    @staticmethod
    def get_developer_name():
        name = ""
        while len(name) == 0:
            print("Write developer's name: ")
            name = input()
        return name

    @staticmethod
    def get_developer_specialization():
        specialization = ""
        while len(specialization) == 0:
            print("Write developer's specialization: ")
            specialization = input()
        return specialization

    @staticmethod
    def get_project_customer():
        customer = ""
        while len(customer) == 0:
            print("Write project's customer: ")
            customer = input()
        return customer

    # result

    @staticmethod
    def print_inserted_entity(entity_type, i):
        print(f"{entity_type} was successfully inserted. Its id is {i}.")

    @staticmethod
    def print_inserted_project_error(company_id):
        print(f"Project was not inserted. Company with id {company_id} doesn't exist.")

    @staticmethod
    def print_updated_entity(entity_type):
        print(f"{entity_type} was successfully updated.")

    @staticmethod
    def print_update_error(entity_type, i):
        print(f"{entity_type} with id {i} does not exist and therefore it wasn't updated.")

    @staticmethod
    def print_updated_project_error(company_id):
        print(f"Project was not updated. Company with id {company_id} doesn't exist.")

    @staticmethod
    def print_deleted_entity(entity_type):
        print(f"{entity_type} was successfully deleted.")

    @staticmethod
    def print_delete_error(entity_type, i):
        print(f"{entity_type} with id {i} does not exist and therefore it wasn't deleted.")

    @staticmethod
    def print_companies(companies):
        print("COMPANIES:")
        for com in companies:
            print(f"Id: {com[0]}, Name: {com[1]}, CEO: {com[2]}")
        print()

    @staticmethod
    def print_developers(developers):
        print("DEVELOPERS:")
        for dev in developers:
            print(f"Id: {dev[0]}, Name: {dev[1]}, Specialization: {dev[2]}")
        print()

    @staticmethod
    def print_projects(projects):
        print("PROJECTS:")
        for proj in projects:
            print(f"Id: {proj[0]}, Title: {proj[1]}, Customer: {proj[2]}, Budget: {proj[3]}, "
                  f"Company id: {proj[4]}")
        print()

    @staticmethod
    def print_system_error():
        print("Some system error happened. Please ask Anastasiia to do check the program.")
