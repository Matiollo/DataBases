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
        self.cursor.execute('create or replace function generateString(length int) '
                            'returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputString text; '
                            'begin '
                            'select string_agg(chr(trunc(97 + random()*25)::int), '') '
                            'from generate_series(1, length) '
                            'into outputString; '
                            'return outputString; '
                            'end; '
                            '$$; ')
        self.connection.commit()

    def define_generate_int_func(self):
        self.cursor.execute('create function generateint(max integer) returns text '
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
        self.cursor.execute('create function getrandomcompanyid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id'
                            'FROM companies'
                            'ORDER BY random()'
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;' 
                            '$$; ')
        self.connection.commit()

    def define_get_random_developer_id_func(self):
        self.cursor.execute('create function getrandomdeveloperid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id'
                            'FROM developers'
                            'ORDER BY random()'
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;' 
                            '$$; ')
        self.connection.commit()

    def define_get_random_project_id_func(self):
        self.cursor.execute('create function getrandomprojectid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id'
                            'FROM projects'
                            'ORDER BY random()'
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;' 
                            '$$; ')
        self.connection.commit()

    # not needed method
    # def get_all_companies(self):
    #     self.cursor.execute("SELECT * FROM public.companies")
    #     self.connection.commit()
    #     return self.cursor.fetchall()

    # data generation

    def generate_companies(self, number):
        # start_time = time.time()
        try:
            self.cursor.execute(f'INSERT  INTO companies (name,ceo)'
                                f' SELECT generatestring(15),'
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
            self.cursor.execute(f'INSERT  INTO developers (name,specialization)'
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
            self.cursor.execute(f"INSERT  INTO projects (title,customer,budget,company_id)"
                                f"SELECT generatestring(15),"
                                f"generatestring(15),"
                                f"generateint(100000)::int, "
                                f"getrandomcompanyid()::int"
                                f"FROM generate_series(1, {number})")
            self.connection.commit()
        except Exception as err:
            print("Generate projects error! ", err)
        # end_time = time.time()
        # return str(end_time - start_time)[:9] + 's'

    def fill_companies_developers_table(self, number):
        try:
            self.cursor.execute(f"INSERT  INTO companies_developers (company_id, developers_id)"
                                f"SELECT getrandomcompanyid()::int,"
                                f"getrandomdeveloperid()::int"
                                f"FROM generate_series(1, {number})")
            self.connection.commit()
        except Exception as err:
            print("fill_companies_developers_table error! ", err)

    def fill_developers_projects_table(self, number):
        try:
            self.cursor.execute(f"INSERT  INTO developers_projects (developer_id, project_id)"
                                f"SELECT getrandomdeveloperid()::int,"
                                f"getrandomprojectid()::int"
                                f"FROM generate_series(1, {number})")
            self.connection.commit()
        except Exception as err:
            print("fill_developers_projects_table error! ", err)

    # CUD methods

    def insert_company(self, company):
        self.cursor.execute("INSERT INTO public.companies(name, ceo) VALUES (%name, %ceo);", (company.name, company.ceo))
        self.connection.commit()
        new_id = self.cursor.execute("SELECT currval('companies_id_seq');")
        return new_id

    def update_company(self, company):
        self.cursor.execute("UPDATE public.companies SET name=%name, ceo=%ceo WHERE id=%id;", (company.name, company.ceo, company.id))
        updated = self.cursor.rowcount()
        self.connection.commit()
        # delete next line
        print(updated)
        return updated

    def delete_company(self, i):
        self.cursor.execute("DELETE FROM public.companies WHERE id=%id;", i)
        deleted = self.cursor.rowcount()
        self.connection.commit()
        return deleted

    def insert_developer(self, developer):
        print("not done")

    def update_developer(self, developer):
        print("not done")

    def delete_developer(self, i):
        print("not done")

    def insert_project(self, project):
        print("not done")

    def update_project(self, project):
        print("not done")

    def delete_project(self, i):
        print("not done")

    # search methods

    def search_for_projects(self, dev_id, proj_title, proj_budget):
        #

    def search_for_developers(self, com_id, proj_id, dev_name, dev_specialization):
        #

    def search_for_companies(self, proj_budget, proj_customer, dev_specialization):
        #