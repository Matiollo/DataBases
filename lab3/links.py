from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, Table

Base = declarative_base()

companies_developers = Table(
    'companies_developers', Base.metadata,
    Column('company_id', Integer, ForeignKey('companies.id')),
    Column('developers_id', Integer, ForeignKey('developers.id'))
)

developers_projects = Table(
    'developers_projects', Base.metadata,
    Column('developer_id', Integer, ForeignKey('developers.id')),
    Column('project_id', Integer, ForeignKey('projects.id'))
)

companies_projects = Table(
    'companies_projects', Base.metadata,
    Column('company_id', Integer, ForeignKey('companies.id')),
    Column('project_id', Integer, ForeignKey('projects.id'))
)