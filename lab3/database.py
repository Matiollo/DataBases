import models
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import time


class Database:
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:Omezoh38@localhost:5435/public', echo=True)
        self.session = sessionmaker(bind=self.engine)()

    def close(self):
        self.session.close()

    # CUD methods

    def insert_company(self, company):
        try:
            self.session.add(company)
            self.session.commit()
            self.session.refresh(company)
            return company.id
        except Exception as err:
            print("Add error: ", err)
            raise err

    def update_company(self, company):
        try:
            item = self.session.query(models.Company).filter_by(id=company.id).update(
                {models.Company.name: company.name, models.Company.ceo: company.ceo})
            self.session.commit()
            if item:
                return 1
            else:
                return 0
        except (Exception, SQLAlchemyError) as err:
            self.session.rollback()
            print("Update error: ", err)

    def delete_company(self, i):
        try:
            item = self.get_company_by_id(i)
            if type(item) is not models.Company:
                return 0
            c = self.session.delete(item)
            self.session.commit()
            return 1
        except(Exception, SQLAlchemyError) as error:
            self.session.rollback()
            print("Delete error: ", error)

    def get_company_by_id(self, i):
        try:
            return self.session.query(models.Company).get(i)
        except Exception as err:
            print("Get by id error! ", err)
            raise err

    def insert_developer(self, developer):
        try:
            self.session.add(developer)
            self.session.commit()
            self.session.refresh(developer)
            return developer.id
        except Exception as err:
            print("Add error: ", err)
            raise err

    def update_developer(self, developer):
        try:
            item = self.session.query(models.Developer).filter_by(id=developer.id).update(
                {models.Developer.name: developer.name, models.Developer.specialization: developer.specialization})
            self.session.commit()
            if item:
                return 1
            else:
                return 0
        except (Exception, SQLAlchemyError) as err:
            self.session.rollback()
            print("Update error: ", err)

    def delete_developer(self, i):
        try:
            item = self.get_developer_by_id(i)
            if type(item) is not models.Developer:
                return 0
            c = self.session.delete(item)
            self.session.commit()
            return 1
        except(Exception, SQLAlchemyError) as error:
            self.session.rollback()
            print("Delete error: ", error)

    def get_developer_by_id(self, i):
        try:
            return self.session.query(models.Developer).get(i)
        except Exception as err:
            print("Get by id error! ", err)
            raise err

    def insert_project(self, project):
        try:
            self.session.add(project)
            self.session.commit()
            self.session.refresh(project)
            return project.id
        except Exception as err:
            print("Add error: ", err)
            raise err

    def update_project(self, project):
        try:
            item = self.session.query(models.Project).filter_by(id=project.id).update(
                {models.Project.title: project.title, models.Project.customer: project.customer,
                 models.Project.budget: project.budget})
            self.session.commit()
            if item:
                return 1
            else:
                return 0
        except (Exception, SQLAlchemyError) as err:
            self.session.rollback()
            print("Update error: ", err)

    def delete_project(self, i):
        try:
            item = self.get_project_by_id(i)
            if type(item) is not models.Project:
                return 0
            c = self.session.delete(item)
            self.session.commit()
            return 1
        except(Exception, SQLAlchemyError) as error:
            self.session.rollback()
            print("Delete error: ", error)

    def get_project_by_id(self, i):
        try:
            return self.session.query(models.Project).get(i)
        except Exception as err:
            print("Get by id error! ", err)
            raise err
