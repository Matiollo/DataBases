from database import DB
from view import View
from models import Participant, Teacher, Competition

database = DB()
database.initiate()

view = View()
choice = 0

while choice != '27':
    print()
    choice = view.print_menu()
    if choice == '1':
        id = view.get_id()
        participant = database.find_participant_by_id(id)
        if type(participant) is str:
            view.print_mes(participant)
        else:
            view.print_entity(participant)
    if choice == '2':
        id = view.get_id()
        teacher = database.find_teacher_by_id(id)
        if type(teacher) is str:
            view.print_mes(teacher)
        else:
            view.print_entity(teacher)
    if choice == '3':
        id = view.get_id()
        competition = database.find_competition_by_id(id)
        if type(competition) is str:
            view.print_mes(competition)
        else:
            view.print_entity(competition)
    if choice == '4':
        id = view.get_id()
        participants = database.find_participants_by_teacher_id(id)
        if type(participants) is str:
            view.print_mes(participants)
        else:
            view.print_entities(participants)
    if choice == '5':
        sport = view.get_sport()
        competitions = database.find_competitions_by_sport(sport)
        if type(competitions) is str:
            view.print_mes(competitions)
        else:
            view.print_entities(competitions)
    if choice == '6':
        organizer = view.get_organizer()
        competitions = database.find_competitions_by_organizer(organizer)
        if type(competitions) is str:
            view.print_mes(competitions)
        else:
            view.print_entities(competitions)
    if choice == '7':
        participants = database.find_all_participants()
        if type(participants) is str:
            view.print_mes(participants)
        else:
            view.print_entities(participants)
    if choice == '8':
        teachers = database.find_all_teachers()
        if type(teachers) is str:
            view.print_mes(teachers)
        else:
            view.print_entities(teachers)
    if choice == '9':
        competitions = database.find_all_competitions()
        if type(competitions) is str:
            view.print_mes(competitions)
        else:
            view.print_entities(competitions)
    if choice == '10':
        entity = view.add_participant()
        participant = Participant(
            name=entity["name"],
            date_of_birth=entity["date_of_birth"],
            gender=entity["gender"],
            height=entity["height"],
            weight=entity["weight"],
            teacher_id=entity["teacher_id"]
        )
        mes = database.add_participant(participant)
        view.print_mes(mes)
    if choice == '11':
        entity = view.add_teacher()
        teacher = Teacher(
            name=entity["name"],
            date_of_birth=entity["date_of_birth"],
            started_practicing=entity["started_practicing"]
        )
        mes = database.add_teacher(teacher)
        view.print_mes(mes)
    if choice == '12':
        entity = view.add_competition()
        competition = Competition(
            name=entity["name"],
            sport=entity["sport"],
            organizer_name=entity["organizer_name"],
            budget=entity["budget"],
            country=entity["country"],
            year=entity["year"]
        )
        mes = database.add_competition(competition)
        view.print_mes(mes)
    if choice == '13':
        id = view.get_id()
        participant_old = database.find_participant_by_id(id)
        if participant_old is str:
            view.print_mes(participant_old)
            continue
        stu = view.update_participant()
        if not stu["name"]:
            stu["name"] = participant_old.name
        if not stu["height"]:
            stu["height"] = participant_old.height
        if not stu["weight"]:
            stu["weight"] = participant_old.weight
        participant = Participant(
            id=id,
            name=stu["name"],
            date_of_birth=participant_old.date_of_birth,
            gender=participant_old.gender,
            height=stu["height"],
            weight=stu["weight"],
            teacher_id=participant_old.teacher_id
        )
        mes = database.update_participant(participant)
        view.print_mes(mes)
    if choice == '14':
        id = view.get_id()
        teacher_old = database.find_teacher_by_id(id)
        if teacher_old is str:
            view.print_mes(teacher_old)
            continue
        stu = view.update_teacher()
        if not stu["name"]:
            stu["name"] = teacher_old.name
        teacher = Teacher(
            id=id,
            name=stu["name"],
            date_of_birth=teacher_old.date_of_birth,
            started_practicing=teacher_old.started_practicing
        )
        mes = database.update_teacher(teacher)
        view.print_mes(mes)
    if choice == '15':
        id = view.get_id()
        competition_old = database.find_competition_by_id(id)
        if competition_old is str:
            view.print_mes(competition_old)
            continue
        stu = view.update_competition()
        if not stu["name"]:
            stu["name"] = competition_old.name
        if not stu["sport"]:
            stu["sport"] = competition_old.sport
        if not stu["organizer_name"]:
            stu["organizer_name"] = competition_old.organizer_name
        if not stu["budget"]:
            stu["budget"] = competition_old.budget
        if not stu["country"]:
            stu["country"] = competition_old.country
        if not stu["year"]:
            stu["year"] = competition_old.year
        competition = Competition(
            id=id,
            name=stu["name"],
            sport=stu["sport"],
            organizer_name=stu["organizer_name"],
            budget=stu["budget"],
            country=stu["country"],
            year=stu["year"]
        )
        mes = database.update_competition(competition)
        view.print_mes(mes)
    if choice == '16':
        id = view.get_id()
        participant = database.find_participant_by_id(id)
        if participant is str:
            view.print_mes(participant)
            continue
        mes = database.remove_participant(id)
        view.print_mes(mes)
    if choice == '17':
        id = view.get_id()
        teacher = database.find_teacher_by_id(id)
        if teacher is str:
            view.print_mes(teacher)
            continue
        mes = database.remove_teacher(id)
        view.print_mes(mes)
    if choice == '18':
        id = view.get_id()
        competition = database.find_competition_by_id(id)
        if competition is str:
            view.print_mes(competition)
            continue
        mes = database.remove_competition(id)
        view.print_mes(mes)
    if choice == '19':
        res = view.get_participants_gender_name_teacher()
        participants = database.find_participants_by_gender_name_teacher(res["gender"], res["name"],
                                                                         res["teacher_name"])
        if type(participants) is str:
            view.print_mes(participants)
        else:
            view.print_entities(participants)
    if choice == '20':
        res = view.get_competitions_sport_height_range()
        competitions = database.find_competitions_by_sport_height_range(res["sport"], res["height_min"],
                                                                        res["height_max"])
        if type(competitions) is str:
            view.print_mes(competitions)
        else:
            view.print_entities(competitions)
    if choice == '21':
        number = view.get_number_generate()
        # mes = database.generate_participants(number)
        mes = database.generate_participants_with_normal_data(number)
        view.print_mes(mes)
    if choice == '22':
        number = view.get_number_generate()
        # mes = database.generate_teachers(number)
        mes = database.generate_teachers_with_normal_data(number)
        view.print_mes(mes)
    if choice == '23':
        number = view.get_number_generate()
        # mes = database.generate_competitions(number)
        mes = database.generate_competitions_with_normal_data(number)
        view.print_mes(mes)
    if choice == '24':
        number = view.get_number_generate()
        mes = database.generate_participants_competitions(number)
        view.print_mes(mes)
    if choice == '25':
        participant_id = view.get_id()
        res = database.count_competitions_of_each_year(participant_id)
        if type(res) is str:
            view.print_mes(res)
        else:
            view.show_plot_bar(res)
    if choice == '26':
        competition_id = view.get_id()
        res = database.count_participants_of_each_gender(competition_id)
        if type(res) is str:
            view.print_mes(res)
        else:
            view.show_plot_bar(res)
