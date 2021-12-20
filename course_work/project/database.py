import psycopg2
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from models import Participant, Teacher, Competition
import pandas as pd


class DB:

    def __init__(self):
        self.s = None
        self._engine = None
        self._engine2 = None
        self.s2 = None

    def initiate(self):
        try:
            self._engine = create_engine('postgresql://postgres:Omezoh38@localhost:5432/course_work')
            self._engine2 = create_engine('postgresql://repl_user:Omezoh38@localhost:5432/course_work')
            session = sessionmaker(bind=self._engine)
            session2 = sessionmaker(bind=self._engine2)
            self.s = session()
            self.s2 = session2()
            print("Connect")
        except (Exception, exc.SQLAlchemyError) as error:
            print("Can`t connect to data base: ", error)

    def close(self):
        self.s.close()

    def find_participant_by_id(self, id):
        participant = None
        try:
            participant = self.s.query(Participant).get(id)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            participant = self.s2.query(Participant).get(id)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_participant_by_id():", error)
        if participant:
            return participant
        else:
            return "Can`t find participant by this id"

    def find_teacher_by_id(self, id):
        teacher = None
        try:
            teacher = self.s.query(Teacher).get(id)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            teacher = self.s2.query(Teacher).get(id)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_teacher_by_id():", error)
        if teacher:
            return teacher
        else:
            return "Can`t find teacher by this id"

    def find_competition_by_id(self, id):
        competition = None
        try:
            competition = self.s.query(Competition).get(id)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            competition = self.s2.query(Competition).get(id)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_competition_by_id():", error)
        if competition:
            return competition
        else:
            return "Can`t find competition by this id"

    def find_participants_by_teacher_id(self, teacher_id):
        participants = None
        try:
            participants = self.s.query(Participant).filter_by(teacher_id=teacher_id).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            participants = self.s2.query(Participant).filter_by(teacher_id=teacher_id).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_participants_by_teacher_id():", error)
        if participants:
            return participants
        else:
            return "Can`t find participants with this teacher id"

    def find_competitions_by_sport(self, sport):
        competitions = None
        try:
            competitions = self.s.query(Competition).filter_by(sport=sport).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            competitions = self.s2.query(Competition).filter_by(sport=sport).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_competitions_by_sport():", error)
        if competitions:
            return competitions
        else:
            return "Can`t find competitions by this sport"

    def find_competitions_by_organizer(self, organizer):
        competitions = None
        try:
            competitions = self.s.query(Competition).filter_by(organizer_name=organizer).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            competitions = self.s2.query(Competition).filter_by(organizer_name=organizer).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_competitions_by_organizer():", error)
        if competitions:
            return competitions
        else:
            return "Can`t find competitions by this organizer"

    def find_all_participants(self):
        participants = None
        try:
            participants = self.s.query(Participant).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            participants = self.s2.query(Participant).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_all_participants():", error)
        if participants:
            return participants
        else:
            return "Can`t find participants"

    def find_all_teachers(self):
        teachers = None
        try:
            teachers = self.s.query(Teacher).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            teachers = self.s2.query(Teacher).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_all_teachers():", error)
        if teachers:
            return teachers
        else:
            return "Can`t find teachers"

    def find_all_competitions(self):
        competitions = None
        try:
            competitions = self.s.query(Competition).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            competitions = self.s2.query(Competition).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_all_competitions():", error)
        if competitions:
            return competitions
        else:
            return "Can`t find competitions"

    def add_participant(self, participant):
        mes = self.find_teacher_by_id(participant.teacher_id)
        if mes == "Can`t find teacher by id":
            return "Teacher with entered id doesn't exist. Add is not successful"
        try:
            self.s.add(participant)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.add(participant)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_participant():", error)
            return "Add is not successful"
        return "Add is successful"

    def add_teacher(self, teacher):
        try:
            self.s.add(teacher)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.add(teacher)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_teacher():", error)
            return "Add is not successful"
        return "Add is successful"

    def add_competition(self, competition):
        try:
            self.s.add(competition)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.add(competition)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_competition():", error)
            return "Add is not successful"
        return "Add is successful"

    def update_participant(self, participant):
        u = None
        try:
            u = self.s.query(Participant).filter_by(id=participant.id).update(
                {Participant.name: participant.name, Participant.height: participant.height,
                 Participant.weight: participant.weight})
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            u = self.s2.query(Participant).filter_by(id=participant.id).update(
                {Participant.name: participant.name, Participant.height: participant.height,
                 Participant.weight: participant.weight})
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in update_participant():", error)
        if u:
            return "Update participant is successful"
        else:
            return "Can`t update participant"

    def update_teacher(self, teacher):
        u = None
        try:
            u = self.s.query(Teacher).filter_by(id=teacher.id).update(
                {Teacher.name: teacher.name})
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            u = self.s2.query(Teacher).filter_by(id=teacher.id).update(
                {Teacher.name: teacher.name})
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in update_teacher():", error)
        if u:
            return "Update teacher is successful"
        else:
            return "Can`t update teacher"

    def update_competition(self, competition):
        u = None
        try:
            u = self.s.query(Competition).filter_by(id=competition.id).update(
                {Competition.name: competition.name, Competition.sport: competition.sport,
                 Competition.organizer_name: competition.organizer_name, Competition.budget: competition.budget,
                 Competition.country: competition.country, Competition.year: competition.year})
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            u = self.s2.query(Competition).filter_by(id=competition.id).update(
                {Competition.name: competition.name, Competition.sport: competition.sport,
                 Competition.organizer_name: competition.organizer_name, Competition.budget: competition.budget,
                 Competition.country: competition.country, Competition.year: competition.year})
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in update_competition():", error)
        if u:
            return "Update competition is successful"
        else:
            return "Can`t update competition"

    def remove_participant(self, id):
        participant = self.find_participant_by_id(id)
        if type(participant) is not Participant:
            return "Can`t find by id"
        try:
            self.s.delete(participant)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.delete(participant)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in remove:", error)
            return "Delete is not successful"
        return "Delete is successful"

    def remove_teacher(self, id):
        teacher = self.find_teacher_by_id(id)
        if type(teacher) is not Teacher:
            return "Can`t find by id"
        try:
            self.s.delete(teacher)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.delete(teacher)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in remove:", error)
            return "Delete is not successful"
        return "Delete is successful"

    def remove_competition(self, id):
        competition = self.find_competition_by_id(id)
        if type(competition) is not Competition:
            return "Can`t find by id"
        try:
            self.s.delete(competition)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.delete(competition)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in remove:", error)
            return "Delete is not successful"
        return "Delete is successful"

    def find_participants_by_gender_name_teacher(self, gender, name, teacher_name):
        result = None
        try:
            result = self.s.execute(
                f"select participants.id, participants.name from participants inner join teachers on "
                f"participants.teacher_id=teachers.id where "
                f"gender='{gender}' and participants.name like '%{name}%' and teachers.name like '%{teacher_name}%'")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            result = self.s2.execute(
                f"select participants.id, participants.name from participants inner join teachers on "
                f"participants.teacher_id=teachers.id where "
                f"gender='{gender}' and participants.name like '%{name}%' and teachers.name like '%{teacher_name}%'")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_participants_by_gender_name_teacher():", error)
        if not result:
            return "Can`t find"
        return result

    def find_competitions_by_sport_height_range(self, sport, height_min, height_max):
        result = None
        try:
            result = self.s.execute(
                f"select competitions.id, competitions.name, participants.name, participants.height "
                f"from competitions inner join participants_competitions on "
                f"competitions.id=participants_competitions.competition_id "
                f"inner join participants on participants.id=participants_competitions.participant_id "
                f"where sport='{sport}' and participants.height > {height_min} and participants.height < {height_max}")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            result = self.s2.execute(
                f"select competitions.id, competitions.name, participants.name, participants.height "
                f"from competitions inner join participants_competitions on "
                f"competitions.id=participants_competitions.competition_id "
                f"inner join participants on participants.id=participants_competitions.participant_id "
                f"where sport='{sport}' and participants.height > {height_min} and participants.height < {height_max}")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_competitions_by_sport_height_range():", error)
        if not result:
            return "Can`t find"
        return result

    def generate_participants(self, number):
        self.define_get_random_teacher_id_func()
        try:
            self.s.execute(
                f"insert into participants(name,date_of_birth,gender,height,weight,teacher_id) "
                f"SELECT name,date_of_birth,gender,height,weight,teacher_id "
                f"FROM (SELECT (md5(random()::text)) as name, "
                f"(timestamp'1980-01-01'+ random()*(timestamp'2003-01-01'- timestamp'1980-01-01')) as date_of_birth, "
                f"(array['M','F'])[trunc(random()*2)+1] as gender, "
                f"trunc(random()*30+55) as height, "
                f"trunc(random()*100+45) as weight, "
                f"(getrandomteacherid()::int) as teacher_id "
                f"FROM generate_series(1, {number}) g) as rnd;")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.execute(
                f"insert into participants(name,date_of_birth,gender,height,weight,teacher_id) "
                f"SELECT name,date_of_birth,gender,height,weight,teacher_id "
                f"FROM (SELECT (md5(random()::text)) as name, "
                f"(timestamp'1980-01-01'+ random()*(timestamp'2003-01-01'- timestamp'1980-01-01')) as date_of_birth, "
                f"(array['M','F'])[trunc(random()*2)+1] as gender, "
                f"trunc(random()*30+55) as height, "
                f"trunc(random()*100+45) as weight, "
                f"(getrandomteacherid()::int) as teacher_id "
                f"FROM generate_series(1, {number}) g) as rnd;")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in generate_participants():", error)
            return "Failed to generate"
        return "Generated"

    def define_get_random_teacher_id_func(self):
        try:
            self.s.execute('create or replace function getrandomteacherid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id '
                            'FROM teachers '
                            'ORDER BY random() '
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;' 
                            '$$; ')
            self.s.commit()
        except exc.OperationalError:
            self.s2.execute('create or replace function getrandomteacherid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id '
                            'FROM teachers '
                            'ORDER BY random() '
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;'
                            '$$; ')
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in define_get_random_teacher_id_func():", error)

    def generate_teachers(self, number):
        try:
            self.s.execute(
                f"insert into teachers(name,date_of_birth,started_practicing) "
                f"SELECT name,date_of_birth,started_practicing "
                f"FROM (SELECT (md5(random()::text)||' '||(md5(random()::text))) as name, "
                f"(timestamp'1980-01-01'+ random()*(timestamp'2000-01-01'- timestamp'1980-01-01')) as date_of_birth, "
                f"(timestamp'2000-01-02'+ random()*(timestamp'2021-11-11'- timestamp'2000-01-02')) as started_practicing "
                f"FROM generate_series(1, {number}) g) as rnd;")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.execute(
                f"insert into teachers(name,date_of_birth,started_practicing) "
                f"SELECT name,date_of_birth,started_practicing "
                f"FROM (SELECT (md5(random()::text)||' '||(md5(random()::text))) as name, "
                f"(timestamp'1980-01-01'+ random()*(timestamp'2000-01-01'- timestamp'1980-01-01')) as date_of_birth, "
                f"(timestamp'2000-01-02'+ random()*(timestamp'2021-11-11'- timestamp'2000-01-02')) as started_practicing "
                f"FROM generate_series(1, {number}) g) as rnd;")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in generate_teachers():", error)
            return "Failed to generate"
        return "Generated"

    def generate_competitions(self, number):
        try:
            self.s.execute(
                f"insert into competitions(name,sport,organizer_name,budget,country,year) "
                f"SELECT name,sport,organizer_name,budget,country,year "
                f"FROM (SELECT (md5(random()::text)) as name, "
                f"(md5(random()::text)) as sport, "
                f"(md5(random()::text)) as organizer_name, "
                f"trunc(random()*70000+1000) as budget, "
                f"(md5(random()::text)) as country, "
                f"trunc(random()*70+1950) as year "
                f"FROM generate_series(1, {number}) g) as rnd;")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.execute(
                f"insert into competitions(name,sport,organizer_name,budget,country,year) "
                f"SELECT name,sport,organizer_name,budget,country,year "
                f"FROM (SELECT (md5(random()::text)) as name, "
                f"(md5(random()::text)) as sport, "
                f"(md5(random()::text)) as organizer_name, "
                f"trunc(random()*70000+1000) as budget, "
                f"(md5(random()::text)) as country, "
                f"trunc(random()*70+1950) as year "
                f"FROM generate_series(1, {number}) g) as rnd;")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in generate_competitions():", error)
            return "Failed to generate"
        return "Generated"

    def generate_participants_competitions(self, number):
        self.define_get_random_participant_id_func()
        self.define_get_random_competition_id_func()
        try:
            self.s.execute(
                f"insert into participants_competitions(participant_id, competition_id) "
                f"SELECT participant_id, competition_id "
                f"FROM (SELECT (getrandomparticipantid()::int) as participant_id, "
                f"(getrandomcompetitionid()::int) as competition_id "
                f"FROM generate_series(1, {number}) g) as rnd;")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.execute(
                f"insert into participants_competitions(participant_id, competition_id) "
                f"SELECT participant_id, competition_id "
                f"FROM (SELECT (getrandomparticipantid()::int) as participant_id, "
                f"(getrandomcompetitionid()::int) as competition_id "
                f"FROM generate_series(1, {number}) g) as rnd;")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in generate_participants_competitions():", error)
            return "Failed to generate"
        return "Generated"

    def define_get_random_participant_id_func(self):
        try:
            self.s.execute('create or replace function getrandomparticipantid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id '
                            'FROM participants '
                            'ORDER BY random() '
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;' 
                            '$$; ')
            self.s.commit()
        except exc.OperationalError:
            self.s2.execute('create or replace function getrandomparticipantid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id '
                            'FROM participants '
                            'ORDER BY random() '
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;' 
                            '$$; ')
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in define_get_random_participant_id_func():", error)

    def define_get_random_competition_id_func(self):
        try:
            self.s.execute('create or replace function getrandomcompetitionid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id '
                            'FROM competitions '
                            'ORDER BY random() '
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;' 
                            '$$; ')
            self.s.commit()
        except exc.OperationalError:
            self.s2.execute('create or replace function getrandomcompetitionid() returns text '
                            'language plpgsql '
                            'as '
                            '$$ '
                            'declare '
                            'outputInt int; '
                            'begin '
                            'SELECT id '
                            'FROM competitions '
                            'ORDER BY random() '
                            'LIMIT 1 '
                            'into outputInt; '
                            'return outputInt; '
                            'end;' 
                            '$$; ')
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in define_get_random_competition_id_func():", error)

    def count_competitions_of_each_year(self, participant_id):
        mes = self.find_participant_by_id(participant_id)
        if mes == "Can`t find participant by this id":
            return mes
        try:
            df1 = pd.read_sql_table('participants', self._engine)
            df2 = pd.read_sql_table('competitions', self._engine)
            df3 = pd.read_sql_table('participants_competitions', self._engine)
        except exc.OperationalError:
            print("Go to slave server")
            df1 = pd.read_sql_table('participants', self._engine2)
            df2 = pd.read_sql_table('competitions', self._engine2)
            df3 = pd.read_sql_table('participants_competitions', self._engine2)
        df1 = df1[df1.id == participant_id]
        df1 = df1.rename(columns={'id': 'participant_id', 'name': 'participant_name'})
        df2 = df2.rename(columns={'id': 'competition_id'})
        df = pd.merge(df1, df3, how='inner', on='participant_id')
        df = pd.merge(df, df2, how='inner', on='competition_id')
        final_df = df.groupby(['year'])['competition_id'].count()
        return final_df

    def count_participants_of_each_gender(self, competition_id):
        try:
            df1 = pd.read_sql_table('participants', self._engine)
            df2 = pd.read_sql_table('competitions', self._engine)
            df3 = pd.read_sql_table('participants_competitions', self._engine)
        except exc.OperationalError:
            print("Go to slave server")
            df1 = pd.read_sql_table('participants', self._engine2)
            df2 = pd.read_sql_table('competitions', self._engine2)
            df3 = pd.read_sql_table('participants_competitions', self._engine2)
        df2 = df2[df2.id == competition_id]
        df1 = df1.rename(columns={'id': 'participant_id'})
        df2 = df2.rename(columns={'id': 'competition_id', 'name': 'competition_name'})
        df = pd.merge(df1, df3, how='inner', on='participant_id')
        df = pd.merge(df, df2, how='inner', on='competition_id')
        final_df = df.groupby(['gender'])['participant_id'].count()
        return final_df
