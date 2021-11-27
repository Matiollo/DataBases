import psycopg2
import structures
import time


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(dbname='lab1', user='postgres',
                            password='Omezoh38', host='127.0.0.1', port='5432')
            self.cursor = self.connection.cursor()
            print("Connected")
        except(Exception, psycopg2.Error) as error:
            print('Error with connection', error)

    def prepare_for_data_generation(self):
        self.define_generate_string_func()
        self.define_generate_int_func()
        self.define_get_random_company_id_func()
        self.define_get_random_developer_id_func()
        self.define_get_random_project_id_func()

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Connection closed")

    # functions for data generation

    def define_generate_string_func(self):
        self.cursor.execute("create or replace function generateString(length int) "
                            "returns text "
                            "language plpgsql "
                            "as "
                            "$$ "
                            "declare "
                            "outputString text; "
                            "begin "
                            "select string_agg(chr(trunc(97 + random()*25)::int), '') "
                            "from generate_series(1, length) "
                            "into outputString; "
                            "return outputString; "
                            "end; "
                            "$$; ")
        self.connection.commit()

    def define_generate_int_func(self):
        self.cursor.execute('create or replace function generateint(max integer) returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'select trunc(random() * max + 1) '
                            'into outputInt; '
                            'return outputInt; '
                            'end; '
                            '$$; ')
        self.connection.commit()

    def define_get_random_company_id_func(self):
        self.cursor.execute('create or replace function getrandomcompanyid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id '
                            'FROM companies '
                            'ORDER BY random() '
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;' 
                            '$$; ')
        self.connection.commit()

    def define_get_random_developer_id_func(self):
        self.cursor.execute('create or replace function getrandomdeveloperid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id '
                            'FROM developers '
                            'ORDER BY random() '
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;' 
                            '$$; ')
        self.connection.commit()

    def define_get_random_project_id_func(self):
        self.cursor.execute('create or replace function getrandomprojectid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id '
                            'FROM projects '
                            'ORDER BY random() ' 
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;' 
                            '$$; ')
        self.connection.commit()

    # data generation

    def generate_companies(self, number):
        # start_time = time.time()
        try:
            self.cursor.execute(f'INSERT INTO companies (name,ceo)'
                                f'SELECT generatestring(15),'
                                f'generatestring(15)'
                                f'FROM generate_series(1, {number})')
            self.connection.commit()
        except Exception as err:
            print("Generate companies error! ", err)
        # end_time = time.time()
        # return str(end_time - start_time)[:9] + 's'

    def generate_developers(self, number):
        # start_time = time.time()
        try:
            self.cursor.execute(f'INSERT INTO developers (name,specialization)'
                                f'SELECT generatestring(15),'
                                f'generatestring(15)'
                                f'FROM generate_series(1, {number})')
            self.connection.commit()
        except Exception as err:
            print("Generate developers error! ", err)
        # end_time = time.time()
        # return str(end_time - start_time)[:9] + 's'

    def generate_projects(self, number):
        # start_time = time.time()
        try:
            self.cursor.execute(f"INSERT INTO projects (title,customer,budget,company_id) "
                                f"SELECT generatestring(15), "
                                f"generatestring(15), "
                                f"generateint(100000)::int, "
                                f"getrandomcompanyid()::int "
                                f"FROM generate_series(1, {number})")
            # self.cursor.execute(f"INSERT INTO projects (title,customer,budget,company_id) "
            #                     f"SELECT generatestring(15), "
            #                     f"generatestring(15), "
            #                     f"generateint(100000)::int, "
            #                     f"getrandomcompanyid()::int "
            #                     f"FROM generate_series(1, {number})")
            self.connection.commit()
        except Exception as err:
            print("Generate projects error! ", err)
        # end_time = time.time()
        # return str(end_time - start_time)[:9] + 's'

    def fill_companies_developers_table(self, number):
        try:
            self.cursor.execute(f"INSERT  INTO companies_developers (company_id, developers_id) "
                                f"SELECT getrandomcompanyid()::int, "
                                f"getrandomdeveloperid()::int "
                                f"FROM generate_series(1, {number})")
            self.connection.commit()
        except Exception as err:
            print("fill_companies_developers_table error! ", err)

    def fill_developers_projects_table(self, number):
        try:
            self.cursor.execute(f"INSERT  INTO developers_projects (developer_id, project_id) "
                                f"SELECT getrandomdeveloperid()::int, "
                                f"getrandomprojectid()::int "
                                f"FROM generate_series(1, {number})")
            self.connection.commit()
        except Exception as err:
            print("fill_developers_projects_table error! ", err)

    # CUD methods

    def insert_company(self, company):
        self.cursor.execute(f"INSERT INTO public.companies(name, ceo) VALUES ('{company.name}', '{company.ceo}');"
                            f"SELECT currval('companies_id_seq');")
        new_id = self.cursor.fetchone()[0]
        self.connection.commit()
        return new_id

    def update_company(self, company):
        self.cursor.execute(f"WITH rows AS (UPDATE public.companies SET name='{company.name}', ceo='{company.ceo}' "
                            f"WHERE id={company.id} RETURNING 1)"
                            f"SELECT count(*) FROM rows;")
        updated = self.cursor.fetchone()[0]
        self.connection.commit()
        return updated

    def delete_company(self, i):
        self.cursor.execute(f'DELETE FROM developers_projects where project_id in (select id from projects where company_id={i});'
                            f'DELETE FROM public.projects WHERE company_id={i};'
                            f'DELETE FROM public.companies_developers WHERE company_id={i};'
                            f'WITH rows AS (DELETE FROM public.companies WHERE id={i} RETURNING 1)'
                            f'SELECT count(*) FROM rows;')
        deleted = self.cursor.fetchone()[0]
        self.connection.commit()
        return deleted

    def insert_developer(self, developer):
        self.cursor.execute(f"INSERT INTO public.developers(name, specialization) "
                            f"VALUES ('{developer.name}', '{developer.specialization}');"
                            f"SELECT currval('developers_id_seq');")
        new_id = self.cursor.fetchone()[0]
        self.connection.commit()
        return new_id

    def update_developer(self, developer):
        self.cursor.execute(f"WITH rows AS (UPDATE public.developers SET name='{developer.name}', "
                            f"specialization='{developer.specialization}' WHERE id={developer.id} RETURNING 1)"
                            f"SELECT count(*) FROM rows;")
        updated = self.cursor.fetchone()[0]
        self.connection.commit()
        return updated

    def delete_developer(self, i):
        self.cursor.execute(f'DELETE FROM public.companies_developers WHERE developers_id={i};'
                            f'DELETE FROM public.developers_projects WHERE developer_id={i};'
                            f'WITH rows AS (DELETE FROM public.developers WHERE id={i} RETURNING 1)'
                            f'SELECT count(*) FROM rows;')
        deleted = self.cursor.fetchone()[0]
        self.connection.commit()
        return deleted

    def insert_project(self, project):
        self.cursor.execute(f"SELECT COUNT (*) FROM companies WHERE id={project.company_id};")
        num = self.cursor.fetchone()[0]
        print(num)

        if num != 0:
            self.cursor.execute(f"INSERT INTO public.projects(title, customer, budget, company_id) "
                                f"VALUES ('{project.title}', '{project.customer}', {project.budget}, {project.company_id});"
                                f"SELECT currval('projects_id_seq');")
            new_id = self.cursor.fetchone()[0]
            self.connection.commit()
            return new_id
        else:
            return -1

    def update_project(self, project):
        self.cursor.execute(f"SELECT COUNT (*) FROM companies WHERE id={project.company_id};")
        num = self.cursor.fetchone()[0]

        if num != 0:
            self.cursor.execute(f"WITH rows AS (UPDATE public.projects SET title='{project.title}', "
                                f"customer='{project.customer}', budget={project.budget}, "
                                f"company_id={project.company_id} WHERE id={project.id} RETURNING 1)"
                                f"SELECT count(*) FROM rows;")
            updated = self.cursor.fetchone()[0]
            self.connection.commit()
            return updated
        else:
            return -1

    def delete_project(self, i):
        self.cursor.execute(f'DELETE FROM public.developers_projects WHERE project_id={i};'
                            f'WITH rows AS (DELETE FROM public.projects WHERE id={i} RETURNING 1)'
                            f'SELECT count(*) FROM rows;')
        deleted = self.cursor.fetchone()[0]
        self.connection.commit()
        return deleted

    # search methods

    def search_for_projects(self, dev_id, proj_title, proj_budget: int):
        try:
            self.cursor.execute(
                f"SELECT p.id, p.title, p.customer, p.budget, p.company_id from projects as p "
                f"inner join developers_projects on developers_projects.project_id = p.id "
                f"Where developer_id = {dev_id} and title = '{proj_title}' and budget = {proj_budget}")
            return self.cursor.fetchall()
        except Exception as err:
            print("search_for_projects error", err)

    def search_for_developers(self, com_id, proj_id, dev_name, dev_specialization):
        try:
            self.cursor.execute(
                f"SELECT d.id, d.name, d.specialization from developers as d "
                f"inner join developers_projects on developers_projects.developer_id = d.id "
                f"inner join companies_developers on companies_developers.developers_id = d.id "
                f"Where project_id = {proj_id} and company_id = {com_id} and name = '{dev_name}' "
                f"and specialization = '{dev_specialization}'")
            return self.cursor.fetchall()
        except Exception as err:
            print("search_for_developers error", err)

    def search_for_companies(self, proj_budget, proj_customer, dev_specialization):
        try:
            self.cursor.execute(
                f"SELECT c.id, c.name, c.ceo from companies as c "
                f"inner join projects on projects.company_id = c.id "
                f"inner join companies_developers on companies_developers.company_id = c.id "
                f"inner join developers on companies_developers.company_id = developers.id "
                f"Where budget = {proj_budget} and customer = '{proj_customer}' and specialization = '{dev_specialization}'")
            return self.cursor.fetchall()
        except Exception as err:
            print("search_for_companies error", err)
