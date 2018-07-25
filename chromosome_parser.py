import xml_parser as parser
import datetime

def parse_chromosome(chromosome, course_students_dict):
    print("{:^10} {:^10} {:^10} {:^10} {:^10} {:^10}".format( "Class", "Room", "From", "To", "Days", "Students"))
    for class_id in chromosome:
        students_in_class = course_students_dict[class_id]
        start_and_end_time = get_time_from_timeslot(chromosome[class_id][1])
        days = chromosome[class_id][2]
        room_number = chromosome[class_id][0]
        print("{:^10} {:^10} {:^10} {:^10} {:^10} {}".format(class_id, room_number, start_and_end_time[0], start_and_end_time[1], days, students_in_class))
        print()


def get_time_from_timeslot(timeslot):
    first_timeslot_of_day = datetime.datetime(100,1,1,8,00,00)
    start_time = first_timeslot_of_day + datetime.timedelta(0,timeslot[0]*60*30)
    end_time = first_timeslot_of_day + datetime.timedelta(0,timeslot[1]*60*30)
    return ['{}:{:02d}'.format(start_time.time().hour, start_time.time().minute), '{}:{:02d}'.format(end_time.time().hour, end_time.time().minute)]

