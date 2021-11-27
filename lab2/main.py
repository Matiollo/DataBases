import structures

import psycopg2
from database import Database
from view import View
database = Database()
database.connect()
view = View()

#try:
generate = view.generate_items()
if generate:
    com_num = view.get_number_of_items_to_generate("companies")
    dev_num = view.get_number_of_items_to_generate("developers")
    proj_num = view.get_number_of_items_to_generate("projects")

    database.prepare_for_data_generation()

    database.generate_companies(com_num)
    database.generate_developers(dev_num)
    database.generate_projects(proj_num)
    database.fill_companies_developers_table(dev_num)
    database.fill_developers_projects_table(int(proj_num*4))

while True:
    choice = view.display_menu()
    if choice == 5:
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
        search_type = view.choose_search_type()
        if search_type == 1:
            dev_id = view.get_id("developer")
            proj_title = view.get_project_title()
            proj_budget = view.get_project_budget()
            projects = database.search_for_projects(dev_id, proj_title, proj_budget)
            view.print_projects(projects)
        elif search_type == 2:
            com_id = view.get_id("company")
            proj_id = view.get_id("project")
            dev_name = view.get_developer_name()
            dev_specialization = view.get_developer_specialization()
            developers = database.search_for_developers(com_id, proj_id, dev_name, dev_specialization)
            view.print_developers(developers)
        elif search_type == 3:
            proj_budget = view.get_project_budget()
            proj_customer = view.get_project_customer()
            dev_specialization = view.get_developer_specialization()
            companies = database.search_for_companies(proj_budget, proj_customer, dev_specialization)
            view.print_companies(companies)
    elif choice == 4:
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
# except Exception as err:
#     view.print_system_error()
