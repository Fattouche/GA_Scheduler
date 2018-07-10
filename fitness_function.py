from collections import defaultdict

COURSE_INFO_ROOM_ID_INDEX = 0
COURSE_INFO_TIMESLOT_INDEX = 1
COURSE_INFO_DAYS_INDEX = 2
PREFERRED_START = 4
PREFERRED_END = 16


def calc_num_student_course_conflicts(chromosome, student_courses_dict):
    num_student_course_conflicts = 0

    for student in student_courses_dict:
        student_courses = student_courses_dict[student]

        # Get time slots of each course from the chromosome
        course_timeslots = [
            (chromosome[course][COURSE_INFO_TIMESLOT_INDEX],
            chromosome[course][COURSE_INFO_DAYS_INDEX])
            for course in student_courses
        ]

        # Sort the courses by start time
        # This is O(1) since number of courses a student can have is O(1)
        course_timeslots.sort(
            key=lambda timeslot: timeslot[0][0]
        )

        for i in range(1, len(course_timeslots)):
            prev_timeslot = course_timeslots[i-1][0]
            curr_timeslot = course_timeslots[i][0]

            prev_end_time = prev_timeslot[1]
            curr_start_time = curr_timeslot[0]

            if (curr_start_time <= prev_end_time):
                prev_days = course_timeslots[i-1][1]
                curr_days = course_timeslots[i][1]
                
                # Returns true if both strings contain a common char
                if (not set(prev_days).isdisjoint(curr_days)):
                    num_student_course_conflicts += 1

    return num_student_course_conflicts


def calc_num_course_room_time_conflicts(chromosome):
    num_course_room_time_conflicts = 0

    # Index this dict by (time, day)
    courses_per_time_and_day = defaultdict(set)

    for course_id in chromosome:
        course_info_list = chromosome[course_id]
        room_id = course_info_list[COURSE_INFO_ROOM_ID_INDEX]

        for time in range(course_info_list[COURSE_INFO_TIMESLOT_INDEX][0],
                          course_info_list[COURSE_INFO_TIMESLOT_INDEX][1] + 1):
            for day in course_info_list[COURSE_INFO_DAYS_INDEX]:
                if room_id in courses_per_time_and_day[(time, day)]:
                    num_course_room_time_conflicts += 1
                else:
                    courses_per_time_and_day[(time, day)].add(room_id)

    return num_course_room_time_conflicts


def calc_total_room_overflow(chromosome, room_information_dict,
                             course_students_dict):
    total_room_overflow = 0

    for course in chromosome:
        course_info_list = chromosome[course]
        room_id = course_info_list[COURSE_INFO_ROOM_ID_INDEX]

        room_capacity = room_information_dict[room_id]['capacity']
        num_students_in_course = len(course_students_dict[course])

        if (num_students_in_course > room_capacity):
            total_room_overflow += (num_students_in_course - room_capacity)

    return total_room_overflow


def calc_num_unfavoured_timeslots_used(chromosome):
    num_unfavoureds_slots = 0

    for class_id in chromosome:
        for time in range(chromosome[class_id][COURSE_INFO_TIMESLOT_INDEX][0],
                  chromosome[class_id][COURSE_INFO_TIMESLOT_INDEX][1] + 1):

          if time < PREFERRED_START or time > PREFERRED_END:
              num_unfavoureds_slots += 1

    return num_unfavoureds_slots


def calc_num_empty_seats_in_course_rooms(chromosome, room_information_dict, courses_student_dict):
    num_empty_seats = 0

    for class_id in chromosome:
        capacity = room_information_dict[class_id]["capacity"]
        enrolled = len(courses_student_dict[class_id])
        num_empty_seats += (capacity - enrolled)

    return num_empty_seats


def calc_fitness(chromosome, room_information_dict,
                 courses_student_dict, student_courses_dict):

    fitness = \
        1.0 * calc_num_student_course_conflicts(chromosome, student_courses_dict) \
        + 1.0 * calc_num_course_room_time_conflicts(chromosome) \
        + 1.0 * calc_total_room_overflow(chromosome, room_information_dict,
                                         course_students_dict) \
        + 0.1 * calc_num_unfavoured_timeslots_used(chromosome) \
        + 0.05 * calc_num_empty_seats_in_course_rooms(chromosome,
                                room_information_dict, courses_student_dict)

    return fitness


def is_valid(chromosome, room_information_dict, student_courses_dict, courses_student_dict):
    student_conflicts = calc_num_student_course_conflicts(
        chromosome, student_courses_dict)
    room_conflicts = calc_num_course_room_time_conflicts(chromosome)
    room_overflow = calc_total_room_overflow(
        chromosome, room_information_dict, courses_student_dict)

    return True if (student_conflicts == 0 and room_conflicts == 0 and room_overflow == 0) else False
