from collections import defaultdict

COURSE_INFO_ROOM_ID_INDEX = 0
COURSE_INFO_TIMESLOT_INDEX = 1
COURSE_INFO_DAYS_INDEX = 2
PREFERRED_START = 4
PREFERRED_END = 16

class FitnessCalculator:
    def __init__(self, room_information_dict, course_students_dict, student_courses_dict,
                fitness_threshold):
        self.room_information_dict = room_information_dict
        self.course_students_dict = course_students_dict
        self.student_courses_dict = student_courses_dict
        self.fitness_threshold = fitness_threshold


    def calc_num_student_course_conflicts(self, chromosome):
        num_student_course_conflicts = 0

        for student in self.student_courses_dict:
            student_courses = self.student_courses_dict[student]

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


    def calc_num_course_room_time_conflicts(self, chromosome):
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


    def calc_total_room_overflow(self, chromosome):
        total_room_overflow = 0

        for course in chromosome:
            course_info_list = chromosome[course]
            room_id = course_info_list[COURSE_INFO_ROOM_ID_INDEX]

            room_capacity = self.room_information_dict[room_id]['capacity']
            num_students_in_course = len(self.course_students_dict[course])

            if (num_students_in_course > room_capacity):
                total_room_overflow += (num_students_in_course - room_capacity)

        return total_room_overflow


    def calc_num_unfavoured_timeslots_used(self, chromosome):
        num_unfavoureds_slots = 0

        for class_id in chromosome:
            for time in range(chromosome[class_id][COURSE_INFO_TIMESLOT_INDEX][0],
                            chromosome[class_id][COURSE_INFO_TIMESLOT_INDEX][1] + 1):

                if time < PREFERRED_START or time > PREFERRED_END:
                    num_unfavoureds_slots += 1
        return num_unfavoureds_slots


    def calc_num_empty_seats_in_course_rooms(self, chromosome):
        num_empty_seats = 0
        if(self.calc_total_room_overflow(chromosome) > 0):
            return num_empty_seats
        for class_id in chromosome:
            capacity = self.room_information_dict[chromosome[class_id][0]]["capacity"]
            enrolled = len(self.course_students_dict[class_id])
            num_empty_seats += (capacity - enrolled)
        return num_empty_seats


    def calc_fitness(self, chromosome):
        fitness = \
            1.0 * self.calc_num_student_course_conflicts(chromosome) \
            + 1.0 * self.calc_num_course_room_time_conflicts(chromosome) \
            + 1.0 * self.calc_total_room_overflow(chromosome) \
            + 0.1 * self.calc_num_unfavoured_timeslots_used(chromosome) \
            + 0.05 * self.calc_num_empty_seats_in_course_rooms(chromosome)

        return fitness


    def is_valid(self, chromosome):
        if chromosome is None:
            return False
        student_conflicts = self.calc_num_student_course_conflicts(chromosome)
        room_conflicts = self.calc_num_course_room_time_conflicts(chromosome)
        room_overflow = self.calc_total_room_overflow(chromosome)

        return True if (student_conflicts == 0 and room_conflicts == 0 and room_overflow == 0) else False


    def fittest_chromosome(self, population):
        min_fitness = self.fitness_threshold
        fittest_chromosome = None
        for chromosome in population:
            chromosome_fitness = self.calc_fitness(chromosome)
            if chromosome_fitness < min_fitness:
                fittest_chromosome = chromosome
                min_fitness = chromosome_fitness
        return fittest_chromosome
