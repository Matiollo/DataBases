from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from links import companies_developers, companies_projects, developers_projects

Base = declarative_base()


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    ceo = Column('ceo', String)

    Developers = relationship("Developer", secondary=companies_developers)
    Projects = relationship("Project", secondary=companies_projects)

    def __init__(self, name: str, ceo: str):
        self.name = name
        self.ceo = ceo

    def __repr__(self):
        return "<Company(id='%s', name='%s', birthday='%s')>\n" % (
            self.id, self.name, self.ceo)


class Developer(Base):
    __tablename__ = 'developers'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    specialization = Column('specialization', String)

    Companies = relationship("Company", secondary=companies_developers)
    Projects = relationship("Project", secondary=developers_projects)

    def __init__(self, name: str, specialization: str):
        self.name = name
        self.specialization = specialization

    def __repr__(self):
        return "<Developer(id='%s', name='%s', specialization='%s')>\n" % (
            self.id, self.name, self.specialization)


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    customer = Column('customer', String)
    budget = Column('pages', Integer)

    Companies = relationship("Company", secondary=companies_projects)
    Developers = relationship("Developer", secondary=developers_projects)

    def __init__(self, title: str, customer: str, budget: int):
        self.title = title
        self.customer = customer
        self.budget = budget

    def __repr__(self):
        return "<Project(id='%s', title='%s', customer='%s', budget='%s')>\n" % (
            self.id, self.title, self.customer, self.budget)
