import structures

import psycopg2
from database import Database
from view import View
database = Database()
view = View()

try:
    while True:
        choice = view.display_menu()
        if choice == 4:
            database.close()
            break
        if choice == 1:
            entity_type = view.choose_item_type()
            if entity_type == "companies":
                company = view.get_company()
                res = database.insert_company(company)
                view.print_inserted_entity("Company", res)
            elif entity_type == "developers":
                developer = view.get_developer()
                res = database.insert_developer(developer)
                view.print_inserted_entity("Developer", res)
            elif entity_type == "projects":
                project = view.get_project()
                res = database.insert_project(project)
                if res != -1:
                    view.print_inserted_entity("Project", res)
                else:
                    view.print_inserted_project_error(project.company_id)
        elif choice == 2:
            entity_type = view.choose_item_type()
            if entity_type == "companies":
                company = view.get_company_with_id()
                res = database.update_company(company)
                if res == 0:
                    view.print_update_error("Company", company.id)
                else:
                    view.print_updated_entity("Company")
            elif entity_type == "developers":
                developer = view.get_developer_with_id()
                res = database.update_developer(developer)
                if res == 0:
                    view.print_update_error("Developer", developer.id)
                else:
                    view.print_updated_entity("Developer")
            elif entity_type == "projects":
                project = view.get_project_with_id()
                res = database.update_project(project)
                if res == -1:
                    view.print_updated_project_error(project.company_id)
                elif res == 0:
                    view.print_update_error("Project", project.id)
                else:
                    view.print_updated_entity("Project")
        elif choice == 3:
            entity_type = view.choose_item_type()
            if entity_type == "companies":
                i = view.get_id("company")
                res = database.delete_company(i)
                if res == 0:
                    view.print_delete_error("Company", i)
                else:
                    view.print_deleted_entity("Company")
            elif entity_type == "developers":
                i = view.get_id("developer")
                res = database.delete_developer(i)
                if res == 0:
                    view.print_delete_error("Developer", i)
                else:
                    view.print_deleted_entity("Developer")
            elif entity_type == "projects":
                i = view.get_id("project")
                res = database.delete_project(i)
                if res == 0:
                    view.print_delete_error("Project", i)
                else:
                    view.print_deleted_entity("Project")
except Exception as err:
    view.print_system_error()
