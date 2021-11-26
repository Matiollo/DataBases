from typing import NamedTuple


class Company(NamedTuple):
    id: int
    name: str
    ceo: str


class Developer(NamedTuple):
    id: int
    name: str
    specialization: str


class Project(NamedTuple):
    id: int
    title: str
    customer: str
    budget: int
    company_id: int