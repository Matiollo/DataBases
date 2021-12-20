from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey, Table, Date
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Participant(Base):
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_of_birth = Column(Date)
    gender = Column(Text)
    height = Column(Integer)
    weight = Column(Integer)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    participants_competitions = relationship("Participant_Competition", cascade="all, delete", backref="participants")

    def __repr__(self):
        return "<Participant (id={}, name='{}', date_of_birth='{}', gender='{}', height='{}', weight='{}', teacher_id='{}')>" \
            .format(self.id, self.name, self.date_of_birth, self.gender, self.height, self.weight, self.teacher_id)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_of_birth = Column(Date)
    started_practicing = Column(Date)
    participants = relationship("Participant", cascade="all, delete", backref="teachers")

    def __repr__(self):
        return "<Teacher(id={}, name='{}', date_of_birth='{}', started_practicing='{}')>" \
            .format(self.id, self.name, self.date_of_birth, self.started_practicing)


class Competition(Base):
    __tablename__ = 'competitions'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    sport = Column(Text)
    organizer_name = Column(Text)
    budget = Column(Integer)
    country = Column(Text)
    year = Column(Integer)
    participants_competitions = relationship("Participant_Competition", cascade="all, delete", backref="competitions")

    def __repr__(self):
        return "<competitions(id={}, name='{}', sport='{}', organizer_name='{}', budget='{}', country='{}', year='{}')>" \
            .format(self.id, self.name, self.sport, self.organizer_name, self.budget, self.country, self.year)


class Participant_Competition(Base):
    __tablename__ = 'participants_competitions'
    id = Column(Integer, primary_key=True)
    participant_id = Column(Integer, ForeignKey('participants.id'))
    competition_id = Column(Integer, ForeignKey('competitions.id'))

    def __repr__(self):
        return "<participant_id={}, competition_id={}>" \
            .format(self.participant_id, self.competition_id)
